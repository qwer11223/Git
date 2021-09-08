# 集群linux环境搭建

## linux配置ip地址
`/etc/sysconfig/network-scripts/ifvfg-ens33`
> BOOTPROTO=static  
>
> IPADDR=192.168.60.100  
> GATEWAY=192.168.60.2  
> NETMASK=255.255.255.0  
> DNS1=114.114.114.114  
> DNS2=223.5.5.5

## 配置主机名和域名映射

* 修改主机名  
`vi /etc/sysconfig/network`  
> NETWORKING=yes  
HOSTNAME=node01

* 设置ip和域名映射  
`vi /etc/hosts`
> 192.168.60.100 node01 node01.hadoop.com  
192.168.60.110 node02 node02.hadoop.com  
192.168.60.120 node03 node03.hadoop.com

## 关闭防火墙和SELinux

* 关闭防火墙
```
service iptables stop #关闭防火墙
chkconfig iptables off #禁止开机启动
```

* 关闭selinux

SELinux是linux的一种安全子系统，linux中的权限管理是针对文件的，SELinux在Linux的文件权限之外，增加了对进程的限制，进程只能在进程允许的范围内操作资源。

> selinux 工作模式  
* `enforcing` 强制模式
* `permissive` 宽容模式
* `disable` 关闭

```
#修改selinux配置文件
vi /etc/selinux/config
```


## SSH免密登陆

Secure Shell (安全外壳协议)

1. 生成公私钥对

> `ssh-keygen -t rsa ` # -t表示类型选择，采用rsa算法

2. 将公钥拷贝到远程主机
> `ssh-copy-id node01`

3. 复制node01的认证到其他节点
> `scp /root/.ssh/authorized_keys node02:/root/.ssh`

## 时钟同步

1. 所有主机和同一台主机时间保持同步
2. 通过网络，所有主机时钟与服务器保持同步
> #安装  
> yum install ntp  
>
> #启动定时任务  
> crontab -e
> 
> #在输入界面键入
> */1 * * * * /usr/sbin/ntpdate ntp4.aliyun.com;

## 安装JAVA

1. 上传 jdk-11.0.1_linux-x64_bin.tar.gz

2.  `tar -xvf  jdk-11.0.1_linux-x64_bin.tar.gz -C /opt` 解压文件到 /opt 目录
3. 配置环境变量

```shell
# /etc/profile

#添加
export JAVA_HOME=/opt/jdk-11.0.1
export PATH=:$JAVA_HOME/bin:$PATH
```





# Zookeeper 环境搭建

1. 上传zookeeper并解压
2. 修改配置文件

```shell
# 1.
cd /opt/zookeeper-3.2.1/conf/

# 2.
cp zoo_sample.cfg zoo.cfg
#添加
server.1=node01:2888:3888
server.2=node02:2888:3888
server.3=node03:2888:3888

# 3.
mkdir /opt/zookeeper-3.2.1/zkdatas
```

3.  添加myid配置

`echo 1 > /opt/zookeeper-3.2.1/zkdatas/myid`

4. 安装包分发并修改myid值
5.  zookeeper/bin/zkServer.sh start 启动zookeeper



# Hadoop 环境搭建

https://blog.csdn.net/qq_41515513/article/details/101873098



# Hive 环境搭建

https://blog.csdn.net/weixin_43861175/article/details/90372513



# MapReduce

![image-20210908162609948](C:\Users\Lenovo\Desktop\Git\Document\hadoop.assets\image-20210908162609948.png)

![image-20210908162847013](C:\Users\Lenovo\Desktop\Git\Document\hadoop.assets\image-20210908162847013.png)

![image-20210908162805749](C:\Users\Lenovo\Desktop\Git\Document\hadoop.assets\image-20210908162805749.png)

![image-20210908162931831](C:\Users\Lenovo\Desktop\Git\Document\hadoop.assets\image-20210908162931831.png)

![image-20210908162949893](C:\Users\Lenovo\Desktop\Git\Document\hadoop.assets\image-20210908162949893.png)



## 分区

1.    ` job.setPartitionerClass(MyPartition.class);`

2.  ```java
   public class MyPartition extends Partitioner<Text, NullWritable> {
       /*
        * 1. 定义分区规则 2. 返回对应分区编号
        */
       @Override
       public int getPartition(Text arg0, NullWritable arg1, int arg2) {
           // 1.拆分文本数据 k2
           String[] split = arg0.toString().split("\t");
           String numStr = split[1];
   
           // 2. 判断关系，返回分区编号
           if(Integer.parseInt(numStr) > 30)
               return 1;
           else
               return 0;
       }
   }
   ```

3. ​    `job.setNumReduceTasks(2);`



## 排序

```java
public class SortBean implements WritableComparable<SortBean> {
    private String word;
    private int num;

    // 实现反序列化
    @Override
    public void readFields(DataInput arg0) throws IOException {
        this.word = arg0.readUTF();
        this.num = arg0.readInt();
    }

    // 实现序列化
    @Override
    public void write(DataOutput arg0) throws IOException {
        arg0.writeUTF(word);
        arg0.writeInt(num);
    }

    // 实现比较器，指定排序规则
    @Override
    public int compareTo(SortBean o) {
        int res = this.word.compareTo(o.word);
        if (res == 0) {
            return this.num - o.num;
        }
        return res;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    @Override
    public String toString() {
        return word + "\t" + num;
    }

}
```





## 规约

1. `    job.setCombinerClass(MyCombiner.class);`

2. ```java
   public class MyCombiner extends Reducer<Text, LongWritable, Text, LongWritable> {
       @Override
       protected void reduce(Text key, Iterable<LongWritable> values,
               Reducer<Text, LongWritable, Text, LongWritable>.Context context) throws IOException, InterruptedException {
           long count = 0;
           // 1.遍历集合，将集合中数字相加得到 v3
           for (LongWritable value : values) {
               count += value.get();
           }
   
           // 2.将 k3 和 v3 写入上下文中
           context.write(key, new LongWritable(count));
   
       }
   }
   ```



## 分组

1. `    job.setGroupingComparatorClass(OrderGroup.class);`

2. ```java
   /*
       1: 继承 WriteableComparator
       2: 调用父类有参构造
       3: 指定分组规则（重写方法）
   */
   
   // 1: 继承 WriteableComparator
   public class OrderGroup extends WritableComparator {
       // 2: 调用父类有参构造
       public OrderGroup() {
           super(OrderBean.class, true);
       }
   
       // 3: 指定分组规则（重写方法）
       @SuppressWarnings("rawtypes")
       @Override
       public int compare(WritableComparable a, WritableComparable b) {
           OrderBean first = (OrderBean) a;
           OrderBean second = (OrderBean) b;
           return first.getOrderId().compareTo(second.getOrderId());
       }
   }
   ```



## OutputFormat

1. `job.setOutputFormatClass(MyOutputFormat.class);`

2. ```java
   public class MyOutputFormat extends FileOutputFormat<Text, IntWritable> {
       @Override
       public RecordWriter<Text, IntWritable> getRecordWriter(TaskAttemptContext arg0)
               throws IOException, InterruptedException {
   
           // 1.使用配置对象获取输出流
           FileSystem fileSystem = FileSystem.get(arg0.getConfiguration());
           FSDataOutputStream firstOutputStreaam = fileSystem
                   .create(new Path("demo/src/main/java/a2020_finals/data/output/weixiuhuanjian.csv"));
           FSDataOutputStream secondOutputStreaam = fileSystem
                   .create(new Path("demo/src/main/java/a2020_finals/data/output/chongfudata.csv"));
   
           // 2.将输出流传递给RecordWrite
           MyRecordWriter myRecordWriter = new MyRecordWriter(firstOutputStreaam, secondOutputStreaam);
   
           return myRecordWriter;
       }
   }
   
   //-------------------------------------------------------------------//
   
   
   public class MyRecordWriter extends RecordWriter<Text, IntWritable> {
   
       private FSDataOutputStream firstOutputStreaam;
       private FSDataOutputStream secondOutputStreaam;
   
       @Override
       public void close(TaskAttemptContext arg0) throws IOException, InterruptedException {
           firstOutputStreaam.close();
           secondOutputStreaam.close();
   
       }
   
       @Override
       public void write(Text arg0, IntWritable arg1) throws IOException, InterruptedException {
           // 1: 获取 value
           // 2：根据value写入不同文件
   
           if (arg1.get() == 0) {
               firstOutputStreaam.write(arg0.toString().getBytes());
               firstOutputStreaam.write("\r\n".getBytes());
           } else {
               secondOutputStreaam.write(arg0.toString().getBytes());
               secondOutputStreaam.write("\r\n".getBytes());
           }
   
       }
   
       public MyRecordWriter(FSDataOutputStream firstOutputStreaam, FSDataOutputStream secondOutputStreaam) {
           this.firstOutputStreaam = firstOutputStreaam;
           this.secondOutputStreaam = secondOutputStreaam;
       }
   
       public MyRecordWriter() {
       }
   
   }
   ```



## counter

```java
public class DataReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    // --- 定义计数器
    public static enum Counter {
        FIX_COUNT, DUPLICATE_COUNT
    }

    @Override
    protected void reduce(Text arg0, Iterable<IntWritable> arg1,
            Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {

        // 1.获取键对应值数量
        int count = 0;
        Iterator<IntWritable> iterator = arg1.iterator();
        while (iterator.hasNext()) {
            iterator.next();
            count++;
        }

        // 2. 区分数据：0 唯一数据 ， 1 重复数据
        if (count == 1) {
            // 设置计数器
            arg2.getCounter(Counter.FIX_COUNT).increment(1L);

            arg2.write(arg0, new IntWritable(0));
        } else {
            for (int j = 0; j < count; j++) {
                if (j == 0) {
                    // 设置计数器
                    arg2.getCounter(Counter.FIX_COUNT).increment(1L);
                    arg2.write(arg0, new IntWritable(0));
                } else {
                    // 设置计数器
                    arg2.getCounter(Counter.DUPLICATE_COUNT).increment(1L);
                    arg2.write(arg0, new IntWritable(1));
                }

            }
        }
    }
}
```





## Map-Join

JobMian.java

```java
package map_join;

import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class JobMain extends Configured implements Tool {
    @Override
    public int run(String[] arg0) throws Exception {
        // 1.获取job对象
        Job job = Job.getInstance(super.getConf(), "map_join_job");

        // 2.设置job对象(将小表放在分布式缓存中)
        job.addCacheFile(new URI("hdfs://192.168.60.100:9000/cache_file/product.txt"));

        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("src/main/java/map_join/data"));

        job.setMapperClass(MapJoinMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        // 第八步：设置输出
        job.setOutputFormatClass(TextOutputFormat.class);
        TextOutputFormat.setOutputPath(job, new Path("src/main/java/map_join/data/output"));

        // 3.等待任务结束
        boolean waitForCompletion = job.waitForCompletion(true);

        return waitForCompletion ? 0 : 1;
    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();

        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }

}
```

MapJoinMapper.java

```java
package map_join;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;

import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapJoinMapper extends Mapper<LongWritable, Text, Text, Text> {
    private HashMap<String, String> map = new HashMap<String, String>();

    // 1.将分布式缓存的小表数据读取到本地map集合(只需执行一次)

    @Override
    protected void setup(Mapper<LongWritable, Text, Text, Text>.Context context)
            throws IOException, InterruptedException {
        // 1. 获取分布式缓存列表
        URI[] cacheFiles = context.getCacheFiles();

        // 2.获取指定的分布式缓存文件的文件系统(FileSystem)
        FileSystem fileSystem = FileSystem.get(cacheFiles[0], context.getConfiguration());

        // 3.获取文件的输入流
        FSDataInputStream inputStream = fileSystem.open(new Path(cacheFiles[0]));

        // 4.读取文件内容，将数据存入map集合
        // 4.1 字节流转为字符缓冲流
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

        // 4.2 读取小表文件内容，以行为单位，并存入map

        String line = null;
        while ((line = bufferedReader.readLine()) != null) {
            String[] split = line.split(",");
            map.put(split[0], line);
        }

        // 5.关闭流
        bufferedReader.close();
        fileSystem.close();
    }

    // 2.对大表的处理业务逻辑，并且实现大表的小表的join操作
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
            throws IOException, InterruptedException {
        // 1.从行文本数据中获取商品id
        String[] split = value.toString().split(",");
        String productId = split[2];

        // 2.在map集合中，将商品id作为键，获取值，和value拼接，得到k2
        String productLine = map.get(productId);
        String valueLine = productLine + '\t' + value.toString();

        // 3.写入上下文
        context.write(new Text(productId), new Text(valueLine));
    }

}
```





## Reduce-Join

mapper

```java
package reduce_join;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.Mapper;

public class ReduceJoinMapper extends Mapper<LongWritable, Text, Text, Text> {
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
            throws IOException, InterruptedException {
        // 1. 判断数据来自哪个文件
        FileSplit fileSplit = (FileSplit) context.getInputSplit();
        String fileName = fileSplit.getPath().getName();
        if (fileName.equals("products.txt")) {
            // 数据来自商品表
            // 转为 k2 v2 ，写入上下文
            String[] split = value.toString().split(",");
            String productId = split[0];

            context.write(new Text(productId), value);
        } else {
            // 数据来自订单表
            // 转为 k2 v2 ，写入上下文

            String[] split = value.toString().split(",");
            String productId = split[2];

            context.write(new Text(productId), value);
        }

    }
}
```

 reduce

```java
package reduce_join;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ReduceJoinReducer extends Reducer<Text, Text, Text, Text> {
    @Override
    protected void reduce(Text arg0, Iterable<Text> arg1, Reducer<Text, Text, Text, Text>.Context arg2)
            throws IOException, InterruptedException {
        // 1.遍历集合，获取v3 (first + second)
        String first = "";
        String second = "";
        for (Text value : arg1) {
            if (value.toString().startsWith("p")) {
                first = value.toString();
            } else {
                second = value.toString();
            }
        }

        // 2.k3 v3 写入上下文
        arg2.write(arg0, new Text(first + "\t" + second));
    }

}
```



# SQL执行顺序

1. from 
2. join 
3. on 
4. where 
5. group by(开始使用select中的别名，后面的语句中都可以使用)
6.  avg,sum.... 
7. having 
8. select 
9. distinct 
10. order by
11. limit 