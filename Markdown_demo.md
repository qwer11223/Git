一级标题
==================

二级标题
-----------------

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题


段落换行 使用两个以上的空格  
加上回车

段落后使用空行

表示重新开始一个段落


*斜体文字*
_斜体文字_

**粗体文字**
__粗体文字__

***粗斜体文字***
___粗斜体文字___



(分隔线)
***
* * *
*****
- - -
-----

(删除线)  
~~demodemodemo~~

(下划线)  
<u>demodemodemo</u>

(脚注)  
创建脚注格式类似这样 [^name]  
[^name]: demodemo

(无序列表)
* 1
* 2
* 3

+ 1
+ 2
+ 3

- 1
- 2
- 3

(有序列表)
1. 第一项
2. 第二项
3. 第三项

(列表嵌套需在子列表中的选项前面添加四个空格)
1. 第一项
    * 第一项嵌套的第一个元素


(区块)
> 1  
> 2  
> 3  

> 1
>> 2
>>> 3


(代码)

`printf()`函数

(代码区块)

    代码区块使用 4 个空格
    或者一个制表符（Tab 键）

```
可使用```包裹一段代码
```

```javascript
//代码区块指定语言

$(document).ready(function () {
    alert('hellow');
});
```

(链接)

百度 www.baidu.com

通过变量设置链接[百度][baidu]

[baidu]: https://www.baidu.com

(图片)
> `![alt 属性文本](图片地址 "可选标题")`

![图片替代文字](https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2654041071,937083517&fm=26&gp=0.jpg "可选标题")

<img src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1337709790,736487537&fm=26&gp=0.jpg" width="50%">

(表格)

> Markdown 制作表格使用 | 来分隔不同的单元格，使用 - 来分隔表头和其他行  
>
>-: 设置内容和标题栏居右对齐。  
:- 设置内容和标题栏居左对齐。  
:-: 设置内容和标题栏居中对齐。

|表头|表头|
|:---:|:---:|
|单元格|单元格|
|单元格|单元格|

(支持html元素)

使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> 重启电脑

(转义)

**加粗**  
\*\*加粗\*\*


<p id="s">fdsfds</p>  

<style>
#s{
    color: #f00;
    font-size: 50px;
    font-family: "华文彩云"
}
</style>