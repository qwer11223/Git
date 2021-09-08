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