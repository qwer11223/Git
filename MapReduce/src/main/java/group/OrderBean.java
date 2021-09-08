package group;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;

public class OrderBean implements WritableComparable<OrderBean> {
    private String orderId;
    private Double price;
    

    public String getOrderId() {
        return orderId;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return orderId + "\t" + price;
    }

    @Override
    public void readFields(DataInput arg0) throws IOException {
        this.orderId = arg0.readUTF();
        this.price = arg0.readDouble();

    }

    @Override
    public void write(DataOutput arg0) throws IOException {
        arg0.writeUTF(orderId);
        arg0.writeDouble(price);
    }

    @Override
    public int compareTo(OrderBean o) {
        int id = this.orderId.compareTo(o.getOrderId());
        if (id == 0)
            id = this.price.compareTo(o.getPrice());
        return id * -1;
    }

    public OrderBean(String orderId, Double price) {
        this.orderId = orderId;
        this.price = price;
    }

    public OrderBean() {
    }

}