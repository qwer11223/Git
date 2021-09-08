package hdfs_api;

import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;

public class GetFileSystem {

    public void getFileSystem1() throws Exception {
        Configuration configuration = new Configuration();
        // 1.设置文件系统类型及路径
        configuration.set("fs.defaultFS", "hdfs://  or  file://");

        // 2.获取指定的文件系统
        FileSystem fileSystem = FileSystem.get(configuration);
        System.out.println(fileSystem.toString());
    }

    public void GetFileSystem2() throws Exception{
        //URI获取fileSystem
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://"), new Configuration());
        System.out.println(fileSystem.toString());
    }
}
