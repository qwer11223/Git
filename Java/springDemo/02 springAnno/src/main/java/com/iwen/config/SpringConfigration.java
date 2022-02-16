package com.iwen.config;

import com.alibaba.druid.pool.DruidDataSource;
import com.alibaba.druid.pool.DruidPooledConnection;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;

//标志该类是spring核心配置类
//用类代替文件，用注解代替标签
@Configuration

//<context:component-scan base-package="com.iwen" />
@ComponentScan("com.iwen")
@Import({DataSourceConfigration.class}) //导入DataSourceConfigration配置类
public class SpringConfigration {


}
