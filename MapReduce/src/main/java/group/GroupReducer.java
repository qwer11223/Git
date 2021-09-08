package group;

import java.io.IOException;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class GroupReducer extends Reducer<OrderBean, Text, Text, NullWritable> {
    @Override
    protected void reduce(OrderBean arg0, Iterable<Text> arg1,
            Reducer<OrderBean, Text, Text, NullWritable>.Context arg2) throws IOException, InterruptedException {
        int i = 0;
        for (Text t : arg1) {
            arg2.write(t, NullWritable.get());
            i++;
            if (i >= 1)
                break;
        }
    }
}