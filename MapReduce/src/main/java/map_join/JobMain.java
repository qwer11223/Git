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