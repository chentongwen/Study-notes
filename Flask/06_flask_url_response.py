#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/1/3 16:26 
# @Author : Mr.CTW
# @File : 06_flask_url_response.py 
# @Software: PyCharm

'''
关于响应（Response）：
视图函数的返回值会被自动转换为一个响应对象，Flask的转换逻辑如下；
    1、如果返回的是一个合法的响应对象，则直接返回。
    2、如果返回的是一个字符串，那么Flask会重新创建一个werkzeug.wrappers.Response对象，Response将该字符串作为主体，
        状态码为200，MIME类型为text/html,然后返回该Response对象。
    3、如果返回的是一个元组，元组中的数据类型是（response，status，headeres）。status值会覆盖默认的200状态码，headers可以是
        一个列表或者字典，作为额外的消息头。
    4、如果以上的条件都不满足，Flask会假设返回值是一个合法的WSGI应用程序，并通过Response.force_type(rv,request.environ)
        转换为一个请求对象。
'''

from flask import Flask,Response
#FLASK= werkzeug+sqlalchemy+jinjia2

app = Flask(__name__)

@app.route('/')
def hello_world():
    #Response('Hello workd!',status=200,mimetype='text/html') == return 'hello world!!'
    return 'hello world!!'


@app.route('/1/')
def  list1():
    return ['a','b']

@app.route('/list2/')
def list2():
    return  'list2',200,{'name':'ctw'}

if __name__ == '__main__':
    app.run(debug=True)