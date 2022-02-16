package com.iwen.dao.impl;

import com.iwen.dao.UserDao;

import java.util.List;
import java.util.Map;
import java.util.Properties;

public class UserDaoImpl implements UserDao {
    private List<String> strList;
    private Map<String,User> userMap;
    private Properties props;

    public void setStrList(List<String> strList) {
        this.strList = strList;
    }

    public void setUserMap(Map<String, User> userMap) {
        this.userMap = userMap;
    }

    public void setProps(Properties props) {
        this.props = props;
    }

    @Override
    public void save() {
        System.out.println(strList);
        System.out.println(userMap);
        System.out.println(props);
        System.out.println("save...");
    }
}
