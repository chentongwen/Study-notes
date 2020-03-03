from flask import Flask,url_for

#url_for 就是指通过结果可以找到为url路径

app = Flask(__name__)


@app.route('/')
def hello_world():
    # print(url_for('my_list',page=2))
    # return 'Hello World!'
    return (url_for('my_list', page=2,count=2))



@app.route('/list/<page>/')
def my_list(page):
    return 'my_list'

@app.route('/1/')
def A():
    return url_for('login',next='/')

@app.route('/login/')
def login():
    return 'login'

if __name__ == '__main__':
    app.run(debug=True)

#url_for的基本使用
#url_for第一个参数，应该是视图函数的名字的字符串。后面的参数就是传递给url。
#如果传递的参数之前在url中已经定义了，那么这个参数就会被当成path的形式给url。如果这个参数
#之前没有在url中定义，那么将变成查询字符串的形式放到url中


#为什么需要url_for
#1.将来如果修改了url，但没有修改url对应的函数名，就用到去替换url了
#2.url_for会自动的处理那些特殊的字符，不需要手动去处理。
