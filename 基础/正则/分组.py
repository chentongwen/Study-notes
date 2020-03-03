import re
#匹配数字0-100数字
'''
| 或者
'''
n='89'
#改进版
result=re.match(r'[1-9]?\d?$|100$',n)
print (result)

#(word|word2) 匹配整体的括号word或者Word2
# [word|123] 匹配是w，o，r，d，1,2,3都可以
#验证输入的邮箱 163,126,qq
email='123456@qq.com' 
result=re.match(r'\w{5,12}@(163|126|qq)\.(com|cn)',email)
print (result)

#不是以4,7结尾的手机号（11位）
phone='15639888259'
result=re.match(r'1\d{9}[0-35-689]$',phone)
print (result)

#分组部分
##爬虫相关
phone='010-12345678'
#表示'()'分组
result=re.match(r'(\d{3}|\d{4})-(\d{8})$',phone)
print (result)
print (result.group())
#group(1) 是指第一组内容
#第二个()，(2)是第二组第二组内容。
print (result.group(1))
print (result.group(2))

#
msg='<html>abc</h1>'
xxx='<h1>hello</h1>'
result=re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9A-Za-z]+>$',msg)
print (result)
print (result.group(1))
#匹配成对的
#'\1'表示引用
#r'<([0-9a-zA-Z]+)>(.+)</\1>$'；'\1'=([0-9a-zA-Z]+)匹配到的字符
result=re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg)
print ('111',result)
result=re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',xxx)
print ('222',result)
#

msg='<html><h1>abc</h1></html>'
result=re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print (result)
print (result.group(1))
print (result.group(2))
print (result.group(3))
#别名的方式防止上边数字引用容易引起的混乱,此处的别名是指给分组起的别名，利于后续的引用。
result=re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
print (result)
print (result.group(1))
print (result.group(2))
print (result.group(3))


##re的替换函数sub
result =re.sub(r'\d+','90','java:100,python:80')
print (result)
#sub使用函数替换
def func(temp):
    num=temp.group()
    num1=int(num)+1
    return str(num1)
result =re.sub(r'\d+',func,'java:100,python:80')
print (result)


#切割 split

result=re.split(r'[,:]',"java:100,python:80")
print (result)
'''
分组：（）-----》result.group(1) 获取组中匹配内容
    在分组的时候还可以结合“|”来使用，“|”表示或的意思
    不需要引用分组的内容：
        result=re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9A-Za-z]+>$',msg)
        print (result)
        print (result.group(1))
    引用分组匹配内容:
        1.number  \number 引用number组数据


        2.?P<名字>

'''

'''
re模块使用的函数
match   从开头匹配符合的内容
search  查找符合的内容只匹配一次
findall 查找所有符合的内容
sub(正则表达式，新内容，string)
split result=re.split(r'[,:]',"java:100,python:80") 在字符串中搜索如果遇到:或者，就分割将分割的内容都保存到列表中。

'''

