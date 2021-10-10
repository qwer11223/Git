# HBase 安装

1. 解压文件

   ```shell
   tar -zxvf hbase-2.3.6-bin.tar.gz -C /opt/
   ```

2. 配置 hbase-env.sh

   ```shell
   vim /opt/hbase-2.3.6/conf/hbase-env.sh
   
   #添加以下内容
   export JAVA_HOME=/opt/jdk-11.0.1/
   export HBASE_MANAGES_ZK=false	#关闭自带zookeeper
   
   
   # JDK8记得移除下面几个配置项
   # Configure PermSize. Only needed in JDK7. You can safely remove it for JDK8+
   # export HBASE_MASTER_OPTS="$HBASE_MASTER_OPTS -XX:PermSize=128m -XX:MaxPermSize=128m -XX:ReservedCodeCacheSize=256m"
   # export HBASE_REGIONSERVER_OPTS="$HBASE_REGIONSERVER_OPTS -XX:PermSize=128m -XX:MaxPermSize=128m -XX:ReservedCodeCacheSize=256m"
   ```

3. 配置 hbase-site.xml

   ```shell
   vim /opt/hbase-2.3.6/conf/hbase-site.xml
   
   #清空所有配置，添加以下内容
   <configuration>
     
   <!--指定HBase在HDFS上的数据存储目录-->
     <property>
       <name>hbase.rootdir</name>
       <value>hdfs://node01:9000/hbase</value>
     </property>
     
   <!--配置Zookeeper的连接地址-->
     <property>
       <name>hbase.zookeeper.quorum</name>
       <value>node01:2181,node02:2181,node03:2181</value>
       <description>The directory shared by RegionServers. </description>
     </property>
   
   <!--开启HBase的分布式,false表示单机运行-->
     <property>
       <name>hbase.cluster.distributed</name>
       <value>true</value>
     </property>
     
   <!--配置HBase访问端口-->
     <property>
       <name>hbase.master.info.port</name>
       <value>16010</value>
     </property>
     
     <property>
       <name>hbase.unsafe.stream.capability.enforce</name>
       <value>false</value>
     </property>
     
     <property>
       <name>hbase.wal.provider</name>
       <value>filesystem</value>
     </property>
   
   </configuration>
   ```

4. 配置 regionservers

   ```shell
   #添加当前三台主机的主机名
   node01
   node02
   node03
   ```

5. 需要将Hadoop的核心配置文件拷贝到当前的HBase的配置目录

   ```shell
   cp /opt/hadoop-3.2.1/etc/hadoop/core-site.xml ./
   ```

6. 将HBase远程拷贝给另外两台主机

   ```sehll
   scp -r  /opt/hbase-2.3.6/ node02:/opt
   scp -r  /opt/hbase-2.3.6/ node03:/opt
   ```

7. 配置三台主机的HBase环境变量

   ```shell
   vim /etc/profile
   
   export HBASE_HOME=/opt/hbase-2.3.6/
   export PATH=$PATH:$HBASE_HOME/bin
   
   source /etc/profile
   ```

8. 启动hbase

   ```shell
   #！需要先启动zookeeper、hdfs
   
   #在第一台主机上启动hbase
   start-hbase.sh
   ```

   