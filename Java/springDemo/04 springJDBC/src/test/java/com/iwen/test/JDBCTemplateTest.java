package com.iwen.test;

import com.alibaba.druid.pool.DruidDataSource;
import org.junit.Test;
import org.springframework.jdbc.core.JdbcTemplate;

public class JDBCTemplateTest {

    @Test
//    jdbc开发步骤
    public void test1(){
        //1创建数据源对象
        DruidDataSource druidDataSource = new DruidDataSource();
        druidDataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        druidDataSource.setUrl("jdbc:mysql://localhost:3306/ithtdb?serverTimezone=UTC");
        druidDataSource.setUsername("root");
        druidDataSource.setPassword("123456");

        JdbcTemplate jdbcTemplate = new JdbcTemplate();
        //2设置数据源对象
        jdbcTemplate.setDataSource(druidDataSource);
        //3执行操作
        int row = jdbcTemplate.update("insert into account values (?,?,?)", 2, "ss", "dsa231");
        System.out.println(row);
    }
}
