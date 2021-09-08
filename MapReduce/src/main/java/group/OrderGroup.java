package group;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;

/*
    1: 继承 WriteableComparator
    2: 调用父类有参构造
    3: 指定分组规则（重写方法）
*/

// 1: 继承 WriteableComparator
public class OrderGroup extends WritableComparator {
    // 2: 调用父类有参构造
    public OrderGroup() {
        super(OrderBean.class, true);
    }

    // 3: 指定分组规则（重写方法）
    @SuppressWarnings("rawtypes")
    @Override
    public int compare(WritableComparable a, WritableComparable b) {
        OrderBean first = (OrderBean) a;
        OrderBean second = (OrderBean) b;
        return first.getOrderId().compareTo(second.getOrderId());
    }
}