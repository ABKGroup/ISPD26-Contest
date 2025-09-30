# ================== environment & setup ==================
set top_proj_dir    "$::env(TOP_PROJ_DIR)"
set proj_dir        "$::env(PROJ_DIR)"
set design_name     "$::env(DESIGN_NAME)"
set crfile          "$::env(CONGESTION_REPORT)"
set folder          "$::env(FOLDER_NAME)"

set lib_setup_file    "lib_setup.tcl"
set design_setup_file "design_setup.tcl"

set start [clock seconds]
source $lib_setup_file
source $design_setup_file

# ================== helpers ==================

# Returns 1 if placement looks legal, 0 otherwise.
proc is_placement_legal {} {
  # If check_placement throws (e.g. DPL-0386), treat as illegal.
  if {[catch { check_placement -verbose } err]} {
    puts "check_placement reported errors: $err"
    return 0
  }
  return 1
}

# ================== (1) read tech, libs, DEF, netlist, link ==================
foreach lef_file ${lefs}    { read_lef     $lef_file }
foreach lib_file ${libbest} { read_liberty $lib_file }

read_def      $def_file
read_verilog  $verilog_netlist

read_sdc $sdc_file
#set_propagated_clock [get_clocks *]
set_ideal_network [all_clocks]

# Keep units exactly as requested
set_cmd_units -time ns -capacitance pF -current mA -voltage V -resistance kOhm -distance um -power mW
set_units -power mW

# ================== (2) legalization if needed ==================
puts "### Check placement legality ###"
set placement_legal [is_placement_legal]
if {$placement_legal} {
  puts "Placement is legal; skip legalization."
} else {
  puts "Placement NOT legal; running detailed_placement..."

  detailed_placement
  # Best-effort re-check
  set placement_legal [is_placement_legal]
  if {$placement_legal} {
    puts "Placement legalized."
  } else {
    puts stderr "WARN: Placement still illegal after detailed_placement."
  }
}

# ================== (3) global route with auto-legalize retry ==================
# Route layer setup (override via design_setup.tcl if provided)
if {[info exists route_signal_layers]} { set sig_layers $route_signal_layers } else { set sig_layers "M2-M9" }
if {[info exists route_clock_layers]}  { set clk_layers $route_clock_layers }  else { set clk_layers "M2-M9" }

set_routing_layers -signal $sig_layers -clock $clk_layers
#set_global_routing_layer_adjustment * 0.5

puts "### Global routing (first attempt) ###"
set placement_legal 1
if {[catch { global_route -allow_congestion -congestion_report_file $crfile } gr_err]} {
  # If GR fails (e.g., unplaced inst), legalize then retry
  puts "INFO: global_route failed on first attempt: $gr_err"
  puts "INFO: running detailed_placement, then retrying global_route..."
  set placement_legal 0

  detailed_placement
  if {[catch { global_route -allow_congestion } gr_err2]} {
    puts stderr "ERROR: global_route still failing after detailed_placement: $gr_err2"
    exit 2
  }
}

# Estimate parasitics using global routing
estimate_parasitics -global_routing

set end [clock seconds]

# ================== (4) evaluation metrics (OpenSTA + OpenROAD) ==================
set TOTAL_INSTS [llength [get_cells *]]
puts "===== METRICS ====="
puts "design:                 $design_name"
puts "placement_legal:        $placement_legal"
puts [format "total_insts:            %d" $TOTAL_INSTS]
report_units
report_tns
report_wns
report_power



# ---- global routing overflow -----
puts "Start Global Routing Results Analysis ..."
set block [ord::get_db_block]
set gcellgrid [$block getGCellGrid]
set tech [$block getTech]
set layers {}
foreach layer [$tech getLayers] {
  set routing_level [$layer getRoutingLevel]
  if {$routing_level > 0} {
    lappend layers $layer
  }
}

# set layers [lsort -unique $layers]
set gird_x_count [llength [$gcellgrid getGridX]]
set gird_y_count [llength [$gcellgrid getGridY]]

## For loop for x from 0 to gird_x_count - 1
for {set x 0} {$x < $gird_x_count} {incr x} {
  for {set y 0} {$y < $gird_y_count} {incr y} {
    set capacity_value 0
    set usage_value 0
    foreach layer $layers {
      set capacity [$gcellgrid getCapacity $layer $x $y]
      set usage [$gcellgrid getUsage $layer $x $y]
      set capacity_value [expr $capacity_value + $capacity]
      set usage_value [expr $usage_value + $usage]
    }
    set congestion 0
    if {$capacity_value > 0} {
    set congestion [expr ($usage_value *100.0) / $capacity_value]
    }
    puts "$x $y $capacity_value $usage_value $congestion"
  }
}
puts "End Global Routing Results Analysis ..."


report_check_types -max_slew         -violators 
report_check_types -max_capacitance  -violators 
report_check_types -max_fanout       -violators 


puts "\[INFO\] Flow running time:   [expr {$end - $start}] second"