package combiner;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class JobMain extends Configured implements Tool {

    // 该方法永远指定一个job任务
    @Override
    public int run(String[] arg0) throws Exception {
        // 1.创建一个job任务对象
        Job job = Job.getInstance(super.getConf(), "wrodcount");

        // 2.配置job任务对象(八个步骤)

        // 2.1 指定文件的读取方式和读取路径
        job.setInputFormatClass(TextInputFormat.class);
        TextInputFormat.addInputPath(job, new Path("src/main/java/combiner/data"));

        // 2.2 指定Map阶段的处理方式和数据类型
        job.setMapperClass(WordCountMapper.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(LongWritable.class);

        // 3(分区)、4(排序)

        //5.规约 （减少网络传输量）
        job.setCombinerClass(MyCombiner.class);

        //6(分组) 采用默认方式

        // 7. 指定Reduce阶段的处理方式和数据类型
        job.setReducerClass(WordCountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        // 8. 设置输出方式
        job.setOutputFormatClass(TextOutputFormat.class);
        // 8.1 设置输出路径
        TextOutputFormat.setOutputPath(job,
                new Path("src/main/java/combiner/data/output"));

        // 等待任务结束
        boolean bl = job.waitForCompletion(true);

        return bl ? 0 : 1;

    }

    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();

        // 启动Job任务
        int run = ToolRunner.run(configuration, new JobMain(), args);
        System.exit(run);
    }
}