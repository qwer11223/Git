package com.iwen.test;

import com.iwen.domain.Account;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.List;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("classpath:applicationContext.xml")
public class JDBCTemplateCRUDTest {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Test
    public void testQueryCount() {
        Integer integer = jdbcTemplate.queryForObject("select count(*) from account", Integer.class);
        System.out.println(integer);
    }

    @Test
    public void testQueryOne() {
        Account account = jdbcTemplate.queryForObject("select * from account where id=?", new BeanPropertyRowMapper<Account>(Account.class), 1);
        System.out.println(account);
    }


    @Test
    public void testQueryAll() {
        List<Account> accountList = jdbcTemplate.query("select * from account",new BeanPropertyRowMapper<Account>(Account.class));
        System.out.println(accountList);
    }

    @Test
    public void testDelete() {
        int row = jdbcTemplate.update("delete from account where id=?", 2);
        System.out.println(row);
    }

    @Test
    public void testUpdate() {
        int row = jdbcTemplate.update("update account set password=? where id=?", 666, 2);
        System.out.println(row);
    }
}
