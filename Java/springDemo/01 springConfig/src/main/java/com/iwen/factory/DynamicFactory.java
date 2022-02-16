package com.iwen.factory;

import com.iwen.dao.UserDao;
import com.iwen.dao.impl.UserDaoImpl;

public class DynamicFactory {
    public UserDao getUserDao(){
        return new UserDaoImpl();
    }
}
