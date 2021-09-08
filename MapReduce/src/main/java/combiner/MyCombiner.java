package combiner;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

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