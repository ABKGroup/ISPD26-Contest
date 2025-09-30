export TOP_PROJ_DIR="/ISPD26-Contest"
export PROJ_DIR="${TOP_PROJ_DIR}/scripts"

export DESIGN_NAME="aes_cipher_top"
export FOLDER_NAME="TCP_250_UTIL_0.40"


mkdir ${FOLDER_NAME} -p
export LOG_FILE="${FOLDER_NAME}/evaluation.log"
export METRICS_CSV="${FOLDER_NAME}/metrics.csv"
export CONGESTION_REPORT="${FOLDER_NAME}/congestion_report.rpt"

/OpenROAD/build/bin/openroad -exit ${PROJ_DIR}/evaluation.tcl | tee ./${LOG_FILE}

# output metrics to csv
python3 ${PROJ_DIR}/parse_log.py ./${LOG_FILE} --csv ./${METRICS_CSV}



