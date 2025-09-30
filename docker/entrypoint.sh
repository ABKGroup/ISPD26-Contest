#!/bin/bash

source /opt/miniconda3/etc/profile.d/conda.sh

if [ ! -f "/opt/installed" ]; then
  echo Preparing to start for the first time...
  cd /OpenROAD/build
  make -j install 1> /dev/null
  cd /
  
  touch /opt/installed
  echo "Done."
  echo

fi


export PATH="/opt/oss-cad-suite/bin":$PATH
export YOSYS_EXE=/opt/oss-cad-suite/bin/yosys
export OPENROAD_EXE=/OpenROAD/build/src/openroad

cat /etc/motd

bash -i <<< "source /opt/miniconda3/etc/profile.d/conda.sh && conda activate base && echo 'Ready.'; exec </dev/tty"