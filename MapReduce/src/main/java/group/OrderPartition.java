package group;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

public class OrderPartition extends Partitioner<OrderBean, Text> {
    @Override
    public int getPartition(OrderBean arg0, Text arg1, int arg2) {
        return (arg0.getOrderId().hashCode() & 2147483647) % arg2;
    }
}