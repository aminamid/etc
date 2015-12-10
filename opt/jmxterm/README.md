echo "beans -d org.apache.cassandra.metrics" | ./jmxterm | grep -i tbl_chglog | sort | sed -e "s/,/ /g" | grep -i hist | column -t
