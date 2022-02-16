package com.iwen.web;

import com.iwen.config.SpringConfigration;
import com.iwen.service.UserService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class UserController {
    public static void main(String[] args) {
        ApplicationContext app = new AnnotationConfigApplicationContext(SpringConfigration.class);
        UserService bean = (UserService) app.getBean("userService");
        bean.save();
    }
}
