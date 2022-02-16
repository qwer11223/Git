package com.iwen.controller;

import com.iwen.domain.User;
import com.iwen.domain.VO;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.List;

@Controller
public class MvcTest01 {
    //    08 获取cookie
    @RequestMapping(value = "/quick16")
    @ResponseBody
    public String save16(@CookieValue(value = "JSESSIONID",required = false) String js) {
        return js;
    }

    //    07 获取请求头
    @RequestMapping(value = "/quick15")
    @ResponseBody
    public String save15(@RequestHeader(value = "User-Agent",required = false) String userAgent) {
        return userAgent;
    }

    //    06 回写数据：Restful风格的参数 @PathVariable
    @RequestMapping(value = "/quick14/{name}")
    @ResponseBody
    public String save14(@PathVariable(value = "name",required = true) String username) {
        return username;
    }

    //    05 回写数据：直接回写字符串 @@RequestParam参数绑定
    @RequestMapping("/quick13")
    @ResponseBody
    public String save13(@RequestParam(value = "name", required = false, defaultValue = "anan") String username) {
        return username;
    }

    //    04-4-1 获得请求参数：json格式直接使用@RequestBody获得 集合 类型数据，无需封装VO
    @RequestMapping("/quick12")
    @ResponseBody
    public List<User> save12(@RequestBody List<User> userList) {
        return userList;
    }

    //    04-4 获得请求参数：获得 集合 类型数据
    @RequestMapping("/quick11")
    @ResponseBody
    public VO save11(VO vo) {
        System.out.println(vo);
        return vo;
    }

    //    04-3 获得请求参数：获得 数组 类型数据
    @RequestMapping("/quick10")
    @ResponseBody
    public List<String> save10(String[] strs) {
        return Arrays.asList(strs);
    }

    //    04-2 获得请求参数：获得POJO类型数据
    @RequestMapping("/quick9")
    @ResponseBody
    public User save9(User user) {
        return user;
    }

    //    04-1 获得请求参数：获得基本类型数据
    @RequestMapping("/quick8")
    @ResponseBody
    public String save8(String name, int age) {
        return name + "---" + age;
    }

    //    03-2 回写数据，返回对象或集合，配置spring-mvc返回json格式
    /*
        1.导入jackson maven依赖
        2.spring-mvc.xml中加入 <mvc:annotation-driven />
    */
    @RequestMapping("/quick7")
    @ResponseBody
    public User save7() {
        User user = new User();
        user.setName("jack");
        user.setAge(12345);

        return user;
    }

    //    03-1 回写数据：直接回写字符串
    @RequestMapping("/quick6")
    @ResponseBody
    public String save6() {
        return "success1.jsp";
    }

    //    02-4页面跳转，原生servlet方式
    @RequestMapping("/quick5")
    public String save5(HttpServletRequest httpServletRequest) {
        httpServletRequest.setAttribute("username", "servlet");
        return "success1.jsp";
    }

    //    02-3页面跳转，Model返回string
    @RequestMapping("/quick4")
    public String save4(Model model) {
        model.addAttribute("username", "ccc");
        return "success1.jsp";
    }

    //    02-2页面跳转，返回ModelAndView,自动注入modelAndView
    @RequestMapping("/quick3")
    public ModelAndView save3(ModelAndView modelAndView) {
//        设置模型数据
        modelAndView.addObject("username", "bbb");
//        设置视图名称
        modelAndView.setViewName("success1.jsp");

        return modelAndView;
    }

    //    02-1页面跳转，返回ModelAndView
    @RequestMapping("/quick2")
    public ModelAndView save2() {
        /*
            Model 模型： 作用 封装数据
            View 视图： 作用 展示数据
         */
        ModelAndView modelAndView = new ModelAndView();
//        设置模型数据
        modelAndView.addObject("username", "aaa");
//        设置视图名称
        modelAndView.setViewName("success1.jsp");

        return modelAndView;
    }

    //    01页面跳转，返回字符串形式
    @RequestMapping("/quick")
    public String save() {
        System.out.println("mvc...");
        return "success.jsp";
    }
}
