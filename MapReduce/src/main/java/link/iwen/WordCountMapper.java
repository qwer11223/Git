package link.iwen;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 将 k1 和 v1 转换成 k2 和 v2 并写入上下文
public class WordCountMapper extends Mapper<LongWritable, Text, Text, LongWritable> {
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, LongWritable>.Context context)
            throws IOException, InterruptedException {
        Text text = new Text();
        LongWritable longWritable = new LongWritable();

        //1.将文本数据切分
        String[] split = value.toString().split(",");

        //2.遍历数组，组装 k2 和 v2
        for(String word:split){
            text.set(word);
            longWritable.set(1);
            context.write(text, longWritable);
        }
    }
}