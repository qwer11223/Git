# 索引
* [Java基本语法](#Java基本语法)
* [面向对象]()
* [多线程]()
* [Java API]()
* [集合类]()
* [IO]()
* [GUI]()
* [网络编程]()

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

## Java数组

一维数组：

```java
int[] x = new int[100];

int[] y;
y = new int[100];

System.out.println("y[0]: " + y[0]);

for (int i = 0; i < x.length; i++)
	System.out.println(x[i]);


```



二维数组：

```java
int[][] arr = new int[3][4];

int[][] arr1 = new int[3][];

int[][] arr2 = { { 1, 2 }, { 1, 2, 3, 4 }, { 1, 2, 3 } };

System.out.println(arr2[0][0]);

for(int i=0;i<arr2.length;i++)
    for(int j=0;j<arr2[i].length;j++)
        System.out.println("arr2: "+arr2[i][j]);
```



<br/>



# 面向对象

## 1. 类的定义

```java
/**
 * define class
 */

class Person {
    int age = 10; // 成员变量

    void speak() {
        int age = 60; // 局部变量
        System.out.println(age);
    }
}
```



## 2. 对象的创建与使用

> `类名 对象名称 = new 类名()`

```java
public class Object {
    public static void main(String[] args) {
        Person p1 = new Person();
        Person p2 = new Person();
        p1.age = 18;
        p1.speak();
        p2.speak();
    }
}
```



## 3. 构造方法

1. 方法名与类名相同
2. 在方法名的前面没有返回值类型声明
3. 在方法中不能使用 return 语句返回一个值

```java
public class Object {
    public static void main(String[] args) {
        
        Person p1 = new Person();
        Person p2 = new Person("llll");
    }
}

/**
 * define class
 */

class Person {
    int age = 10; // 成员变量

    // 构造方法与类同名
    public Person() {
        System.out.println("aaa");
    }

    // 构造方法重载
    public Person(String a) {
        System.out.println(a);
    }

    void speak() {
        int age = 60; // 局部变量
        System.out.println(age);
    }
}
```



## 4. this 关键字

```java
class Person{
    int age;

    public Person(int age){
        this.age=age; // 1. 通过this访问类成员变量，解决局部变量冲突
    }

                        // 2. 通过this调用成员方法

    public Person(){
        this(2); // 3. 调用有参构造方法 
        getAge();
    }

    public int getAge(){
        return this.age;
    }
}
```



## 5. static 关键字

1. 静态变量 ： 在内存中只有一份，同一个类的所有实例对象共享，不可修饰局部变量

```java
public class Static {
    public static void main(String[] args) {
        Student stu1 = new Student();
        Student stu2 = new Student();
        Student.school = "aaa";
        System.out.println(stu1.school);
        System.out.println(stu2.school);
    }
}

class Student {
    static String school;
}
```



2. 静态方法： 不创建对象就可调用某个方法，静态方法使用 `类名.方法名` 访问

```java
public class Static {
    public static void main(String[] args) {
        Person.say();
    }
}

class Person{
    public static void say(){
        System.out.println("static method");
    }
}
```



3. 静态代码块 :  类加载时，静态代码块会执行，由于类只会加载一次，因此静态代码块只执行一次；通常使用静态代码块对类成员变量进行初始化。

```java
public class Static {
    public static void main(String[] args) {
        Block b = new Block();
    }
}

class Block{
    static String country;

    // static code block
    static{
        country = "china";
        System.out.println("class block static code block execute");
    }
}
```



## 6. 单例模式

java中的一种设计模式，指在设计一个类时，需要保证在整个程序运行期间针对该类只存在一个实例对象。

```java
public class Single {
    public static void main(String[] args) {
        Case c1 = Case.getInstance();
        Case c2 = Case.getInstance();
        System.out.println(c1 == c2);

        Case1 c3 = Case1.INSTANCE;
        Case1 c4 = Case1.INSTANCE;
        System.out.println(c3 == c4);
    }
}

/**
 * 单例模式： 1. 类的构造方法使用private修饰，使得不可在类外部使用new创建对象 2.
 * 在类内部创建实例对象，使用静态变量引用，禁止外界直接访问声明为private 3. 通过静态方法返回实例对象，由于静态方法，可使用 “ 类名.方法名
 * ”访问
 */

class Case {
    private static Case INSTANCE = new Case();

    private Case() {
    }; // 私有化构造方法

    public static Case getInstance() {
        return INSTANCE;
    }
}

class Case1{
    //单例模式另一种形式

    private Case1(){};
    public static final Case1 INSTANCE = new Case1(); //final禁止外部对该变量进行修改

    // 使用 “ 类名.变量名 ” 获得实例对象
}
```



## 7. 内部类

在一个类的内部定义类，成为内部类。

1. 内部成员类 : 内部类可在外部类中被使用，并能访问外部类的成员。

```java
class Outer {
    private int num = 4; // 类的成员变量

    public void test() {    // 成员方法，用来访问内部类
        Inner inner = new Inner();
        inner.show();
    }

    class Inner {   //成员内部类
        void show() {   //在内部类访问外部类的成员变量
            System.out.println("num=" + num);
        }
    }
}

public class InnerClass{
    public static void main(String[] args) {
        // 通过外部类方法访问内部类
        Outer outer = new Outer();
        outer.test();

        // 直接通过外部类访问内部类

        /* 外部类名.内部类名 变量名 = new  外部类名().new 内部类名() */
        
        Outer.Inner inner = new Outer().new Inner(); //创建内部类对象
        inner.show();
    }
}
```



2. 静态内部类 ： 通过static修饰一个成员内部类，称为静态内部类，可不创建外部类对象的情况下被实例化。

```java
class Outer {
    private static int num = 6; 

    static class Inner {   //静态内部类
        void show() {   
            System.out.println("num=" + num);
        }
    }
}

public class InnerClass{
    public static void main(String[] args) {
        Outer.Inner inner = new Outer.Inner();
        inner.show();
    }
}
```



3. 方法内部类 ： 在成员方法内定义类，只能在当前方法中被使用。

```java
class Outer {
    private static int num = 6;

    public void test(){
        class Inner {  
            void show() {  
                System.out.println("num=" + num);
            }
        }

        Inner inner = new Inner();
        inner.show();
    }
}

public class InnerClass{
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.test();
    }
}
```



## 8. 继承

### 继承

使用 extends 关键字

```java
class A{
    String name;

    void fun(){
        System.out.println("class A");
    }
}

class B extends A{
    public void p(){
        System.out.println("name = " + name);
    }

    void fun(){     // 重写父类方法， 不能使用比父类重写方法更严格的访问权限 P117
        System.out.println("class B");
    }
}

public class Inherit{
    public static void main(String[] args) {
        B b = new B();
        b.name = "class_B";
        b.p();
        b.fun();
    }
}
```

### super

1. 使用super调用父类成员变量和成员方法

```java
class A{
    String name = "A";

    void fun(){
        System.out.println("class A");
    }
}

class B extends A{
    String name = "B";
    
    void fun(){
        super.fun();
    }
}

public class Super {
    public static void main(String[] args) {
        B b = new B();
        b.fun();
    }
}
```



2. 使用super调用父类构造方法

```java
class A{
    public A(){
        System.out.println("construct-fun-A");
    }
}

class B extends A{
    public B(){
        super();
    }
}

public class Super {
    public static void main(String[] args) {
        B b = new B();
    }
}
```





## 9. final关键字

1. final 修饰类

被final修饰的类不能被继承

```java
final class Animal{
    // methods
}
```



2. final 修饰方法

被final修饰的方法不能被子类重写

```java
class Animal{
    public final void shout(){
        //code
    }
}
```



3. final 修饰变量

被final修饰的变量为常量

```java
public class Example{
    public ststic void main(String[] args){
        final int num = 2;
        num = 4; // throw error!!!
    }
}
```



## 10. 抽象类和接口

抽象类：

1. ==包含抽象方法的类必须声明为抽象类，但抽象类可以不包含任何抽象方法==
2. ==抽象类不可以被实例化==
3. ==调用抽象类中定义的方法需创建子类实现抽象方法==

```java

public class Abstract {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.shout();
    }
}

//abstract class
abstract class Animal{
    abstract void shout();
}

class Dog extends Animal{
    void shout(){
        System.out.println("dog");
    }
}
```



接口：

1. 接口中的方法都是抽象的，不能被实例化
2. 当一个类实现接口时，如果这个类是抽象类，可实现接口中部分方法，否则需实现接口中所有方法
3. 一个类可实现多个接口
4. 一个接口可通过extends继承多个接口
5. 一个类继承另一个类的同时还可以实现接口

```java
public class Interface {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.run();
    }
}

interface Animal{
    int ID = 1; //全局常量	//默认使用 public static final 修饰
    void run(); //抽象方法	 //默认使用 public abstract 修饰
}

interface LandAnimal extends Animal{
    void liveOnLand();
}

class Dog implements LandAnimal{
    public void run(){
        System.out.println("run");
    }

    public void liveOnLand(){
        System.out.println("live");
    }
}

```







## 11. 多态

同一方法中由于参数类型不同而导致的执行效果各异的现象就是多态。

```java
class Polymorphic{
    public static void main(String[] args) {
        NetCard n = new NetCard();
        SoundCard s = new SoundCard();
        MothBoard mb = new MothBoard();

        mb.usePci(n); //send...
        mb.usePci(s); //sound
    }
}

interface PCI{
    void start();   //接口中方法默认使用 public abstract 修饰
}

class NetCard implements PCI{
    public void start(){
        System.out.println("send...");
    }
}

class SoundCard implements PCI{
    public void start(){
        System.out.println("sound");
    }
}

class MothBoard{
    public void usePci(PCI p){
        p.start();
    }
}
```



## 12. 异常

try...catch...finally

throws 抛出异常

```java
public class Abnormal {
    public static void main(String[] args) {
        try{
            int res = divide(4, 2);
            System.out.println(res);
        }catch(Exception e){
            e.printStackTrace();
        }finally{
            System.out.println("finally");
        }
    }

    public static int divide(int x, int y) throws Exception { // throws抛出异常
        int reslut = x / y;
        return reslut;
    }
}
```



## 13. 包

```java
package cn.itht //使用package 关键字声明包
// javac -d . demom.java 编译生成与包对应的目录

import cn.itht.*; //导入包下所有类
```



jar 打包：

`jar -cvf demo.jar package`  //打包

`java -jar demo.jar`  //运行jar包 （在MANIFEST.MF 文件添加 Main-Class: 包名.类名）

`jar -xvf demo.jar`  //解压jar包



## 14. 访问控制

(p157)

private(类访问级别) -> default(包访问级别) -> protected(子类访问级别) -> public(公共访问级别)

==类或类的成员不使用修饰符默认为default==



# 多线程

## 1. 继承Thread类创建多线程

```java

public class MyThread {
    public static void main(String[] args) {
        Sub s = new Sub();
        s.start();
        while(true){
            System.out.println("main() method is running");
        }
    }
}

class Sub extends Thread{
    public void run(){
        while(true){
            System.out.println("run() method is running");
        }
    }
}
```



## 2. Runnable接口创建多线程

由于java只支持单继承，多继承类可使用Runnable接口实现多线程

1. 实现Runnable接口的 run() 方法
2. 调用 Thread 的 另一个构造方法 Thread(Runnablr Target)
3. 使用 Runnable 接口中的 run() 方法作为运行代码

```java

public class MyThread {
    public static void main(String[] args) {
        Sub s = new Sub();
        Thread thread = new Thread(s);
        thread.start();
        while(true){
            System.out.println("main() method is running");
        }
    }
}

class Sub implements Runnable{	//实现Runnable接口
    public void run(){
        while(true){
            System.out.println("run() method is running");
        }
    }
}
```



## 3. 后台线程

(p172)

新创建的线程默认都是前台线程，如果程序中只有后台线程在运行，这个进程就会结束。

设置后台线程：

`Thread.setdeamon(true) `



## 4. 线程调度

### 线程的优先级

(p175)

设置线程优先级：

`Thread.setPriority(int newPriority)`

- newPriority: 1-10之间整数或Thread类的三个静态变量



```java
public class Priority{
    public static void main(String[] args) {
        Thread minPriority = new Thread(new MinPriority(),"MinPriority");
        Thread maxPriority = new Thread(new MaxPriority(),"MaxPriority");
        minPriority.setPriority(Thread.MIN_PRIORITY); //设置低优先级
        maxPriority.setPriority(Thread.MAX_PRIORITY); //设置高优先级
        minPriority.start();
        maxPriority.start();
    }
}

class MaxPriority implements Runnable{
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println(Thread.currentThread().getName() + " output " + i);
        }
    }
}

class MinPriority implements Runnable{
    public void run(){
        for(int i=0;i<10;i++){
            System.out.println(Thread.currentThread().getName() + " output " + i);
        }
    }
}
```



### 线程休眠

`Thread.sleep(long millis)`

使当前线程休眠一段时间，休眠结束后，线程返回到就绪状态。



```java
public class Priority {
    public static void main(String[] args) throws Exception {
        new Thread(new SleepThread()).start();
        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                Thread.sleep(2000);
            }
            System.out.println("Mian Thread output: " + i);
            Thread.sleep(500);
        }
    }
}

class SleepThread implements Runnable {
    public void run() {
        for (int i = 1; i <= 10; i++) {
            if (i == 3) {
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Thread 1 output: " + i);
            try {
                Thread.sleep(500);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
```





### 线程让步

`Thread.yield()`

yield不会阻塞线程，直接将线程转换为就绪状态，让系统调度器重新调度。

```java
public class Priority {
    public static void main(String[] args) throws Exception {
        Thread  t1 = new YieldThread("Thread A");
        Thread t2 = new YieldThread("Thread B");
        t1.start();
        t2.start();
    }
}

class YieldThread extends Thread{
    public YieldThread(String name){
        super(name); //call parent class constrauct method
    }

    public void run(){
        for(int i=0;i<5;i++){
            System.out.println(Thread.currentThread().getName() + " --- " + i);
            if(i==3){
                System.out.print("thread yeild: ");
                Thread.yield();
            }
        }
    }
}
```



### 线程插队

`Thread.join()`

在某个线程中调用其他线程的join()方法时，调用的线程将被阻塞，直到被join()方法加入的线程==执行完成==后他才会继续运行。

```java
public class Priority {
    public static void main(String[] args) throws Exception {
        Thread t = new Thread(new EmergencyThread(), "Thread 1");
        t.start();
        for (int i = 1; i < 6; i++) {
            System.out.println(Thread.currentThread().getName() + " input: " + i);
            if (i == 2) {
                System.out.println(t.getName() + " join:");
                t.join();
            }
            Thread.sleep(500);
        }
    }
}

class EmergencyThread implements Runnable {
    public void run() {
        for (int i = 1; i < 6; i++) {
            System.out.println(Thread.currentThread().getName() + " input: " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```



## 5. 多线程同步

### 同步代码块

线程执行同步代码块时，首先检查锁对象的标志位，默认为1，此时执行同步代码块，同时将锁对象标志位置为0；线程获取锁对象有一定的随机性。

```java
public class Example {
    public static void main(String[] args) {
        SaleThread saleThread = new SaleThread();
        new Thread(saleThread, "Thread 1").start();
        new Thread(saleThread, "Thread 2").start();
        new Thread(saleThread, "Thread 3").start();
        new Thread(saleThread, "Thread 4").start();

    }
}

class SaleThread implements Runnable {
    private int tickets = 10;
    Object lock = new Object();	//新建任意锁对象

    public void run() {
        // sync block
        synchronized (lock) {
            while (true) {

                // delay
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                // sale
                if (tickets > 0)
                    System.out.println(Thread.currentThread().getName() + " ---sale ticket " + tickets--);
                else
                    break;

            }
        }
    }
}
```



### 同步方法

同步方法的锁是 **当前调用该方法的对象**，也就是this指向的对象；静态方法的锁对象是 **该方法所在类的class对象**，该对象可直接使用 “ 类名.class ” 获取。

```java
public class Example2 {
    public static void main(String[] args) {
        Ticket1 t = new Ticket1();
        new Thread(t, "Thread 1").start();
        new Thread(t, "Thread 2").start();
        new Thread(t, "Thread 3").start();
        new Thread(t, "Thread 4").start();
    }
}

class Ticket1 implements Runnable {
    private int tickets = 10;

    public void run() {
        while (true) {
            saleTicket();
            if (tickets <= 0)
                break;
        }
    }

    private synchronized void saleTicket() {	//sync method
        if (tickets > 0) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(Thread.currentThread().getName() + " ---sale ticket " + tickets--);

        }
    }
}
```



### 多线程通信

(p188)

|方法声明|功能描述|
| :-:  | :-:  |
| void wait() | 使当前线程进入等待状态 |
| void notify() | 唤醒此同步锁上等待的第一个调用 wait() 方法的线程 |
| void notifyAll() | 唤醒此同步锁上调用 wait() 方法的所有线程 |

```java
public class Example4 {
    public static void main(String[] args) {
        Storage st = new Storage();
        Input input = new Input(st);
        Output output = new Output(st);

        new Thread(input).start();
        new Thread(output).start();
    }
}

class Storage {
    private int[] cells = new int[10];
    private int inPos, outPos; // array flag
    private int count;

    public synchronized void put(int num) {
        try {
            while (count == cells.length)
                this.wait();
            cells[inPos] = num;
            System.out.println("cells[" + inPos + "] input data ---- " + cells[inPos]);
            inPos++;
            if (inPos == cells.length)
                inPos = 0;
            count++;
            this.notify();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public synchronized void get() {
        try {
            while (count == 0)
                this.wait();
            int data = cells[outPos];
            System.out.println("cells[" + outPos + "] get data " + data);
            outPos++;
            if (outPos == cells.length)
                outPos = 0;
            count--;
            this.notify();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

class Input implements Runnable {
    private Storage st;
    private int num;

    Input(Storage st) {
        this.st = st;
    }

    public void run() {
        while (true) {
            st.put(num++);
        }
    }
}

class Output implements Runnable {
    private Storage st;

    Output(Storage st) {
        this.st = st;
    }

    public void run() {
        while (true) {
            st.get();
        }
    }
}
```



# JAVA API

* String & StringBuffer
* System & Runtime
* Math & Random
* 包装类
* Date & Canlendar & DateFormat



# 集合类

## 一. Collection

(单列集合类根接口 [value] )

### 1. List

（有序，可重复）

```java
package list;

import java.util.*;

public class ArrayListDemo {
    public static void main(String[] args) {
        //1. ArrayList[长度可变数组] 底层使用数组保存元素
        // ArrayList<Number> list = new ArrayList<>();

        //2. LinkedList[双向循环链表]
        LinkedList<Number> list = new LinkedList<>();
        list.add(123);
        list.add(3);
        list.add(5);
        list.add(2);

        System.out.println(list);

        // Iterator
        Iterator<Number> it = list.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

        System.out.println("-------------");

        // foreach
        for (Number tmp : list)
            System.out.println(tmp);

        System.out.println("-------------");

        //3. Vector 线程安全 用法与 ArrayList 相同
        Vector<Number> v = new Vector<>();
        v.add(1);
        v.add(0);
        Enumeration<Number> e = v.elements();
        while (e.hasMoreElements())
            System.out.println(e.nextElement());
    }
}
```



### 2. Set

（无序，不可重复）

```java
package set;

import java.util.*;

public class HashSetDemo {
    public static void main(String[] args) {

        // 1.HashSet[哈希值]
        //1.1 add()添加元素
        //1.2 hashCode() 获取哈希值
        //1.3 根据哈希值计算存储位置
        //1.4 equals() 比较元素是否相等
        //1.5 将元素存入集合或移除元素
        HashSet<String> set = new HashSet<>();
        set.add("Jack");
        set.add("Eve");
        set.add("Eve");

        System.out.println(set);

        System.out.println("-------------");

        //2.TreeSet[自平衡二叉树]
        // compareTo()比较元素并存入
        TreeSet<String> ts = new TreeSet<>();
        ts.add("Helena");
        ts.add("Helena");
        ts.add("Eve");

        System.out.print(ts);

    }
}
```





## 二. Map

(双列集合类根接口 [key - value] )

```java
package map;

import java.util.*;

public class HashMapDemo {
    public static void main(String[] args) {
        // 1.HashMap(键不重复)
        Map<Number, String> map = new HashMap<>();
        map.put(1, "Jack");
        map.put(2, "Rose");
        map.put(3, "Lucy");

        map.get(2);

        System.out.println("-------------");

        // 遍历1:获取所有键遍历
        Set<Number> keySet = map.keySet(); // 获取键集合
        Iterator<Number> it = keySet.iterator(); // 迭代键集合
        while (it.hasNext()) {
            Object key = it.next();
            Object value = map.get(key);
            System.out.println(key + ":" + value);
        }

        System.out.println("-------------");

        // 遍历2:获取所有映射关系，从中取出键和值
        // Set entrySet = map.entrySet();
        // Iterator i = entrySet.iterator();
        // while (i.hasNext()) {
        // Map.Entry entry = (Map.Entry) (it.next());
        // Object key = entry.getKey();
        // Object value = entry.getValue();
        // System.out.println(key + ":" + value);
        // }

        // 2. LinkedHashMap(HashMap的子类，有序，双向链表存储结构)
        // ...

        // 3.TreeMap(二叉树存储结构)
        // ...

        // 4.Hashtable [线程安全] -> Properties：常用于存取配置项，存储字符串类型的键和值

    }
}
```



## 三. 泛型

```java
package generics;

import java.util.ArrayList;

// 泛型（参数化类型）：在编译时检测非法类型

public class Demo {
    // 1. 泛型方法: 规则：类型参数<T> 声明在方法返回类型前
    public static <T> void printArray(T[] inputArray) {
        for (T element : inputArray) {
            System.out.printf("%s", element);
        }
        System.out.println(); // 换行
    }

    public static void main(String[] args) {
        Integer[] intArr = { 1, 2, 3 };
        Double[] dArr = { 1.1, 2.2, 3.3 };
        Character[] chArr = { 'A', 'B', 'C' };

        printArray(intArr);
        printArray(dArr);
        printArray(chArr);

        ////// 2. 泛型类 //////////
        cachePool<Integer> pool = new cachePool<>();
        pool.save(1);
        Integer temp = pool.get();
        System.out.println(temp);
    }
}

// 2. 泛型类
class cachePool<T> {
    T temp;

    public void save(T tmp) {
        this.temp = tmp;
    }

    public T get() {
        return temp;
    }

    // 类型通配符
    public void test(ArrayList<?> list) {
        ;
    }
}
```



# IO

```java
package com.example;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.LineNumberReader;
import java.io.OutputStream;

/*
    IO 流
    |
    |_ 一、字节流
        |_ <1>InputStream <抽象类>
            |_ 1.FileInputStream
            |_ 2.FilterInputStream
                |_ BufferedInputStream //字节缓冲流
        |_ <2>OutputStream <抽象类>
            |_ 1.FileOutputStream
            |_ 2.FilterOutputStream
                |_ BufferedOutputStream
    |
    |_ 二、字符流
        |_ <1>Reader <抽象类>
            |_1.InputStreamReader
                |_FileReader
            |_2.BufferedReader
                |_LineNumberReader
        |_ <2>writer <抽象类>
            |_1.OutputStreamWriter
                |_FileWriter
            |_2.BufferedWriter
*/

public class IO {
    public static void main(String[] args) throws Exception {

        new Line();
    }
}

/////////// 字节流 /////////////////
// 1.FileInputStream
class In {
    public In() throws IOException {
        FileInputStream in = new FileInputStream("src/main/java/com/example/test.txt");
        int b = 0;
        while (true) {
            b = in.read();
            if (b == -1) {
                break;
            }
            System.out.println(b);
        }
        in.close();
    }
}

// 1.1 fileOutputStream
class Out {
    public Out() throws IOException {
        FileOutputStream out = new FileOutputStream("./out.txt");
        String str = "测试字符";
        byte[] b = str.getBytes();
        for (int i = 0; i < b.length; i++) {
            out.write(b[i]);
        }
        out.close();
    }
}

// 1.2字节流的缓冲区 (p288)
class Buff {
    public Buff() throws IOException {
        InputStream in = new FileInputStream("out.txt");
        OutputStream out = new FileOutputStream("out_copy.txt");
        byte[] buff = new byte[1024];
        int len;
        long begintime = System.currentTimeMillis();
        while ((len = in.read(buff)) != -1) {
            out.write(buff, 0, len);
        }
        long endtime = System.currentTimeMillis();
        System.out.println("消耗时间: " + (endtime - begintime) + " ms");
        in.close();
        out.close();
    }
}

// 1.4 字节缓冲流
class BufferedStream {
    public BufferedStream() throws IOException {
        // (p290 装饰设计模式)
        // BufferedInputStream、BufferedOutputStream 和 1.2 方法类似
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("out.txt"));
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("out_buff_copy.txt"));
        int len;
        while ((len = bis.read()) != -1) {
            bos.write(len);
        }
        bis.close();
        bos.close();
    }
}

//////////////// 字符流 ///////////////////

// 2.字符流操作文件
// 2.1 FileReader
class Read {
    public Read() throws Exception {
        FileReader reader = new FileReader("out.txt");
        int ch;
        while ((ch = reader.read()) != -1) {
            System.out.println((char) ch);
        }
        reader.close();
    }
}

// 2.2 FileWriter
class Write {
    public Write() throws IOException {
        FileWriter writer = new FileWriter("writer.txt");
        String str = "FileWrite test";
        writer.write(str);
        writer.write("\r\n");
        writer.close();
    }
}

// 2.3 BufferedReader 、BufferedWriter (装饰设计模式)
class BuffRW {
    public BuffRW() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("out.txt"));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("char_buff_copy.txt"));
        String str;
        while ((str = bufferedReader.readLine()) != null) {
            bufferedWriter.write(str);
            bufferedWriter.newLine();
        }
        bufferedReader.close();
        bufferedWriter.close();
    }
}

class Line {
    public Line() throws IOException {
        FileReader fileReader = new FileReader("Test.java");
        FileWriter fileWriter = new FileWriter("test_copy.java");
        LineNumberReader lineNumberReader = new LineNumberReader(fileReader); // 包装
        lineNumberReader.setLineNumber(0);  //设置行号
        String line = null;
        while ((line = lineNumberReader.readLine()) != null) {
            fileWriter.write(lineNumberReader.getLineNumber() + ':' + line);
            fileWriter.write("\r\n");
        }
        lineNumberReader.close();
        fileWriter.close();
    }
}
```



# Junit

```java
package junit;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class CalculatorTest {

    Calculator calculator = new Calculator();

    //-------------------------------------------------

    /**
     * 初始化方法：
     * 用于资源申请：修饰的方法在所有测试方法执行前都会先执行该方法
     */
    @Before
    public void init() {
        System.out.println("init...");
    }

    /**
     * 释放资源方法：
     * 修饰的方法在所有测试方法执行后执行
     */
    @After
    public void close(){
        System.out.println("close...");
    }

    //--------------------------------------------------

    @Test
    public void testAdd() {
        // System.out.println(calculator.add(1, 2));
        int add = calculator.add(1, 2);

        // Assert
        Assert.assertEquals(3, add);
    }

    @Test
    public void testSub() {
        int sub = calculator.sub(1, 3);
        Assert.assertEquals(-1, sub);
    }
}
```

