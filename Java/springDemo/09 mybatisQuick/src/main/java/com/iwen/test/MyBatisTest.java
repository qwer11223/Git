package com.iwen.test;

import com.iwen.domain.User;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class MyBatisTest {

    public static void main(String[] args) throws IOException {
//        加载核心配置文件
        InputStream resourceAsStream = Resources.getResourceAsStream("sqlMapConfig.xml");
//        获得sqlSession工厂对象
        SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
//        获得sqlSession对象
        SqlSession sqlSession = build.openSession();
//        执行sql
        List<User> userLists = sqlSession.selectList("userMapper.findAll");
//        打印结果
        System.out.println(userLists);
//        释放资源
        sqlSession.close();

    }
}
