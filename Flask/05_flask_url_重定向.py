#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/1/3 10:03 
# @Author : Mr.CTW
# @File : 05_flask_url_重定向.py 
# @Software: PyCharm
'''
页面跳转和重定向：
重定向分为永久性重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。
例子：用户访问一个需要权限的页面，但是该用户当前并没有登录，因此我们应该给他重定向到登录页面。

永久性重定向：http的状态码是301，多用于旧网址被废弃转到一个新网址确保用户的访问，最经典的就是京东网站，’
    你输入www.jingdong.com的时候，会被重定向到www.jd.com,因为jingdong.com这个网址已经被废弃了，被改成jd.com，
    这种情况应该用永久重定向。
暂时性重定向：http的状态码是302，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向
    到登录页面，这种情况，应该用暂时性重定向。

在flask中，重定向是通过flask.redirect(location,code=302)这个函数来实现的，location表示需要重定向到的URL，应该配合之前
    讲的url_for()函数来使用，code表示才用那个重定向，默认是302也即暂时性重定向，可以修改成301来实现永久性重定向。

'''
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    return '这是登录界面'

@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '个人中心页面'
    else:
        return redirect(url_for('login'))
if __name__ == '__main__':
    app.run()
