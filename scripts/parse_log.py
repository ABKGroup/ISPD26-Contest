#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse OpenROAD log to extract evaluation metrics.

python3 parse_log.py evaluation.log --csv metrics.csv

Metrics extracted (when present):
- design
- placement_legal (0/1)
- total_insts
- wns, tns (kept in the log's time unit)
- slew_over_sum, slew_over_count
- cap_over_sum,  cap_over_count
- fanout_over_sum, fanout_over_count
- leakage_power, total_power (unit-converted if a power unit banner exists)
- max_gr_overflow, total_gr_overflow
- legal_fail_summary (DPL failure types)
- tool_runtime (seconds)
- flow_runtime (seconds)
"""

import re
import csv
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, Tuple, Optional

FLOAT = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?"
ANSI = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")  # strip ANSI color if any

OR_RSZ_RUNTIME_RE = re.compile(
    rf"^\s*(?:\[[^\]]+\]\s*)?OR\s+RSZ\s+run(?:ning)?\s*time\s*:\s*({FLOAT})\s*sec(?:ond|onds)?\b",
    re.IGNORECASE,
)
FLOW_RUNTIME_RE = re.compile(
    rf"^\s*(?:\[[^\]]+\]\s*)?Flow\s+run(?:ning)?\s*time\s*:\s*({FLOAT})\s*sec(?:ond|onds)?\b",
    re.IGNORECASE,
)

# One line per GCell:
#   x y capacity usage congestion%
GR_LINE = re.compile(rf"^\s*(\d+)\s+(\d+)\s+({FLOAT})\s+({FLOAT})\s+({FLOAT})\s*$")

def _last_floats(line: str, n: int) -> Optional[Tuple[float, ...]]:
    nums = re.findall(FLOAT, line)
    if len(nums) < n:
        return None
    return tuple(float(x) for x in nums[-n:])

def parse_log(log_path: Path) -> Dict[str, Any]:
    m: Dict[str, Any] = {
        "design": None,
        "placement_legal": None,
        "total_insts": None,
        "wns": None,
        "tns": None,
        "slew_over_sum": 0.0,
        "slew_over_count": 0,
        "cap_over_sum": 0.0,
        "cap_over_count": 0,
        "fanout_over_sum": 0.0,
        "fanout_over_count": 0,
        "leakage_power": None,
        "total_power": None,
        "power_unit": None,
        "time_unit": None,
        "cap_unit": None,
        "max_gr_overflow": None,
        "total_gr_overflow": None,
        "legal_fail_summary": None,
        "tool_runtime": None,
        "flow_runtime": None,
    }

    # section state machine for violation tables
    section = None                 # None | "slew" | "cap" | "fanout"
    section_in_table = False

    # GR grid scan state (for your printed grid block)
    in_gr_scan = False
    gr_total_overflow_acc = 0.0
    gr_max_overflow_acc = 0.0

    # units/banner
    time_unit = None
    cap_unit = None
    pref_power_unit = None
    power_table_in_watts = False

    # legality
    placement_illegal_seen = False
    placement_legalized_seen = False

    # collect per-check legality failures
    legal_fails: Dict[str, Dict[str, Any]] = {}
    LEGAL_LINE = re.compile(r"\[(WARNING|ERROR)\s+(DPL-\d+)\]\s*(.*)")

    # power (as Watts from the table)
    power_total_w = None
    power_leak_w = None

    # optional: catch “max overflow:” and “max h/v overflow:”
    max_h_over = None
    max_v_over = None
    max_over   = None  # if the log prints a “max overflow:” line directly

    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            line = ANSI.sub("", raw).rstrip("\r\n")
            stripped = line.strip()

            # ---- GR grid scan block begin/end ----
            if stripped.startswith("Start Global Routing Results Analysis"):
                in_gr_scan = True
                gr_total_overflow_acc = 0.0
                gr_max_overflow_acc = 0.0
                continue
            if stripped.startswith("End Global Routing Results Analysis"):
                in_gr_scan = False
                # Save only if we actually saw any rows; also don't overwrite
                if m["total_gr_overflow"] is None:
                    m["total_gr_overflow"] = gr_total_overflow_acc
                if m["max_gr_overflow"] is None:
                    m["max_gr_overflow"] = gr_max_overflow_acc
                # fall through to parse remainder of the line, if any
            # Inside GR grid scan: parse "x y cap usage cong"
            if in_gr_scan:
                g = GR_LINE.match(stripped)
                if g:
                    _, _, cap_s, use_s, _ = g.groups()
                    cap = float(cap_s)
                    use = float(use_s)
                    overflow = use - cap
                    if overflow < 0:
                        overflow = 0.0
                    gr_total_overflow_acc += overflow
                    if overflow > gr_max_overflow_acc:
                        gr_max_overflow_acc = overflow
                continue  # don’t let these lines hit other parsers

            # ---- design name ----
            if m["design"] is None:
                m1 = re.search(r"^\s*design:\s*(\S+)", line, re.IGNORECASE)
                if m1:
                    m["design"] = m1.group(1)
                else:
                    m2 = re.search(r"^\[INFO ODB-0128\]\s*Design:\s*(\S+)", line)
                    if m2:
                        m["design"] = m2.group(1)

            # ---- total insts ----
            if m["total_insts"] is None:
                m3 = re.search(r"^\s*total_insts:\s*(\d+)", line, re.IGNORECASE)
                if m3:
                    m["total_insts"] = int(m3.group(1))

            # ---- unit banner ----
            if time_unit is None:
                mt = re.search(r"^\s*time\s+1([a-zA-Z]+)\s*$", line)
                if mt:
                    time_unit = mt.group(1)
                    m["time_unit"] = time_unit
            if cap_unit is None:
                mc = re.search(r"^\s*capacitance\s+1([a-zA-Z]+)\s*$", line)
                if mc:
                    cap_unit = mc.group(1)
                    m["cap_unit"] = cap_unit
            if pref_power_unit is None:
                mp = re.search(r"^\s*power\s+1([a-zA-Z]+)\s*$", line)
                if mp:
                    pref_power_unit = mp.group(1).lower()
                    m["power_unit"] = pref_power_unit

            # ---- WNS/TNS ----
            if m["tns"] is None:
                mtns = re.search(r"^\s*tns\s+max\s+({})\s*$".format(FLOAT), line, re.IGNORECASE)
                if mtns:
                    m["tns"] = float(mtns.group(1))
            if m["wns"] is None:
                mwns = re.search(r"^\s*wns\s+max\s+({})\s*$".format(FLOAT), line, re.IGNORECASE)
                if mwns:
                    m["wns"] = float(mwns.group(1))

            # ---- legality overall flags & runtime ----
            if "check_placement reported errors" in line or "Placement NOT legal" in line:
                placement_illegal_seen = True
            if ("Placement legalized." in line
                    or "Placement is legal; skip legalization." in line):
                placement_legalized_seen = True
            mrt = FLOW_RUNTIME_RE.search(line)
            trt = OR_RSZ_RUNTIME_RE.search(line)
            if mrt:
                try:
                    m["flow_runtime"] = float(mrt.group(1))
                except ValueError:
                    pass
            if trt:
                try:
                    m["tool_runtime"] = float(trt.group(1))
                except ValueError:
                    pass

            # ---- per-check legality details ----
            mleg = LEGAL_LINE.search(line)
            if mleg:
                severity, code, msg = mleg.groups()
                msg = msg.strip().rstrip(".")
                mcount = re.search(r"\((\d+)\)", msg)
                count_val = int(mcount.group(1)) if mcount else None
                short = re.sub(r"\(.*?\)", "", msg).strip().rstrip(".")
                if code not in legal_fails:
                    legal_fails[code] = {
                        "name": short,
                        "count": 0 if count_val is not None else None,
                        "severity": severity
                    }
                if count_val is not None:
                    if legal_fails[code]["count"] is None:
                        legal_fails[code]["count"] = 0
                    legal_fails[code]["count"] += count_val

            # ---- enter violation sections ----
            if re.search(r"^\s*max\s+slew\s*$", line, re.IGNORECASE):
                section = "slew"; section_in_table = False; continue
            if re.search(r"^\s*max\s+capacitance\s*$", line, re.IGNORECASE):
                section = "cap"; section_in_table = False; continue
            if re.search(r"^\s*max\s+fanout\s*$", line, re.IGNORECASE):
                section = "fanout"; section_in_table = False; continue

            # table header & end
            if section and (stripped.lower().startswith("pin ") or stripped.lower() == "pin"):
                section_in_table = True; continue
            if section and section_in_table and stripped == "":
                section = None; section_in_table = False; continue

            # table body rows
            if section and section_in_table:
                if "(VIOLATED)" in line:
                    last3 = _last_floats(line, 3)
                    if last3:
                        limit_val, value, _slack = last3
                        over = value - limit_val
                        if over > 0:
                            if section == "slew":
                                m["slew_over_sum"] += over
                                m["slew_over_count"] += 1
                            elif section == "cap":
                                m["cap_over_sum"] += over
                                m["cap_over_count"] += 1
                            elif section == "fanout":
                                m["fanout_over_sum"] += over
                                m["fanout_over_count"] += 1
                continue

            # ---- power table ----
            if "Power (Watts)" in line:
                power_table_in_watts = True
            if stripped.startswith("Total"):
                mtot = re.search(
                    r"^\s*Total\s+({})\s+({})\s+({})\s+({})\b".format(FLOAT, FLOAT, FLOAT, FLOAT),
                    line
                )
                if mtot:
                    _internal_w, _switching_w, leakage_w, total_w = [float(mtot.group(i)) for i in range(1, 5)]
                    power_total_w = total_w
                    power_leak_w = leakage_w

            # ---- congestion (other formats) ----
            mg1 = re.search(r"^\s*max_gr_overflow:\s*({})".format(FLOAT), line, re.IGNORECASE)
            if mg1 and m["max_gr_overflow"] is None:
                m["max_gr_overflow"] = float(mg1.group(1))
            mg2 = re.search(r"^\s*total_gr_overflow:\s*({})".format(FLOAT), line, re.IGNORECASE)
            if mg2 and m["total_gr_overflow"] is None:
                m["total_gr_overflow"] = float(mg2.group(1))
            # Generic “report_congestion” styles:
            if m["total_gr_overflow"] is None:
                mg3 = re.search(r"total\s+overflow\s*:\s*({})".format(FLOAT), line, re.IGNORECASE)
                if mg3:
                    m["total_gr_overflow"] = float(mg3.group(1))
            if max_over is None:
                mg4 = re.search(r"max\s+overflow\s*:\s*({})".format(FLOAT), line, re.IGNORECASE)
                if mg4:
                    max_over = float(mg4.group(1))
            if max_h_over is None:
                mgh = re.search(r"max\s*h[\.\s]*overflow\s*:\s*({})".format(FLOAT), line, re.IGNORECASE)
                if mgh:
                    max_h_over = float(mgh.group(1))
            if max_v_over is None:
                mgv = re.search(r"max\s*v[\.\s]*overflow\s*:\s*({})".format(FLOAT), line, re.IGNORECASE)
                if mgv:
                    max_v_over = float(mgv.group(1))

    # finalize legality overall flag
    if placement_legalized_seen:
        m["placement_legal"] = 1
    elif placement_illegal_seen:
        m["placement_legal"] = 0

    # finalize legality failure summary
    if legal_fails:
        parts = []
        for code in sorted(legal_fails.keys()):
            info = legal_fails[code]
            if info.get("count") is not None:
                parts.append(f"{code}: {info.get('name')}={info.get('count')}")
            else:
                parts.append(f"{code}: {info.get('name')}")
        m["legal_fail_summary"] = "; ".join(parts)

    # finalize max overflow if H/V or direct “max overflow” seen
    if m["max_gr_overflow"] is None:
        if max_over is not None:
            m["max_gr_overflow"] = max_over
        elif max_h_over is not None or max_v_over is not None:
            vals = [v for v in (max_h_over, max_v_over) if v is not None]
            if vals:
                m["max_gr_overflow"] = max(vals)

    # power unit conversion (Watts -> desired banner unit)
    if power_total_w is not None and power_leak_w is not None:
        unit_mult = 1.0
        unit_name = None
        if pref_power_unit:
            unit_name = pref_power_unit
            to_mult = {"w": 1.0, "mw": 1e3, "uw": 1e6, "nw": 1e9, "pw": 1e12, "fw": 1e15}
            unit_mult = to_mult.get(unit_name, 1.0)
        else:
            unit_name = "w"

        if power_table_in_watts:
            m["total_power"] = power_total_w * unit_mult
            m["leakage_power"] = power_leak_w * unit_mult
            m["power_unit"] = unit_name
        else:
            m["total_power"] = power_total_w
            m["leakage_power"] = power_leak_w
            if not m["power_unit"]:
                m["power_unit"] = "w"

    return m

def print_metrics(m: Dict[str, Any]) -> None:
    print("===== PARSED METRICS =====")
    def p(name, val, unit=None):
        if val is None:
            print(f"{name:24s}:")
        else:
            print(f"{name:24s}: {val} {unit or ''}".rstrip())

    p("design", m["design"])
    p("placement_legal", m["placement_legal"])
    p("total_insts", m["total_insts"])
    p("wns", m["wns"], m.get("time_unit"))
    p("tns", m["tns"], m.get("time_unit"))
    p("slew_over_sum", round(m["slew_over_sum"], 6), m.get("time_unit"))
    p("slew_over_count", m["slew_over_count"])
    p("cap_over_sum", round(m["cap_over_sum"], 6), m.get("cap_unit"))
    p("cap_over_count", m["cap_over_count"])
    p("fanout_over_sum", round(m["fanout_over_sum"], 6))
    p("fanout_over_count", m["fanout_over_count"])
    p("leakage_power", m["leakage_power"], m.get("power_unit"))
    p("total_power", m["total_power"], m.get("power_unit"))
    p("max_gr_overflow", m["max_gr_overflow"])
    p("total_gr_overflow", m["total_gr_overflow"])
    p("legal_fail_summary", m["legal_fail_summary"])
    p("tool_runtime", m["tool_runtime"], "seconds")
    p("flow_runtime", m["flow_runtime"], "seconds")
    print("==========================")

def append_csv(csv_path: Path, m: Dict[str, Any]) -> None:
    header = [
        "design","placement_legal","total_insts",
        "wns","tns","time_unit",
        "slew_over_sum","slew_over_count",
        "cap_over_sum","cap_over_count","cap_unit",
        "fanout_over_sum","fanout_over_count",
        "leakage_power","total_power","power_unit",
        "max_gr_overflow","total_gr_overflow",
        "legal_fail_summary",
        "tool_runtime",
        "flow_runtime",
    ]
    row = [
        m.get("design"),
        m.get("placement_legal"),
        m.get("total_insts"),
        m.get("wns"),
        m.get("tns"),
        m.get("time_unit"),
        m.get("slew_over_sum"),
        m.get("slew_over_count"),
        m.get("cap_over_sum"),
        m.get("cap_over_count"),
        m.get("cap_unit"),
        m.get("fanout_over_sum"),
        m.get("fanout_over_count"),
        m.get("leakage_power"),
        m.get("total_power"),
        m.get("power_unit"),
        m.get("max_gr_overflow"),
        m.get("total_gr_overflow"),
        m.get("legal_fail_summary"),
        m.get("tool_runtime"),
        m.get("flow_runtime"),
    ]
    new_file = not csv_path.exists()
    with csv_path.open("a", newline="") as fp:
        writer = csv.writer(fp)
        if new_file:
            writer.writerow(header)
        writer.writerow(row)

def main():
    ap = argparse.ArgumentParser(description="Parse OpenROAD log for metrics.")
    ap.add_argument("log", type=str, help="Path to OpenROAD log file")
    ap.add_argument("--csv", type=str, default=None, help="Append metrics to CSV file")
    args = ap.parse_args()

    log_path = Path(args.log)
    if not log_path.exists():
        print(f"ERROR: log file not found: {log_path}", file=sys.stderr)
        sys.exit(1)

    metrics = parse_log(log_path)
    print_metrics(metrics)

    if args.csv:
        append_csv(Path(args.csv), metrics)

if __name__ == "__main__":
    main()