#!/bin/bash

docker exec -it namenode sh -c "/usr/local/spark/sbin/start-master.sh"
docker exec -it datanode1 sh -c "/usr/local/spark/sbin/start-worker.sh spark://namenode:7077"
docker exec -it datanode2 sh -c "/usr/local/spark/sbin/start-worker.sh spark://namenode:7077"
docker exec -it datanode3 sh -c "/usr/local/spark/sbin/start-worker.sh spark://namenode:7077"
