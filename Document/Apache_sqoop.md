# 一. sqoop 安装

1. 解压文件到指定目录

   ```shell
   tar -zxvf sqoop-1.4.6.bin__hadoop-2.0.4-alpha.tar.gz -C /opt/
   ```

   

2. 配置环境变量

    ```shell
    vim /etc/profile

    export SQOOP_HOME=/opt/sqoop-1.4.6.bin/
    export PATH=$PATH:$SQOOP_HOME/bin

    source /etc/profile #生效文件

    sqoop version #验证
    ```



3. 修改配置文件

   ```shell
   cd /opt/sqoop-1.4.6.bin/conf
   mv sqoop-env-template.sh sqoop-env.sh
   
   #配置hadoop的安装目录
   export HADOOP_COMMON_HOME=/opt/hadoop-3.2.1/
   
   #配置的hadoop的mr的安装目录
   export HADOOP_MAPRED_HOME=/opt/hadoop-3.2.1/
   
   #set the path to where bin/hbase is available
   #export HBASE_HOME=
   
   #配置hive的安装目录
   export HIVE_HOME=/opt/apache-hive-3.1.2-bin/
   
   #设置 zookeeper的配置文件目录
   export ZOOCFGDIR=
   
   5）复制mysql的驱动包 放在sqoop的安装目录的lib下
   cp /opt/apache-hive-3.1.2-bin/lib/mysql-connector-java-8.0.25.jar /opt/sqoop-1.4.6.bin/lib/
   ```
   
4. 连接测试

   ```shell
   sqoop list-databases \
   --connect jdbc:mysql://localhost:3306 \
   --username root --password 123456
   ```




# 二. sqoop 导入

## 1. 全量导入mysql表数据到HDFS

```shell
sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--delete-target-dir \	#如果目录存在先删除
--target-dir /sqoopresult \
--table table_name \	#指定表明
[--fields-terminated-by '\t']  #指定分隔符，默认为','
[--split-by id] \  #-m大于2时，需指定分割字段
-m 1	#mapreduce个数
```



## 2. 全量导入mysql表数据到HIVE

### 方式一：先复制表结构到hive中再导入数据

```shell
# 1.将关系型数据库的表结构复制到hive中

sqoop create-hive-table \
--connect jdbc:mysql://node03:3306/userdb \	#userdb:链接数据库时，使用的数据库
--table table_name \	#mysql中的表名
--username root \
--password 123456 \
--hive-table test.table_name #test:hive中的数据库；table_name:导入数据的表名

# 2.从数据库导入文件到hive中
sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
--hive-table test.table_name \
--hive-import \	#执行hive数据导入
-m 1
```



### 方式二：直接复制表结构数据到hive中

```shell
sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
--hive-import \
-m 1 \
--hive-database test;  #没有指定表名，导入后的表名和mysql中一样
```



## 3. 导入表数据子集(where过滤)

```shell
sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--where "city='aa'" \	#指定从数据库导入时的查询条件
--target-dir /wherequery \
--table table_name \
-m 1
```



## 4. 导入表数据子集(query查询)

```shell
#注意事项：
#1.使用query sql语句时不能加参数--table；
#2.必须添加where条件(导入全部数据时可使用 where 1=1)；
#3.where条件后必须带一个$CONDITIONS这个字符串；
#4.sql语句必须使用单引号；

sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--target-dir /wherequery1 \
--query 'select * from table_name where id>12 and $CONDITIONS' \	#sql语句
--fields-terminated-by '\t' \
--split-by id \	#配合-m使用
-m 2 #默认1
```



## 5. 增量导入

```shell
--check-column (col) #指定一些列来检查是否作为增量数据进行导入，可指定多个列，不能使用字符等类型，如char、vchar等；

--incremental (mode)
	#|_ append:追加，比如对大于 last-value 指定的值之后的纪录进行追加导入
	#|_ lastmodified:最后修改时间，追加 last-value指定日期之后的纪录
		#|_ --append:lastmodified追加模式（！！注意：append模式匹配 >= 的数据）
		#|_ --merge-key id：lastmodified合并模式（会把增量数据合并到一个文件中）

--last-value (value) #指定自从上次导入后列的最大值
```

---

### append模式增量导入

```shell
sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
-m 1 \
--target-dir /sqoopresult \
--incremental append \
--check-column id \
--last-value 123
```

### lastmodified模式增量导入

```shell
#创建mysql时间戳表
#create table name(id int,name vchar(20),last_mod timestamp default current_timestamp on update current_timestamp);

sqoop import \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
-m 1 \
--target-dir /sqoopresult \
--incremental lastmodified \
--check-column last_mod \
--last-value "2021-10-02 22:38:12" \
--append #lastmodified追加模式（！！注意：append模式匹配 >= 的数据,可能存在两个相同数据；解决：修改值）
```



# 三. sqoop导出

数据导出前，==目标表必须存在于目标数据库中==

export 有三种模式：

1. 默认将文件中的每行数据使用 insert 语句插入表中
2. 更新模式：sqoop 将生成 update 替换数据库中现有记录的语句
3. 调用模式：sqoop 将为每条记录创建一个存储过程调用



## 默认模式导出数据到mysql

```shell
sqoop export \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
--export-dir /hdfs|hive_path  #需要导出数据的路径hdfs或hive

#相关配置参数
--input-fields-terminated-by '\t' #指定导出文件中的分隔符（默认为','）
--columns id,name,deg  #当表文件与数据库中列顺序不一致时，指定字段
--input-null-string "\\N" --input-null-non-string "\\N"
```



## 更新导出

```shell
#参数说明
--update-key #根据哪个字段进行更新，如id,或多个字段用','分隔
--updatemod 
	#|_ updateonly(默认模式)，只会更新已存在的数据，不会执行insert增加新数据
	#|_ allowinsert模式，更新已存在的纪录，同时插入新纪录，实际上是一个 insert&update 的操作
```




### (updateonly模式)

```shell
sqoop export \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
--export-dir /hdfs|hive_path \
--update-key id \
--updatemod updateonly
```

### (allowinsert模式)

```shell
sqoop export \
--connect jdbc:mysql://node03:3306/userdb \
--username root \
--password 123456 \
--table table_name \
--export-dir /hdfs|hive_path \
--update-key id \
--updatemod allowinsert
```