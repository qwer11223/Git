# 索引
* <a href="#sql">SQL</a>
* <a href="#type">数据类型</a>
* <a href="#lg">登录MySQL</a>
* <a href="#db">处理数据库</a>
* <a href="#table">处理表</a>
* <a href="#data">数据操作</a>
* [高级操作](#高级操作)

<br/>

# <a href="#" id="sql"># SQL</a>
> 1. DQL: Data Query Language, 数据查询语言，用于查询和检索数据 
> 2. DML: Data Manipulation Language, 数据操作语言，用于数据的写操作（增删改）
> 3. DDL: Data Definition Language, 数据定义语言，用于创建数据结构
> 4. DCL: Data ConTrol Language, 数据控制语言，用于用户权限管理
> 5. TPL: Transaction Process Language, 事务处理语言，辅助DML进行事务操作（因此也归属于DML）

<br/>

# <a href="#" id="type"># 数据类型 [+]</a>
[+]:https://www.runoob.com/mysql/mysql-data-types.html

> ## 日期和时间
|类型|范围|备注|
|:-:|:-:|:-:|
|date|1000-01-01 ~ 9999-12-31|
|datetime|1000-01-01 00:00:00 ~ 9999-12-31 23:59:59|
|time|-838:59:59 ~ 838:59:59|
|timestamp|1970-01-01 00:00:01 ~ 2037-12-31 23:59:59
|year| 两位数值- 1 ~ 99 ;四位数值- 1901 ~ 2155

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
|类型|大小(bytes)|备注|
|:-:|:-:|:-:|
|char|0 ~ 255
|varchar|0 ~ 65 535
|tinyblob|0 ~ 255
|tinytext|0 ~ 255
|blob|0 ~ 65 535
|text|0 ~ 65 535
|mediumblob|0 ~ 16 777 215
|mediumtext|0 ~ 16 777 215
|longblob|0 ~4 294 967 295
|longtext|0 ~4 294 967 295
|enum
|set

<br/>

# <a href="#" id="lg"># 登录MySQL</a>
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

# <a href="#" id="db"># 处理数据库</a>

## 创建数据库
> `create database db_name;`

## 切换/使用数据库
> `use database_name;`

## 删除数据库
> `drop database db_name;`

## 修改数据库字符集
> `alter database 数据库名 charset utf8;`

<br/>

# <a href="#" id="table"># 处理表</a>

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
drop [temporary] table [if exists] tb1_name [,tb2_name];
```

## 更改表结构
```sql
-- 增加 birthdate 列，data类型
alter table tb add [column] birthdate date;

-- 增加 birthdate 列，data类型,放置在 email 后
alter table tb add [column] birthdate date after email;

-- 修改字段名
alter table 表名 change [column] 旧字段名 新字段名 字段类型 [属性];

-- 修改字段类型
alter table 表名 change 旧字段名 旧字段名 字段类型 [属性];  #不推荐使用change修改

alter table 表名 modify [column] 字段名 字段类型 [属性];

-- 删除字段
alter table 表名 drop 字段名;
```

## 更新表名
> `rename table oldname to newname;`

<br/>

# <a href="#" id="data"># 数据操作</a>
## 新增数据
```sql
insert into 表名 values (字段1对应的值1，字段2对应的值2，...);

-- 指定字段新增数据
insert into 表名 (字段1，字段2，...) values (值1，值2，...);

-- 新增多行记录
insert into 表名 [(字段1，字段2，...)] values (值1，值2，...),(值1，值2，...);
```

## 查看数据
```sql
select * from tb;

select field 1, field 2 from tb;

select field_list / * from tb where expression;
```

## 更新数据
```sql
-- 全部更新
update 表名 set 字段 = 新值;

-- 根据条件更新
update 表名 set 字段 = 新值 where 条件表达式;

-- 修改多个字段数据
update 表名 set 字段1 = 新值1, 字段2 = 新值2 where 条件表达式;
```

## 删除数据
```sql
-- 全部删除
delete from 表名;

-- 按条件删除
delete from 表名 where 条件表达式;
```

<br/>

# 高级操作
## 主键冲突
```sql
-- 1.主键冲突更新
insert into 表名 values (字段1对应的值1，字段2对应的值2，...) on duplicate key update 字段 = 新值

-- 2.主键冲突替换
replace into [(字段列表)] values (值列表)
```

## 蠕虫复制
```sql
-- 一分为二，成倍增加数据，测试表压力
insert into 表名 [(字段列表)] select */字段列表 from 表
```

## 重置 auto_increment
> `truncate 表名;`

## 查询数据
> 完整的查询指令：  
`select 选项 字段列表 from 数据源 where 条件 group by 分组 having 条件 order by 排序 limit 限制;`
>  
>select 选项：系统如何对待查询得到的结果  
>* all:  默认的，表示保存所有的记录  
>* distinct: 去重，去除重复的记录，只保留一条（所有字段都相同的情况）
>
> 字段列表：从多表获取到相同字段时，使用别名(alias)
>* 语法：字段名 [as] 别名  
`select distinct ch ch1,ch ch2 from tb1;`
>
>from 数据源:
>* from 是为前面查询提供数据
>* 多表数据： `select * from tb1, tb2` ，两表数据相乘产生笛卡尔积
>* 动态数据： `select * from (select 字段列表 from 表) as 别名`

## where 子句
where 子句：用来从数据库获取数据的时候，然后进行条件筛选，通过运算符进行结果计较来判断数据

## group by 子句
group by 表示分组的含义：根据指定的字段，将数据进行分组；分组的目标是为了统计
> 基本语法：`group by 字段名`  
> 聚合函数：
>* count(); 统计每组中的数量，如果统计目标是字段，那么不统计为NULL的字段； * 代表统计记录
>* avg(); 求平均值
>* sum(); 求和
>* max(); 求最大值
>* min(); 求最小值
>* group_concat(); 将分组中指定的字段进行合并（字符串拼接）
>
> 多分组：`group by 字段1，字段2;`  
// 先按字段1排序，再将结果按字段2排序...
>
> 分组排序：分组默认有排序功能，默认升序排列字段
> 基本语法：`group by 字段 [asc|desc], [字段 [asc|desc]]`
>
> 回溯统计：每次分组向上统计的过程中都会产生一次新的统计数据，而且当前数据对应的分组字段为 NULL   
`group by 字段 [asc|desc] with rollup`


## having 子句
> having 的本质和 where 一样，用来进行数据条件筛选；  
having 在 group by 子句之后，可以针对分组数据进行统计筛选，但是 where 不行；  
>> **注意：having 在 group by 之后；where 的时候表示将数据从磁盘拿到内存，where 之后的操作都是内存操作；where不能使用聚合函数；**


## order by 子句
> 根据校对规则对数据进行排序  
基本语法：`order by 字段 [asc|desc];  --asc 升序（默认）`  
多字段排序：先按照第一个字段排序，在按照第二个字段排序  
语法：`order by 字段1 [asc|desc], 字段2 [asc|desc]` 


## limit 子句
用来限制记录获取数量，从第一条到指定的数量
> 基本语法： `limit 数量`

分页：利用 limit 获取指定区间的数据
> 基本语法：`limit offset,length;`  
-- offset 偏移量：从哪开始，length 最多获取多少条数据；mysql中记录从 0 开始`


## 运算符 [#]
[#]: https://www.runoob.com/mysql/mysql-operator.html
* 算术运算符
> `+  -  *  /  %`

* 比较运算符
> `>  >=  <  <=  =,<=>  <>,！=   `

* 逻辑运算符
> `NOT 或 !  AND  OR  XOR`
* IN：判断是否在集合内
* IS ：专门用来判断字段是否为 NULL 的运算符
* LIKE：模糊查询

## 联合查询
将多个查询的结果合并到一起（纵向合并），字段数不变，多个查询的记录数合并。

```sql
-- 基本语法
select 语句
union [union 选项]
select 语句;

/*
union 选项:与 select 选项基本一样
distinct: 去重，去掉完全重复的数据（默认）
all: 保存所有的结果
*/

-- 必须是结构完全一致的记录集合才可以使用UNION
-- union 需要保证字段数一样，不需要对应字段类型一致，永远只保留对一个 select 语句对应的字段名字
```

**联合查询中使用 order by:**
1. 第一条 select 语句必须使用括号，否则语法错误
2. 必须配合使用 limit ，limit 数量大于对应表的记录数，否则不生效


<br/>

## 连接查询
将多张表连到一起查询（会导致记录数行和字段数列发生改变）  
> 交叉连接

基本语法： `表1 cross jion 表2;`  
交叉连接产生的结果是笛卡尔积，没有实际应用

> 内连接

内连接：从一张表去除所有记录去另一张表匹配：利用匹配条件，成功保留，失败放弃；  
基本语法：`表1 [inner] jion 表2 on 匹配条件;`  
1. 如果内连接没有匹配条件（允许），那么就是交叉连接（避免）
2. 避免重名错误，通常使用表名.字段名，来确保唯一性 `select * from stu inner join class on stu.class=class.class_id;`
3. 可使用 as 别名简化表名
4. 内连接匹配时，必须保证匹配到才会保存

> 外链接

基本语法：  
左连接：`主表 left [outer] join 从表 on 连接条件;`  
右连接：`主表 right [outer] join 从表 on 连接条件;`

外链接：按照某一张表作为主表（主表中所有记录最后都会保留），根据条件去连接另一张表，从而得到目标数据。  

分类：左外连接(left join)，右外连接(right join)：

左连接：左表是主表  
右连接：右表是主表

> 自然连接

自然连接是一种特殊的等值连接，他要求两个关系表中进行连接的必须是相同的属性列（名字相同），无须添加连接条件，并且在结果中消除重复的属性列。  

基本语法：` select * from table1 natural join table2;`

> using 关键字

基本语法：`表1 [inner,left,right] join 表2 using();`

using 是在连接查询中用来代替 on 关键字进行条件匹配  
1. 连接查询时，使用 using 代替 on
2. 使用 using 的前提是对应两张标的连接字段是同名（类似自然连接自动匹配）
3. 使用 using 关键字，那么对应同名字段，最终结果只会保留一个

<br/>

## 子查询
子查询：指在一条 select 语句中，嵌入了另一条 select 语句，那么被嵌入的 select 语句称为子查询语句

主查询：主要的查询对象，第一条 select 语句，确定用户所有获取的数据目标（数据源），以及要具体得到的字段信息

|分类（按功能）|返回结果|
|:-:|:-:|
|标量子查询|一个数据（一行一列）
|列子查询|一列（一列多行）
|行子查询|一行（一行多列）
|表子查询|多行多列
|exists子查询|1 或 0 （类似布尔操作）

分类（按位置）：  
+ where 子查询：子查询出现的位置在 where 条件中
+ from 子查询： 子查询出现的位置在 from 数据源中（做数据源）

> 标量子查询

基本语法:
```sql
select * from 数据源 where 条件判断 =/<> (select 字段名 from 数据源 where 条件判断);

--子查询得到的结果只有一个值
```

> 列子查询

基本语法：
```sql
主查询 where 条件 in (列子查询);
```

<style>
h1{
    color: #4191ec;
    font-weight: bold;
}

</style>
