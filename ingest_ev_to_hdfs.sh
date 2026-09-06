#!/bin/bash
hdfs dfsadmin -safemode leave
hdfs dfs -mkdir -p /user/ev/raw
hdfs dfs -put -f /cpcb_data/ev_charging.csv /user/ev/raw/
hdfs dfs -ls -h /user/ev/raw
