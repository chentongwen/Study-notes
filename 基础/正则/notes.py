
'''
正则表达式的特点：
1、灵活性、逻辑性和功能性非常强
2、可以迅速的用既简单的方式大道字符串的复杂控制
3、对于刚接触的人来说晦涩难懂


一.常用正则表达式符号和语法：
'.' 匹配所有字符串，除\n以外
‘-’ 表示范围[0-9]
'*' 匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
'+' 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+ 
##########正则验证次数##########
    '*' 匹配前面的字符0次或多次 re.findall("ab*","cabc3abcbbac")结果：['ab', 'ab', 'a']，贪婪模式即尽可能多的匹配  >=0
    '+' 用于将前面的模式匹配一次或多次（贪婪模式） >=1
    ‘?’ 匹配前一个字符串0次或1次 re.findall('ab?','abcabcabcadf')结果['ab', 'ab', 'ab', 'a']    ##0,1
    '*?','+?','??' 即上边的费贪婪模式（尽可能少的匹配）
    '{m}' 匹配前一个字符m次 re.findall('cb{1}','bchbchcbfbcbb')结果['cb', 'cb']
    '{n,m}' 匹配前一个字符n到m次 re.findall('cb{2,3}','bchbchcbfbcbb')结果['cbb']
    '{n.m}？' 即上边的非贪婪模式

'^' 匹配字符串开头
‘$’ 匹配字符串结尾 re
'\' 转义字符， 使后一个字符改变原来的意思，如果字符串中有字符*需要匹配，可以\*或者字符集[*] re.findall(r'3\*','3*ds')结['3*']

'\d' 匹配数字，等于[0-9] re.findall('\d','电话:10086')结果['1', '0', '0', '8', '6']
'\D' 匹配非数字，等于[^0-9] re.findall('\D','电话:10086')结果['电', '话', ':']
'\w' 匹配字母和数字，等于[A-Za-z0-9] re.findall('\w','alex123,./;;;')结果['a', 'l', 'e', 'x', '1', '2', '3']
'\W' 匹配非英文字母和数字,等于[^A-Za-z0-9] re.findall('\W','alex123,./;;;')结果[',', '.', '/', ';', ';', ';']
'\s' 匹配空白字符 re.findall('\s','3*ds \t\n')结果[' ', '\t', '\n']
'\S' 匹配非空白字符 re.findall('\s','3*ds \t\n')结果['3', '*', 'd', 's']
'\A' 匹配字符串开头
'\Z' 匹配字符串结尾
'\b' 匹配单词的词首和词尾，单词被定义为一个字母数字序列，因此词尾是用空白符或非字母数字符来表示的
'\B' 与\b相反，只在当前位置不在单词边界时匹配
'(?P<name>...)' 分组，除了原有编号外在指定一个额外的别名 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{8})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '19930614'}
[] 是定义匹配的字符范围。比如 [a-zA-Z0-9] 表示相应位置的字符要匹配英文字符和数字。[\s*]表示空格或者*号。

'''

import re
#match 是从头匹配，如果没有匹配到，直接返回None。反之返回<re.Match object; span=(0, 4), match='迪丽热巴'>
msg='迪丽热巴娜扎代斯佟丽娅'
pattern=re.compile('迪丽热巴')
result = pattern.match(msg)
print (result)

###########
#使用正则match
result=re.match('迪丽热巴',msg)
print (result)
##search：全局匹配  
result=re.search('佟丽娅',msg)
print (result)
print(result.span())#返回匹配字符串的位置
print(result.group())#提取匹配的数据



######正则的符号###########

s='tt1if n3algn l544aaf2ngk 5lad423sfaf4f'
result=re.search('[a-z][0-9][a-z]',s) #search匹配到第一个就返回，不会匹配后续的结果
print (result)
print (result.group())

#匹配所有结果findall
result=re.findall('[a-z][0-9][a-z]',s)
print (result)

#匹配首字母是英文，中间是数字，中间1个数字和中间多个数字，末尾是字母
result=re.findall('[a-z][0-9]+[a-z]',s)
print (result)

#验证qq号,是5~11位。
qq='2324858'
result=re.match('^[1-9][0-9]{4,10}$',qq)
print (result)

#用户名可以是字母和数字，但不能以数字开头，用户名长度必须6位以上。
username='admin_001'
result=re.match('^[a-zA-Z][0-9a-zA-Z]{5,}$',username)
print (result)
#用户名可以是字母和数字和下划线，但不能以数字开头，用户名长度必须6位以上。
username='admin001'
result=re.match('^[a-zA-Z]\w{5,}$',username)
print (result)

#\b的使用边界
msg= 'a*py  ab.txt bb.txt kk.py tyt.png  1.py'
result= re.findall(r'\w*\.py\b',msg)
print (result)

'''
'.' 任意字符除(\n)
^ 开头
$ 结尾
[] 范围 


正则预定义
\s  空格
\b  边界
\d
\w  word
大写的是反义
\S 非空格

'\w[0-9]'----> \w [0-9] 只能匹配一个字母

量词：
* >=0
+ >=1
? 0,1

{m} 固定m位
{m} >=m
{m,n}  >=m  <=n

'''