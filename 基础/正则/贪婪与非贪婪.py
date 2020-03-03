import re
'''
re.match(pattern,str)
re.search(pattern,str)
re.findall(pattern,str)
re.sub(pattern,str)
re.split(pattern,str)

基础：
.    任意字符
[]   范围
|    或者
()   组


量词：
*     >=0
+     >=1
？    0,1
{m}   =m
{m,}  >=m
{m,n} >=m <=n

预定义：
\s  space
\S  not space
\d  digit
\D  not digit
\w  word      [0-9a-zA-Z]
\W  not word  [^0-9a-zA-Z]
\b  边界
\B

分组：
() -------->group(1)

number
    (\w+)(\d*) ---------> group(1) group(2)
    引用：
    (\w+)(\d*)       \1  \2 表示引用前面得内容

name
    (?P<name>\w+)   (?P=name)


python 里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；
非贪婪则相反，总是尝试匹配尽可能少的字符。
在“*”，“？”，“+”，“{m，n}”后面加上？，使贪婪变成非贪婪。
'''
msg='abc123456ABC'
#默认是贪婪的
result=re.match(r'abc(\d+)',msg)
print (result)
