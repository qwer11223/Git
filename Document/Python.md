# 索引
* [Python3语言基础](#Python3语言基础)
* [运算符与表达式](#运算符与表达式)
* [流程控制语句](#流程控制语句)
* [列表](#列表)
* [元组](#元组)
* [字典](#字典)
* [集合](#集合)
* [字符串](#字符串)
* [正则表达式](#正则表达式)
* [函数]()
* [面向对象程序设计]()
* [模块]()
* [异常处理]()
* [文件及目录操作]()
* [操作数据库]()
* [GUI界面]()
* [线程和进程]()


<br/>

# `Python3语言基础`
## 注释
```py
# 单行注释

'''
 多行注释
'''

"""
 多行注释
"""

#中文注释
#-*- coding:utf-8 -*-
或
#coding:utf-8
```

## 基本数据类型
+ Number (数字)
  1. 整数
  2. 浮点数
+ String (字符串)
+ List (列表)
+ Tuple (元组)
+ Set (集合)
+ Dictionary (字典)

> 数据类型转换

|函数|作用|
|:-:|:-:|
|int(x)|将x转换成整数类型
|......|......

## 基本输入和输出
* input()
* print()

<br/>

# `运算符与表达式`
详见： https://www.runoob.com/python3/python3-basic-operators.html


<br/>

# `流程控制语句`

条件控制： https://www.runoob.com/python3/python3-conditional-statements.html

```py
if expression:
  #statement

#-------------------

if exp:
  #statement1
else:
  #statement2

#-------------------

if exp1:
  #statement1
elif exp2:
  #statement2
elif exp3:
  #statement3
else:
  #statement4

#------------

```

循环语句：https://www.runoob.com/python3/python3-loop.html

```py

while exp:
  #statement

for var in obj:
  #statement

#break
#continue
#pass

```

<br/>

# `列表`
(数组)

```py

list = ['a','b','c']

#切片
list[start:end:step]

#乘法
print(list*3) #['a','b','c','a','b','c','a','b','c']

# list() 创建列表
list1 = list(range(5))

#删除列表
del listname

#添加元素
list.append('d')

list.extend(list1) #将一个列表中的全部元素添加到另一个列表

#修改元素
list[1] = 'e'

#删除元素
del list[0]

list.remove('c') #根据元素值删除

```

|函数|功能|
|:-:|:-:|
count()|获取元素出现次数
index()|获取指定元素首次出现的下标
sum(list[,start])|列表求和
sort([key=None,reverse=False])|对原列表中的元素进行排序
sorted(list[,key=None,reverse=False])|返回排序后的列表，不修改原列表

<br/>

## 列表推倒式
`list = [expression for var in range]`

<br/>

# `元组`
(不可变序列，元组中的元素不能单独需改)

```py
#创建元组
tuple1 = ('a','b','c')

tuple(range(5))

#删除
del tuple1

#修改元组
#只能对元组重新赋值

```

## 列表推倒式
`tuple2 = (expression for var in range)`

<br/>

# `字典`
(键-值对)

```py

#创建字典
dictionary = {'key1':'value1','key2':'value2', ...}

dictionary1 = dict(zip(list1,list2))

dictionary2 = dict(key1=value1,key2=value2)

dictionary3 = dict.fromkeys(list) #使用list创建值为空的字典


#删除字典
del dictionary

dictionary.clear() #清空字典元素


#访问字典
print(dictionary['key1'])

dictoinary.get('key1')


#遍历字典

for item in dictionary.item():
  print(item)

#item()方法返回字典的 "键-值对" 元组列表
#values()
#keys()

```

## 字典推倒式
`dictionary4 = {i:random.randint(10,100) for i in range(5)}`

<br/>

# `集合`
(保存不重复的元素)

```py

#创建集合
set1 = {ele1,ele2, ...}

set2 = set(list1 | tuple1) #使用set()函数创建集合

#向集合中添加元素
set1.add(element)

#删除元素
remove(ele)  #移除指定元素
pop() #删除一个元素
clear() #清空集合

#集合的交集、并集、差集运算
& #交集运算
| #并集
- #差集
^ #对称差集

```

<br/>

# `字符串`

```py

#encode() "编码"，将字符串转换为二进制数据(bytes)
str.encode([encoding="utf=8"][,erroes="strict"])

#encoding 进行转码时采用的字符编码
#errors 制定错误处理方式


#decode() "解码"
bytes.decode([encoding="utf=8"][,erroes="strict"])


#拼接字符串 '+'

print(str1 + str2)

```

|函数|功能|
|:-:|:-:|
len(string)|计算字符串长度
string[start:end:step]|截取字符串
str.spilt(sep,maxsplit)|分割字符串
str.join(iterable)|合并字符串
str.count()|
str.find()|
str.index()|
str.startswith()|
str.endswith()|
str.lower()|
str.upper()|
str.strip()|
str.lstrip()|
str.rstrip()|

<br/>

# `正则表达式`