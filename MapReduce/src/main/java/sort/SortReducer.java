package sort;

import java.io.IOException;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class SortReducer extends Reducer<SortBean,NullWritable,SortBean,NullWritable>{
    @Override
    protected void reduce(SortBean arg0, Iterable<NullWritable> arg1,
            Reducer<SortBean, NullWritable, SortBean, NullWritable>.Context arg2)
            throws IOException, InterruptedException {
        arg2.write(arg0, NullWritable.get());
    }
}