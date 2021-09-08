package sort;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;

import org.apache.hadoop.io.WritableComparable;

public class SortBean implements WritableComparable<SortBean> {
    private String word;
    private int num;

    // 实现反序列化
    @Override
    public void readFields(DataInput arg0) throws IOException {
        this.word = arg0.readUTF();
        this.num = arg0.readInt();
    }

    // 实现序列化
    @Override
    public void write(DataOutput arg0) throws IOException {
        arg0.writeUTF(word);
        arg0.writeInt(num);
    }

    // 实现比较器，指定排序规则
    @Override
    public int compareTo(SortBean o) {
        int res = this.word.compareTo(o.word);
        if (res == 0) {
            return this.num - o.num;
        }
        return res;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    @Override
    public String toString() {
        return word + "\t" + num;
    }

}