import re

string = 'MR_SHOP mr_shop'
string1 =  'aa MR_SHOP mr_shop'
pattern = r'mr_\w+'

#---- match() --------

match = re.match(pattern,string,re.I)

print(match)
print(re.match(pattern,string1,re.I)) #第一个字母不符合条件时，则不再进行匹配，返回None

print('匹配值的起始位置：',match.start())
print('匹配值的结束位置：',match.end())
print('匹配位置的元组：',match.span())
print('要匹配的字符串：',match.string)
print('匹配数据：',match.group())


#----- search() ---------

match2 = re.search(pattern,string,re.I)

print(match2)
print(re.search(pattern,string1,re.I))

#---- findall() 在整个字符串中搜索所有符合正则表达式的字符串，返回列表 ------

find = re.findall(pattern,string,re.I)
print(find)

ip = '127.0.0.1 192.168.1.10'
str1 = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
print(re.findall(str1,ip))

#---- sub() 替换字符串 --------

str2 = 'aaaa'
print(re.sub(r'a{4}','bbb',str2))

#---- split() 分割字符串，以列表形式返回----

url = 'http://www.itht.com?username="aa"&pwd="123"'
pattern = r'[?|&]' #定义分隔符

result = re.split(pattern,url)
print(result)