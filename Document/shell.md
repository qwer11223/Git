# Shell 环境
Shell 编程跟 JavaScript、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类众多，常见的有：

* Bourne Shell（/usr/bin/sh或/bin/sh）
* Bourne Again Shell（/bin/bash）
* C Shell（/usr/bin/csh）
* K Shell（/usr/bin/ksh）
* Shell for Root（/sbin/sh）
* ……

本教程关注的是 Bash，也就是 Bourne Again Shell，由于易用和免费，Bash 在日常工作中被广泛使用。同时，Bash 也是大多数Linux 系统默认的 Shell。

在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 #!/bin/sh，它同样也可以改为 #!/bin/bash。

#! 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。

## 运行shell脚本
```sh
# 1. 作为可执行程序

chmod +x ./file.sh  # 增加可执行权限
./file.sh  #执行脚本


# 2. 作为解释器参数

/bin/sh file.sh

#这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。
```

# Shell变量
变量类型
运行shell时，会同时存在三种变量：

1) 局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
2) 环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
3) shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行  

> 定义变量时，变量名不加美元符号  
> 
> `注意，变量名和等号之间不能有空格`

```sh
#!/bin/sh
var1="aa"
readonly constant_var="cv" #只读变量

echo $var1
echo ${constant_var} #括号帮助解释器识别变量边界

unset var1  #删除变量，unset不能删除只读变量

echo $var1

constant_var="aaa" #只读变量无法修改

```

# Shell字符串

```sh
#!/bin/sh

#单引号
#任何字符都会原样输出，单引号字符串中的变量是无效的

str='this is a string'

#双引号
#双引号内可以有变量，可以出现转义字符

str1="aaa\nbbb"

echo -e  $str1 #-e 处理特殊字符 -n 不换行输出

#拼接字符串

con_str1="shell"
con_str2="aaa"$con_str1

echo "bbb" $con_str2

#获取字符串长度
echo ${#str1}

#提取子字符串
echo ${str1:1:4}  #从第2个字符开始截取4个字符

#查找子字符串
substr="dsfsddr"
echo `expr index "$substr" ds`

```

# Shell数组
bash支持一维数组（不支持多维数组），并且没有限定数组的大小。

> `在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开`
```sh
#!/bin/bash

arr=(1 2 3) #定义数组

arr[3]=4

echo ${arr[@]} # @ 读取数组所有元素

echo ${#arr[2]} #取得数组单个元素长度
echo ${#arr[@]} #取得数组元素个数
echo ${#arr[*]} #取得数组元素个数


#多行注释

:<<EOF
注释内容...

注释内容...

注释内容...

EOF

```

# Shell 传递参数

在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：$n。n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……
```sh
#!/bin/bash

echo "\$0 执行文件名：$0"
echo "\$1 第一个参数为：$1"
echo "\$2 第二个参数为：$2"
echo "\$# 传递到脚本的参数个数: $#"
echo "\$* 以一个单字符串显示所有向脚本传递的参数: $*"
echo "\$\$ 脚本运行的当前进程ID号: $$"
echo "\$! 后台运行的最后一个进程的ID号: $!"
echo "\$@ 与 \$* 相同，但是使用时加引号，并在引号中返回每个参数: $@"
echo "\$- 显示Shell使用的当前选项，与set命令功能相同: $-"
echo "\$? 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误: $?"

```

# Shell 基本运算符

https://www.runoob.com/linux/linux-shell-basic-operators.html

# Shell 流程控制

```sh
# if
if condition
then
    command1
    command2
fi

#if else
if condition
then
    command1
    command2
else
    command
fi

#if else-if else
if condition
then
    command1
elif condition2
then
    command2
else
    commandN
fi

#for
for var in item1,item2 ... itemN
do
    command1
    command2
done

#while
while condition
do
    command
done

#------------------

#无限循环

# 1
while :
do
    command
done

# 2
while true
do
    command
done

# 3
for(( ; ;))

#------------------

#until
#until 与 while 处理方式相反 ；循环执行一系列命令直至条件为 true 时停止

until condition
do 
    command
done

#case
#Shell case语句为多选择语句。可以用case语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令

case value in
mode1)
    command1
    command2
    ;;          # ;; 表示 break
mode2)
    command1
    ;;
*)
    command1
    ;;
esac

# 跳出循环
# break 
# continue

```

# Shell 函数
```sh
# [] 代表可选
# 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255）

[ function ] funname [()]
{
    action;

    [return int;]
}


#函数参数
#--------------------
#在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

#!/bin/bash
fun()
{
        for i in "$@" ;do
                echo $i
        done
}

fun 1 2 3 4

```

# Shell 出入/输出重定向
大多数 UNIX 系统命令从你的终端接受输入并将所产生的输出发送回​​到您的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。  

重定向命令列表如下：

|命令|说明|
|:-:|:-:|
|command > file|	将输出重定向到 file。
|command < file	|将输入重定向到 file。
|command >> file|	将输出以追加的方式重定向到 file。
|n > file	|将文件描述符为 n 的文件重定向到 file。
|n >> file	|将文件描述符为 n 的文件以追加的方式重定向到 file。
|n >& m	|将输出文件 m 和 n 合并。
|n <& m	|将输入文件 m 和 n 合并。
|<< tag|	将开始标记 tag 和结束标记 tag 之间的内容作为输入。

> `需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。`

# Shell 文件包含
Shell 可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

Shell 文件包含的语法格式如下：
```sh
. filename   # 注意点号(.)和文件名中间有一空格

或

source filename
```

# Shell echo
```sh
echo aaa    #可省略引号
echo 'aa\c' 
echo "aa\ta"    
echo `date` #显示命令执行结果
echo -e "aaa\n" # -e 开启转义
echo -n "aaa"   # -n 不换行
```

# Shell printf

printf 命令的语法：

> `printf  format-string  [arguments...] `

参数说明：
* format-string: 为格式控制字符串
* arguments: 为参数列表。

```sh
#!/bin/bash
 
# format-string为双引号
printf "%d %s\n" 1 "abc"

# 单引号与双引号效果一样
printf '%d %s\n' 1 "abc"

# 没有引号也可以输出
printf %s abcdef

# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n"
```