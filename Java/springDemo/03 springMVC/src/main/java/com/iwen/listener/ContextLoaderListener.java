package com.iwen.listener;

import com.iwen.dao.UserDao;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import javax.servlet.ServletContext;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

public class ContextLoaderListener implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce) {
//        获取全局上下文
        ServletContext servletContext = sce.getServletContext();
//        读取web.xml中的全局参数
        String contextConfigration = servletContext.getInitParameter("contextConfigration");
//        读取spring配置文件
        ClassPathXmlApplicationContext app = new ClassPathXmlApplicationContext(contextConfigration);
        servletContext.setAttribute("app", app);
        System.out.println("spring container init success...");
    }
}
