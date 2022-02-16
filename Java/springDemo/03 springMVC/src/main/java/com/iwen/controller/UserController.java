package com.iwen.controller;

import com.iwen.dao.UserDao;
import com.iwen.service.UserService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.support.WebApplicationContextUtils;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class UserController extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        ServletContext servletContext = this.getServletContext();

//        Object app = servletContext.getAttribute("app");
//        使用自定义监听器
//        ApplicationContext app = WebApplicationContextUtils.getWebApplicationContext(servletContext);

//        使用spring-web
        WebApplicationContext app = WebApplicationContextUtils.getWebApplicationContext(servletContext);

        UserService userService = (UserService) app.getBean("userService");
        userService.save();
    }
}
