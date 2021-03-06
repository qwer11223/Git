# 索引
* [Java基本语法](#Java基本语法)
* [类与对象]()
* [继承]()
* [抽象、接口与标注]()
* [异常与断言]()
* [文件管理与输入/输出]()
* [线程]()
* [图形用户界面设计]()

<br/>

# Java基本语法

![](https://www.runoob.com/wp-content/uploads/2013/12/ZSSDMld.png)

## 基本语法

```java
//第一个java程序

public class Demo{
    public static void main(String [] args){
        System.out.println("demo01");
    }
}
```

```sh
#编译、运行Java程序

$ javac Demo.java
$ java Demo
```

编写 Java 程序时，应注意以下几点：

* 大小写敏感：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的。
* 类名：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 MyFirstJavaClass 。
* 方法名：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
* 源文件名：<mark>源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 .java。（如果文件名和类名不相同则会导致编译错误）。</mark>
* 主方法入口：所有的 Java 程序由 public static void main(String[] args) 方法开始执行。

## Java标识符

Java 所有的组成部分都需要名字。类名、变量名以及方法名都被称为标识符。

关于 Java 标识符，有以下几点需要注意：

* 所有的标识符都应该以字母（A-Z 或者 a-z）,美元符（$）、或者下划线（_）开始
* 首字符之后可以是字母（A-Z 或者 a-z）,美元符（$）、下划线（_）或数字的任何字符组合
* 关键字不能用作标识符
* 标识符是大小写敏感的
* 合法标识符举例：age、$salary、_value、__1_value
* 非法标识符举例：123abc、-salary

## Java修饰符

像其他语言一样，Java可以使用修饰符来修饰类中方法和属性。主要有两类修饰符：

* 访问控制修饰符 : default, public , protected, private
* 非访问控制修饰符 : final, abstract, static, synchronized

## Java注释

```java
// 单行注释

/*
多行注释
*/

/**
文档注释
**/
```

## Java关键字
https://www.runoob.com/java/java-basic-syntax.html


## Java数据类型

Java 的两大数据类型:
* 内置数据类型(八种基本类型)
    * 六种数字类型(四个整数型，两个浮点型)
    * 字符类型
    * 布尔型

整数型：byte(8) 、 short(16) 、 int(32) 、 long(64)  
浮点型：float(32) 、 double(64)  
字符型：char(16)  
布尔型：boolean(8)

`java 中对于一个给定的实数默认为 double ，若表示为 float 需在数之后添加 F 或 f,如 1.23F 、 -0.456f`

* 引用数据类型
    * 在Java中，引用类型的变量非常类似于C/C++的指针。引用类型指向一个对象，指向对象的变量是引用变量。这些变量在声明时被指定为一个特定的类型，比如 Employee、Puppy 等。变量一旦声明后，类型就不能被改变了。
    * 对象、数组都是引用数据类型。
    * 所有引用类型的默认值都是null。
    * 一个引用变量可以用来引用任何与之兼容的类型。

例子：Site site = new Site()

## Java变量

### 变量的定义
> `[修饰符] 数据类型  变量名1[= 值]，变量名2[= 值]`

### 变量类型转换
1. 隐式转换
2. 强制转换
> `(数据类型)表达式`

### 变量作用域

```java

public class Variable{
    static int allClicks=0;    // 类变量,可直接用 ”类名.变量名访问“
 
    String str="hello world";  // 实例变量/成员变量
 
    public void method(){
 
        int i =0;  // 局部变量,必须赋初值
 
    }
}

```
## Java常量

`final [修饰符] 数据类型 常量名=[初始值]`

## 运算符、表达式、程序流程控制

`#与c近似`