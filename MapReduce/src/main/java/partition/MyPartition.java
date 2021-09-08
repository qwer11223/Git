package partition;

import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

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