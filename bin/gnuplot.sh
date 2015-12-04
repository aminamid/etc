export GDFONTPATH=${TOOL_ROOT}/etc
export GNUPLOT_DEFAULT_GDFONT=DejaVuSans
gnuplot -e "filename='""${TOOL_ROOT}/etc/""gnuplot.dat'" ${TOOL_ROOT}/etc/gnuplot.plg
python -m SimpleHTTPServer
