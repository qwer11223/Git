package com.iwen.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class TargetController {

    @RequestMapping("/target")
    public ModelAndView show(){
        System.out.println("目标代码执行...");
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("name","itht");
        modelAndView.setViewName("index.jsp");
        return modelAndView;
    }
}
