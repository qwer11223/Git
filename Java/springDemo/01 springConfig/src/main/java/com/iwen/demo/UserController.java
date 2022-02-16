package com.iwen.demo;

import com.iwen.service.UserService;
import com.iwen.service.impl.UserServiceImpl;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class UserController {
    public static void main(String[] args) {
//        UserServiceImpl userService = new UserServiceImpl();
//        userService.save();

        ClassPathXmlApplicationContext app = new ClassPathXmlApplicationContext("applicationContext.xml");
        UserService userService = (UserService) app.getBean("userService");
        userService.save();
    }
}
