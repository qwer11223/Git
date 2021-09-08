package hdfs_api;

import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class Cat {

    public static void main(String[] args) throws IOException, URISyntaxException {
        FileSystem fileSystem = FileSystem.get(new URI("hdfs://192.168.60.100:9000"), new Configuration());

        FSDataInputStream inputStream = fileSystem.open(new Path("/cache_file/product.txt"));
        FileOutputStream outputStream = new FileOutputStream("src/main/java/hdfs_api/product.txt");

        IOUtils.copy(inputStream, outputStream);

        IOUtils.closeQuietly(inputStream);
        IOUtils.closeQuietly(outputStream);
        fileSystem.close();

    }
}