# 一、XPath

## 选取节点

XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。

下面列出了最有用的路径表达式：

| 表达式   | 描述                                                       |
| :------- | :--------------------------------------------------------- |
| nodename | 选取此节点的所有子节点。                                   |
| /        | 从根节点选取。                                             |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .        | 选取当前节点。                                             |
| ..       | 选取当前节点的父节点。                                     |
| @        | 选取属性。                                                 |

### 实例

在下面的表格中，我们已列出了一些路径表达式以及表达式的结果：

| 路径表达式      | 结果                                                         |
| :-------------- | :----------------------------------------------------------- |
| bookstore       | 选取 bookstore 元素的所有子节点。                            |
| /bookstore      | 选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！ |
| bookstore/book  | 选取属于 bookstore 的子元素的所有 book 元素。                |
| //book          | 选取所有 book 子元素，而不管它们在文档中的位置。             |
| bookstore//book | 选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。 |
| //@lang         | 选取名为 lang 的所有属性。                                   |

## 谓语（Predicates）

谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

### 实例

在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

| 路径表达式                         | 结果                                                         |
| :--------------------------------- | :----------------------------------------------------------- |
| /bookstore/book[1]                 | 选取属于 bookstore 子元素的第一个 book 元素。                |
| /bookstore/book[last()]            | 选取属于 bookstore 子元素的最后一个 book 元素。              |
| /bookstore/book[last()-1]          | 选取属于 bookstore 子元素的倒数第二个 book 元素。            |
| /bookstore/book[position()<3]      | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。    |
| //title[@lang]                     | 选取所有拥有名为 lang 的属性的 title 元素。                  |
| //title[@lang='eng']               | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。   |
| /bookstore/book[price>35.00]       | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。 |
| /bookstore/book[price>35.00]/title | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

## 选取未知节点

XPath 通配符可用来选取未知的 XML 元素。

| 通配符 | 描述                 |
| :----- | :------------------- |
| *      | 匹配任何元素节点。   |
| @*     | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

### 实例

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

| 路径表达式   | 结果                              |
| :----------- | :-------------------------------- |
| /bookstore/* | 选取 bookstore 元素的所有子元素。 |
| //*          | 选取文档中的所有元素。            |
| //title[@*]  | 选取所有带有属性的 title 元素。   |

## 选取若干路径

通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

### 实例

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

| 路径表达式                       | 结果                                                         |
| :------------------------------- | :----------------------------------------------------------- |
| //book/title \| //book/price     | 选取 book 元素的所有 title 和 price 元素。                   |
| //title \| //price               | 选取文档中的所有 title 和 price 元素。                       |
| /bookstore/book/title \| //price | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。 |



# 二、BeautifulSoup4

BeautifulSoup是用来从HTML或XML中提取数据的Python库。



### 导入

```python
使用方法：
 from bs4 import BeautifulSoup
 soup = BeautifulSoup(html)
```



### 解析器
1.BeautifulSoup(markup, "html.parser")
2.BeautifulSoup(markup, "lxml")
3.BeautifulSoup(markup, "xml")
4.BeautifulSoup(markup, "html5lib")    



### Tag

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
Tag , NavigableString , BeautifulSoup , Comment .

1.Tag 标签;
任何存在于HTML语法中的标签都可以用soup.<tag>访问获得。           
*当HTML文档中存在多个相同<tag>对应内容时，soup.<tag>返回第一个*。
例如，soup.a ---> 返回<a>标签的内容；
   soup.a.name --> 返回<a>标签的名字；
   soup.a.parent.name --> 返回<a>标签上一层的标签名字；
   soup.a.parent.parent.name

   soup.a.attrs --> 返回<a>标签的所有属性；
   soup.a.attrs['class'] --> 返回<a>标签的class属性；

   soup.a.string --> 返回<a>标签中的非属性内容(也就是<>...</>中的内容)； 只能获取一个！

   soup.get_text() --> 获取所有内容；获取标签下所有的文字内容！

   soup.strings --> 如果tag中包含多个字符串,可以使用 `.strings` 来循环获取;

   soup.stripped_strings --> soup.strings输出的字符串中可能包含了很多空格或空行,使用 `.stripped_strings` 可以去除多余空白内容;



### 内容遍历
   soup.contents
   soup.a.contents --> 将<a>标签所有子节点存入列表；    
   soup.a.children --> 与contents类似，但用于循环遍历子节点；
   soup.a.descendants --> 用于循环遍历子孙节点；

注意：BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点！soup.prettify() --> 让HTML内容更加“友好”的显示，prettify()为HTML文本<>及其内容增加更加'\n'。

### 信息提取
   soup.find_all(name,attrs,recursive,string,**kwargs)
   name:对标签名称的检索；
   attrs:对标签属性值的检索；
   recursive:是否对子孙全部检索，默认为True;
   string: <>...</>中字符串区域的检索。

例如:

soup.find_all('a')

soup.find_all(['a','b'])



**注意：find_all()中可以使用正则表达式来检索特定内容！**
   soup.find_all(re.compile(r'^a'))

**find_all()中使用lambda:**

​	soup.find_all(lambda x:x)



