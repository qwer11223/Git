package com.iwen.dao;

import com.iwen.domain.User;
import java.util.List;

public interface UserMapper {

    public List<User> findAll();
    public User findById(int id);
}
