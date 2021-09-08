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