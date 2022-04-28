# spring 配置文件



## 详解

### Bean标签范围

![image-20220205182640789](.\\spring.assets\image-20220205182640789.png)



### Bean生命周期

![image-20220205182750042](.\\spring.assets\image-20220205182750042.png)



### Bean实例化的三种方式

#### 1.无参构造方法实例化（常用）

#### 2.工厂静态方法实例化

​	1.创建静态工厂

![image-20220205183454329](.\\spring.assets\image-20220205183454329.png)



 2. 配置spring配置文件

    ```xml
            <bean id="userDao" class="com.iwen.factory.StaticFactory" factory-method="getUserDao"></bean>
    ```

    
    

#### 3.工厂实例方法实例化

![image-20220205184229292](.\\spring.assets\image-20220205184229292.png)





## 依赖注入

容器外部注入：

![image-20220205192824218](.\\spring.assets\image-20220205192824218.png)

![image-20220205192709779](.\\spring.assets\image-20220205192709779.png)

容器内部注入：

![image-20220205193032174](.\\spring.assets\image-20220205193032174.png)

### 1）引用数据类型

#### 1.set方法注入

set方法注入(1)：

![image-20220205194007083](.\\spring.assets\image-20220205194007083.png)



set方法注入(p命名空间):

![image-20220205194259326](.\\spring.assets\image-20220205194259326.png)

![image-20220205194634529](.\\spring.assets\image-20220205194634529.png)



#### 2.有参构造注入

![image-20220205195412672](.\\spring.assets\image-20220205195412672.png)



### 2）普通数据类型

![image-20220205200600250](.\\spring.assets\image-20220205200600250.png)



### 3）集合数据类型

![image-20220205202207430](.\\spring.assets\image-20220205202207430.png)



### xml配置模块导入

![image-20220205202731591](.\\spring.assets\image-20220205202731591.png)





## 配置文件总结

![image-20220205202939704](.\\spring.assets\image-20220205202939704.png)

# spring 相关API

![image-20220205203141898](.\\spring.assets\image-20220205203141898.png)

![image-20220205203222210](.\\spring.assets\image-20220205203222210.png)



# spring 配置数据源

1. properties配置druid数据源

![image-20220208122937682](.\\spring.assets\image-20220208122937682.png)





2. spring文件配置数据源对象

![image-20220208124120460](.\\spring.assets\image-20220208124120460.png)



3. spring加载外部properties文件

![image-20220208124957691](.\\spring.assets\image-20220208124957691.png)



# spring 注解开发

## 1.原始注解

![image-20220208125118919](.\\spring.assets\image-20220208125118919.png)

![image-20220208125218492](.\\spring.assets\image-20220208125218492.png)



注解使用

![image-20220208132101157](.\\spring.assets\image-20220208132101157.png)





![image-20220208134359674](.\\spring.assets\image-20220208134359674.png)



## 2.新注解

![image-20220208134811312](.\\spring.assets\image-20220208134811312.png)

![image-20220208134756770](.\\spring.assets\image-20220208134756770.png)

新注解使用

![image-20220208140623982](.\\spring.assets\image-20220208140623982.png)



