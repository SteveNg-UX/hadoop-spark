FROM debian:buster

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
RUN apt-get update -y && apt-get upgrade -y && \
	apt-get install -y default-jdk && \
	apt-get install -y openssh-client openssh-server && \
	apt-get install -y python3 python3-pip && \
	apt-get install -y wget && \
	wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && \
	tar -xzf hadoop-3.3.6.tar.gz && \
	mv hadoop-3.3.6 /usr/local/hadoop && \
	rm hadoop-3.3.6.tar.gz
ADD config/* $HADOOP_CONF_DIR/
RUN mkdir -p /usr/local/hadoop/hadoop_data/hdfs/namenode && \
	mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode && \
	hdfs namenode -format -force && \
	wget https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz && \
	tar -xzf spark-3.5.1-bin-hadoop3.tgz && \
	mv spark-3.5.1-bin-hadoop3 /usr/local/spark && \
	rm spark-3.5.1-bin-hadoop3.tgz && \
	echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh
ADD config/spark/* $SPARK_HOME/conf/
RUN mkdir /var/run/sshd && \
	echo 'root:root' | chpasswd && \
	sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
	chmod 0600 ~/.ssh/authorized_keys && \
	for container in ${CONTAINER_NAMES}; do ssh-keyscan -H $container >> ~/.ssh/known_hosts; done
USER root
RUN service ssh start
EXPOSE 22 9000 8042 8041 8040 8088 8042 4040 8888 8080 19888 7077
