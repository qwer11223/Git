# SQL
> 1. DQL: Data Query Language, 数据查询语言，用于查询和检索数据 
> 2. DML: Data Manipulation Language, 数据操作语言，用于数据的写操作（增删改）
> 3. DDL: Data Definition Language, 数据定义语言，用于创建数据结构
> 4. DCL: Data ConTrol Language, 数据控制语言，用于用户权限管理
> 5. TPL: Transaction Process Language, 事务处理语言，辅助DML进行事务操作（因此也归属于DML）

<br/>

# 数据类型
> ## 日期和时间

> ## 数值 (整数)  
|类型|储存字节|有符号数范围|无符号数范围|备注|
|:-:|:-:|:-:|:-:|:-:|
|bool|-|-|-|tinyint(1) 别名，用于赋值 0 和 1|
|tinyint|1|-128 ~ 127|0 ~ 255|
|smallint|2|-32 768 ~ 32 767|0 ~ 65 535|
|mediumint|3|-8 388 608 ~ 8 388 607|0 ~ 16 777 215
|int|4|-2 147 483 648 ~ 2 147 483 647|0 ~ 4 294 967 295|
|bigint|8|-9 223 372 036 854 755 808 ~ 9 233 372 036 854 775 807|0 ~ 18 446 744 073 709 551 615|

**<p style="color:green">显示宽度：不会影响对应类型本身大小，通常配合zerofill实现数据不足宽度时用前导 0 补充至指定宽度</p>**

> ## 数值 (浮点)
|类型|储存字节|有效精度|备注|
|:-:|:-:|:-:|:-:|
|float|4|7 ~ 8位|
|double|8|15 ~ 16位|
|decimal|自适应|15 ~ 16位|（定点型）不会丢失精度

> ## 字符串



<br/>

# 登录MySQL
> `mysql -u root -p`

-h : host 连接服务器的主机地址，本机使用localhost可省略该参数  
-u : username 登录用户名  
-p : （小写）password 登录密码，不推荐提供密码作为选项  
-P : （大写）port 端口号，默认为3306，可省略  
-D : database 指定目标数据库名称，进入客户端后就不必执行 USE 命令  


## 注释
> `-- 注释内容`  
`# 注释内容`  
`/* 注释内容 */`


## 查看数据库列表
> ` show databases;`


## 查看部分数据库
> `show databases like 'name';`

* 占位符（下划线）：匹配固定位置单个字符，_a
* 占位符（百分号）：匹配多个字符，%a


## 查看所有表
> `show tables;`

<br/>

# 处理数据库

## 创建数据库
> `create database db_name;`

## 切换/使用数据库
> `use database_name;`

## 删除数据库
> `drop database db_name;`

## 修改数据库字符集
> `alter database 数据库名 charset utf8;`

<br/>

# 处理表

## 创建表
```sql
create table [if not exists] tb(
    id tinyint unsigned not null auto_increment,
    email varchar(25) not null,
    phone varchar(20) not null,
    primary key(id)
);
```

## 复制表
```sql
-- 将tb副本，名为tb1
create table tb1 select * from tb;

-- 基于现有表的几个列创建一个表
create table tb2 select email, phone from tb;
```

## 创建临时表
```sql
create temporary table temp_tb select email, phone from tb;
```

## 查看可用表
> `show tables;`

## 查看表结构
> `desc tb == (describe tb);`

## 删除表
```sql
drop [temporary] table [id exists] tb1_name [,tb2_name];
```

## 更改表结构
```sql
-- 增加 birthdate 列，data类型
alter table tb add column birthdate date;

-- 增加 birthdate 列，data类型,放置在 email 后
alter table tb add column birthdate date after email;

-- 修改列
alter table tb change birthdate birthdate date not null;

-- 删除birthdate列
alter table tb drop birthdate;
```