package group;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class GroupMapper extends Mapper<LongWritable, Text, OrderBean, Text> {
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, OrderBean, Text>.Context context)
            throws IOException, InterruptedException {
        String[] split = value.toString().split("\t");

        context.write(new OrderBean(split[0], Double.valueOf(split[2])), value);
    }
}