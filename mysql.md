# 索引
* <a href="#sql">SQL</a>
* <a href="#type">数据类型</a>
* <a href="#lg">登录MySQL</a>
* <a href="#db">处理数据库</a>
* <a href="#table">处理表</a>
* <a href="#data">数据操作</a>
* [高级操作](#高级操作)
* [联合查询](#联合查询)
* [连接查询](#连接查询)
* [子查询](#子查询)
* [外键](#外键)
* [视图](#视图)
* [事务](#事务)
* [数据备份与还原](#数据备份与还原)
* [用户权限管理](#用户权限管理)

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

# 联合查询
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

# 连接查询
将多张表连到一起查询（会导致记录数行和字段数列发生改变）  
> ## 交叉连接

基本语法： `表1 cross jion 表2;`  
交叉连接产生的结果是笛卡尔积，没有实际应用

> ## 内连接
![inner_join_img](https://www.runoob.com/wp-content/uploads/2014/03/img_innerjoin.gif)

内连接：从一张表去除所有记录去另一张表匹配：利用匹配条件，成功保留，失败放弃；  
基本语法：`表1 [inner] jion 表2 on 匹配条件;`  
1. 如果内连接没有匹配条件（允许），那么就是交叉连接（避免）
2. 避免重名错误，通常使用表名.字段名，来确保唯一性 `select * from stu inner join class on stu.class=class.class_id;`
3. 可使用 as 别名简化表名
4. 内连接匹配时，必须保证匹配到才会保存

> ## 外链接

基本语法：  
左连接：`主表 left [outer] join 从表 on 连接条件;`  
右连接：`主表 right [outer] join 从表 on 连接条件;`

外链接：按照某一张表作为主表（主表中所有记录最后都会保留），根据条件去连接另一张表，从而得到目标数据。  

分类：左外连接(left join)，右外连接(right join)：

左连接：左表是主表  
右连接：右表是主表

![left_join_img](https://www.runoob.com/wp-content/uploads/2014/03/img_leftjoin.gif)
![right_join_img](https://www.runoob.com/wp-content/uploads/2014/03/img_rightjoin.gif)


> ## 自然连接

自然连接是一种特殊的等值连接，他要求两个关系表中进行连接的必须是相同的属性列（名字相同），无须添加连接条件，并且在结果中消除重复的属性列。  

基本语法：` select * from table1 natural join table2;`

> ## using 关键字

基本语法：`表1 [inner,left,right] join 表2 using();`

using 是在连接查询中用来代替 on 关键字进行条件匹配  
1. 连接查询时，使用 using 代替 on
2. 使用 using 的前提是对应两张标的连接字段是同名（类似自然连接自动匹配）
3. 使用 using 关键字，那么对应同名字段，最终结果只会保留一个

<br/>

# 子查询
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

> ## 标量子查询

基本语法:
```sql
select * from 数据源 where 条件判断 =/<> (select 字段名 from 数据源 where 条件判断);

--子查询得到的结果只有一个值
```

> ## 列子查询

基本语法：
```sql
主查询 where 条件 in (列子查询);
```

> ## 行子查询

基本语法：
```sql
主查询 where 条件 [(构造一个行元素)] = (行子查询)

-- 字段元素是指一个字段对应的值
-- 行元素对应的就是多个字段 
```

> ## 表子查询

基本语法：
```sql
select 字段列表 from (表子查询) as 别名 [where][group by][having][order by][limit]; 

-- 表子查询先执行
-- from 后必须跟表名
```

> ## exists 子查询

返回结果只有 0 和 1;

基本语法：
```sql
where exists (查询语句);

-- exists 根据查询得到的结果进行判断
-- 结果存在返回 1 ，否则返回 0
```

> ## 子查询中的特定关键字
+ in：`主查询 where 条件 in (列子查询);`
+ any:  
`=any(列子查询); -- 条件在查询结果中有任意一个匹配即可，等价于 in`  
`<>any(列子查询); -- 条件在查询结果中不等于任意一个`
+ some：与 any 完全一致
+ all:   
`=all(列子查询); -- 等于其中所有`  
`<>all(列子查询); -- 不等于其中所有` 

*！！如果对应匹配字段有 NULL 那么不参与匹配；*

<br/>

# 外键
如果公共关键字在一个关系中是主关键字，那么这个公共关键字被称为另一个关系的外键。由此可见，外键表示了两个关系之间的相关联系。以另一个关系的外键作主关键字的表被称为主表，具有此外键的表被称为主表的从表。外键又称作外关键字。
> 外键：foreign key  
一张表（A）中有一个字段，保存的值指向另外一张表（B）的主键  
B：主表  
A：从表

## 增加外键
1. 方案1：在创建表的时候增加外键（类似主键）  
基本语法：在字段之后增加一条语句 `[constraint `\`自定外键名\``] foreign key (外键字段) references 主表(主键);`

2. 方案2：在创建表后增加外键  
基本语法：`alter table 从表 add [constraint `\`自定外键名\``] foreign key(外键字段) references 主表(主键);`

> MUL：多索引，外键本身是一个索引，外键要求外键字段本身也是一种普通索引


## 修改&删除外键
外键不允许修改，只能先删除后增加  
基本语法： `alter table 从表 drop foreign key 外键名字;`

外键不能删除产生的普通索引，只会删除外键自己，如果想删除对应的索引：`alter table 表名 drop index 索引名字;`


## 外键基本要求
1. 外键字段需要保证与关联的主表的主键字段类型完全一致；
2. 基本属性也要相同
3. 如果是在表后增加外键，对数据还有一定的要求（从表数据与主表的关联关系）
4. 外键只能使用innodb存储引擎：myisam不支持


## 外键约束
1. 当一个外键产生时：外键所在的表（从表）会受制于主表数据的存在从而导致数据不能进行某些不符合规范的操作（不能插入主表不存在的数据）；
2. 如果一张表被其他表外键引入，那么该表的数据操作就不能随意：必须保证从表数据的有效性（不能随便删除一个被从表引入的记录）；

---

可以在创建外键的时候，对外键约束进行选择性的操作。

> 基本语法： `add foreign key(外键字段) references 主表(主键)  on [指定操作] 约束模式 [on [指定操作] 约束模式];`

指定操作：
* update
* delete

约束模式有三种：  
1. district：严格模式，默认的，不允许操作  
2. cascade：级联模式，一起操作，主表变化，从表数据跟着变化  
3. set null：置空模式，主表变化（删除），从表对应记录设置为空：前提是从表中对应的外键字段允许为空


> **约束作用**  

保证数据的完整性：主表与从表的数据要一致

正是因为外键有非常强大的数据约束作用，而且可能导致数据在后台变化的不可控。导致程序在进行设计开发逻辑的时候，没有办法去很好的把握数据（业务），所以外键比较少使用。

<br/>

# 视图

## 创建视图

视图的本质是SQL指令（select语句）  
>基本语法：`create view 视图名字 as select指令;`	//可以是单表数据，也可以是连接查询，联合查询或者子查询

## 查看视图

视图本身是虚拟表，所以关于表的一些操作都适用于视图
> `Show tables/show create table[view]/desc 视图名字；`

## 使用视图

视图是一张虚拟表：可以直接把视图当做“表”操作，但是视图本身没有数据，是临时执行select语句得到对应的结果。视图主要用户查询操作。

> 基本语法：`select 字段列表 from 视图名字 [子句];`

## 修改视图

修改视图：本质是修改视图对应的查询语句
> 基本语法：`alter view 视图名字 as 新select指令;`

## 删除视图

> 基本语法：`drop view 视图名字;`


<br/>

# 事务
概念：  
事务(Transaction)是访问并可能更新数据库中各种数据项的一个程序执行单元(unit)。事务通常由高级数据库操纵语言或编程语言书写的用户程序的执行所引起。事务由事务开始(begin transaction)和事务结束(end transaction)之间执行的全体操作组成。

基本原理：  
Mysql允许将事务统一进行管理（存储引擎INNODB），将用户所做的操作，暂时保存起来，不直接放到数据表（更新），等到用于确认结果之后再进行操作。

<br/>

## 自动事务

`autocommit`，当客户端发送一条SQL指令（写操作：增删改）给服务器的时候，服务器在执行之后，不用等待用户反馈结果，会自动将结果同步到数据表。

查看事务开启状态：
> `show variables like 'autocommit[%]';`

关闭自动事务：关闭之后系统就不在帮助用户提交结果了  
> `set autocommit = Off;`

一旦自动事务关闭，那么需要用户提供是否同步的命令  
> `Commit`：提交（同步到数据表：事务也会被清空）  
> `Rollback`：回滚（清空之前的操作，不要了）


## 手动事务

手动事务：不管是开始还是过程还是结束都需要用户（程序员），手动的发送事务操作指令来实现。

手动事务对应的命令：
1. `start transaction;` //开启事务：从这条语句开始，后面的所有语句都不会直接写入到数据表（保存在事务日志中）
2. 事务处理：多个写指令构成
3. 事务提交：`commit/rollback`，到这个时候所有的事务才算结束

## 回滚点

回滚点：`savepoint`，当有一系列事务操作时，而其中的步骤如果成功了，没有必要重新来过，可以在某个点（成功），设置一个记号（回滚点），然后如果后面有失败，那么可以回到这个记号位置。

增加回滚点：
> `savepoint 回滚点名字`; //字母数字和下划线构成

回到回滚点：
> `rollback to 回滚点名字`; //那个记号（回滚点）之后的所有操作没有了

注意：在一个事务处理中，如果有很多个步骤，那么可以设置多个回滚点。但是如果回到了前面的回滚点，后面的回滚点就失效；


## 特性

<mark>事务的ACID特性</mark>

事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

原子性（`atomicity`）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
事务从start transaction起到提交事务（commit或者rollback），要么所有的操作都成功，要么就是所有的操作都失败；

一致性（`consistency`）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
数据表中的数据修改，要么是所有操作一次性修改，要么是根本不动。

隔离性（`isolation`）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
如果一个客户端在使用事务操作一个数据（可能是一行/整表）的时候，另外一个客户端不能对该数据进行操作。

> 什么时候是行被隔离？什么时候是整表被隔离？
说明：如果条件中使用了索引（主键），那么系统是根据主键直接找到某条记录，这个时候与其他记录无关，那么只隔离一条记录；反之，如果说系统是通过全表检索（每一条记录都去检查：没有索引），被检索的所有数据都会被锁定（整表）

持久性（`durability`）。持久性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。


<br/>

# 变量

## 系统变量
> 查询

查看所有系统变量：`show variables [like 'pattern'];`

查询变量数据值（系统变量）：`select @@变量名;`

> 修改

1. 局部修改（会话级别）：只针对当前自己客户端当次连接有效  
基本语法：`set 变量名 = 新值;`

2. 针对所有的客户端，“所有时刻”都有效 （除本次连接）  
基本语法：`set global 变量名 = 值; 或 set @@global.变量名 = 值;`  
*全局修改只针对新客户端生效（正在连着的无效）*


## 会话变量

会话变量也称之为用户变量，会话变量跟mysql客户端是绑定的，<mark>设置的变量，只对当前用户使用的客户端当次连接生效。</mark>

> 赋值

定义用户变量：`set @变量名 := 值;`

使用变量的赋值符 `:=` 避免与比较符 `=` 冲突

1. 赋值且查看赋值过程：  
`select @变量1 := 字段1，@变量2 := 字段2 from 数据表 where 条件;`

2. 只赋值，不看过程：  
`select 字段1，字段2… from 数据源 where条件 into @变量1，@变量2…`

> 查看

查看变量：`select @变量名;`

## 局部变量

作用范围在begin到end语句块之间。在该语句块里设置的变量，declare语句专门用于定义局部变量。

声明语法：`declare 变量名 数据类型 [属性];`

<br/>

# 流程结构

## if 分支

1. 用在select查询当中，当做一种条件来进行判断  
基本语法：`if(条件,为真结果,为假结果)`

2. 用在复杂的语句块中（函数/存储过程/触发器）  


```sql
基本语法：

if  条件表达式  then 
	满足条件要执行的语句;
end  if;
```



## while 循环

> 基本语法
```sql
while 条件 do
	要循环执行的代码;
end while;
```

> 结构标识符

标识符(标识名字)的存在主要是为了循环体中使用循环控制。
```sql
标识名: while 条件 do
	-- 要循环执行的代码;
    -- iterate/leave 标识名;
end while [标识名];

-- -----------
iterate：迭代，就是以下的代码不执行，重新开始循环（continue）
leave：离开，整个循环终止（break）

```


<br/>

# 函数 [&]
[&]:https://www.runoob.com/mysql/mysql-functions.html

## 内置函数

> 字符串函数
* char_length()：判断字符串的字符数
* length()：判断字符串的字节数（与字符集有关，按照字符集和字符关系转换）
* concat()：连接字符串
* instr()：判断字符在目标字符串中是否存在，存在返回其位置，不存在返回0
* lcase()：全部小写
* left()：从左侧开始截取，直到指定位置（位置如果超过长度，截取所有）
* ltrim()：消除左边对应的空格
* mid()：从中间指定位置开始截取，如果不指定截取长度，直接到最后

> 时间函数
* now()：返回当前时间，日期 时间
* curdate()：返回当前日期
* curtime()：返回当前时间
* datediff()：判断两个日期之间的天数差距，参数日期必须使用字符串格式（用引号）
* date_add(日期,interval 时间数字 type)：进行时间的增加`type:day/hour/minute/second`
* unix_timestamp()：获取时间戳

> 数学函数
* abs()：绝对值
* ceiling()：向上取整
* floor()：向下取整
* pow()：求指数，谁的多少次方
* rand()：获取一个随机数（0-1之间）
* round()：四舍五入函数

> 其他函数
* MD5()：对数据进行md5加密(mysql中的md5与其他任何地方的md5加密出来的内容是完全相同的)
* version()：获取版本号
* databse()：显示当前所在数据库
* UUID()：生成一个唯一标识符（自增长）：自增长是单表唯一，UUID是整库（数据唯一同时空间唯一）


## 自定义函数

1. 自定义函数是属于用户(会话)级别的：只有当前客户端对应的数据库中可以使用
2. 可以在不同的数据库下看到对应的函数，但是不可以调用
3. 自定义函数：通常是为了将多行代码集合到一起解决一个重复性的问题
4. 函数必须规范返回值：所以在函数内部不能使用select指令(select一旦执行就会得到一个结果(result set)，会直接输出，相当于返回)
但是这个是唯一可用的(给变量赋值)：select 字段 into @变量;


> 创建函数

```sql
delimiter $$   --修改语句结束符
create function 函数名(形参) returns 返回类型
begin
    -- 函数体
    return 返回值;  -- 数据必须与结构中定义的返回值类型一致
end
$$      -- 语句结束
delimter ;  -- 结束符改回 ;

```

> 查看函数

```sql
-- 1.可以通过查看function状态，查看所有的函数
show function status [like 'pattern'];

-- 2.查看函数的创建语句
show create function 函数名
```

> 调用函数

`select 函数名(实参)`

> 删除函数

`drop function 函数名`

<br/>

# 存储过程

## 与函数区别
> 相同点

1、	存储过程和函数目的都是为了可重复地执行操作数据库的sql语句的集合。  
2、	存储过程函数都是一次编译，后续执行。编译一次，就会被缓存起来，下次使用直接命中缓存中编译好的sql，不再重复编译

> 不同点

1、标识符不同。函数的标识符为FUNCTION，过程为：PROCEDURE。  
2、函数中有返回值，且必须返回；而过程没有返回值(必须没有)。  
3、过程无返回值类型，调用时不能将过程的结果直接赋值给变量(因为没有返回值，没有结果)；函数有返回值类型，调用时，除使用select语句调用(如select now())外，必须将返回值赋给变量。  
4、函数可以在select语句中直接调用，而过程不能。(函数是使用select调用，过程不是)


## 存储过程操作

> 创建过程

```sql
delimiter $$
create procedure 过程名([参数列表])
begin
    -- 过程体
end
$$
delimiter ;
```

> 查看过程
```sql
-- 查看全部存储过程
show procedure status [like ‘pattern’];

-- 查看过程创建语句
show create procedure 过程名字;
```

> 调用过程

过程：没有返回值，select不可能调用

语法：`call 过程名([实参列表]);`


> 删除过程

`drop procedure 过程名字;`


## 存储过程的形参类型
存储过程也允许提供参数（形参和实参）：存储的参数也和函数一样，需要指定其类型。  
但是存储过程对参数还有额外的要求：有自己的参数分类(以下三类)：

* `in`  
表示参数从外部传入到里面使用（过程内部使用）：可以是直接数据也可以是保存数据的变量	--类似值传递
只传递值

* `out`  
表示参数是从过程里面把数据保存到变量中，交给外部使用：传入的必须是变量
如果说传入的out变量本身在外部有数据，那么在进入过程之后，第一件事就是被清空，设为NULL	--类似引用传递
进去出来都变(进去被赋为null，出来重新被赋为实参的值)

* `inout`  
数据可以从外部传入到过程内部使用，同时内部操作之后，又会将数据返还给外部。	--类似引用传递
进去不变出来变(出来重新被赋为实参的值)

>参数使用级别语法（形参）  
`过程类型 变量名 数据类型;  //in int_1 int,out int_2 int,inout int_3 int`


<br/>

# 数据备份与还原
整库数据备份也叫SQL数据备份：备份的结果都是SQL指令；  
在Mysql中提供了一个专门用于备份SQL的客户端：<mark>mysqldump.exe</mark>

## SQL 备份
基本语法：  
> `mysqldump -u -p 数据库名字 [表1 [表2 …]] > 备份文件地址\文件名.sql`

1. 整库备份（只需要提供数据库名字）
2. 单表备份：数据库后面跟一张表
3. 多表备份：数据库后跟多张表

## 数据还原
Mysqldump备份的数据中没有关于数据库本身的操作，都是针对表级别的操作：当进行数据（SQL还原），必须指定数据库

数据还原有三种方法：
1. 利用mysql.exe客户端：可以不先登录，直接用该客户端进行数据还原  
`mysql -u -p 数据库 < 文件位置`

2. 在SQL指令，提供了一种导入SQL指令的方式  
`source  SQL文件位置;  -- 必须先进入到对应的数据库`

3. 人为操作：打开备份文件，复制所有SQL指令，然后到mysql.exe客户端中去粘贴执行。（不推荐）

<br/>

# 用户权限管理

Mysql需要客户端进行连接认证才能进行服务器操作：需要用户信息。<red>Mysql中所有的用户信息都是保存在mysql数据库下的user表中。<red>

在mysql中，对用的用户管理中，是由对应的Host和User共同组成主键来区分用户。  
User：代表用户的用户名  
Host：代表本质是允许访问的客户端（IP或者主机地址）。如果host使用%代表所有的用户（客户端）都可以访问

## 创建用户

1、	直接使用root用户在mysql.user表中插入记录（不推荐）  
2、	专门创建用户的SQL指令
基本语法：
```sql
create user 用户 identified by '明文密码';

-- 用户：用户名@主机地址
-- 主机地址：(空)’’ 或 ‘%’

create user 用户名;
-- 简化版创建用户（谁都可以访问，不需要密码）
```

## 删除用户

注意：mysql中user是带着host本身的（具有唯一性）
> 基本语法：`drop user 用户名@host;	 -- 不带@host也可以`


## 修改用户密码

基本语法：  
> `ALTER USER 'test'@'localhost' IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY '新密码';`

## 权限管理

在mysql中将权限管理分为三类：
1. 数据权限：增删改查（select\update\delete\insert）
2. 结构权限：结构操作（create\drop）
3. 管理权限：权限管理（create user\grant\revoke）：通常只给管理员如此权限

> 授予权限：grant

将权限分配给指定的用户  

基本语法： `grant 权限列表 on 数据库/*.表名/* to 用户; `

权限列表：使用逗号分隔，但是可以使用all privileges代表全部权限  

数据库.表名：可以是单表`（数据库名字.表名）`，可以是具体某个数据库`（数据库.*）`，也可以整库 `(*.*)`

> 取消权限：revoke

权限回收：将权限从用户手中收回

基本语法：`revoke 权限列表/all privileges on 数据库/*.表/* from 用户;`

> 刷新权限：flush

基本语法：`flush privileges;`

Flush：刷新，将当前对用户的权限操作，进行一个刷新，将操作的具体内容同步到对应的表中(有可能存在对权限的操作 没有写入到表中)。

<primary>(有很多权限修改是不需要刷新的。比如 授予、撤销表权限这种操作，不需要刷新，因为每次用户查询表时服务端都会验证用户有没有对应表的权限)</primary>


## 密码丢失

如果忘记了root用户密码，就需要去找回或者重置root用户密码

1. 停止服务
2. 重新启动服务：`mysqld.exe –skip-grant-tables`  &nbsp;&nbsp;&nbsp;//启动服务器但是跳过权限
3. 当前启动的服务器没有权限概念：非常危险，任何客户端，不需要任何用户信息都可以直接登录，而且是root权限：新开客户端，使用mysql.exe登录即可
4. 修改root用户的密码：指定 用户名@host
5. 关闭服务器，重启服务



[^_^]:#(==================style=====================================)
<style>
h1{
    color: #4191ec;
    font-weight: bold
}

h2{
    font-weight: bold
}

img{
    background-color:#fff
}

red{
    color: #f00
}

primary{
    color: #07d
}

</style>
