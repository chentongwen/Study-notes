from flask import Flask,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)


@app.route('/')
def hello_world():
    print(url_for('blog1',section=['y','t']))
    return 'Hello World!'

@app.route('/user/<int:user_id>/')
def user(user_id):
    return '您输入的userid为：{0}'.format(user_id)


#一个url中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式
class TelephoneConveter(BaseConverter):
    regex = r'1[875]\d{9}'
app.url_map.converters['tel'] = TelephoneConveter

@app.route('/telephone/<tel:my_tel>/')
def phone(my_tel):
    return '您的手机号码是：{0}'.format(my_tel)

#用户在访问博客的时候，需求访问 A版块和B板块的所有帖子。

#传统使用方式
@app.route('/blog/<section>/')
def blog(section):
    section=section.split('+')
    return "您提交的板块是：{0}".format(section)

#to_python模式
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    # to_url 将会调用url_for函数的时候生成符合要求的url形式
    def to_url(self, value):
        b="+".join(value)
        return b
app.url_map.converters['list'] = ListConverter

@app.route('/blog1/<list:section>/')
def blog1(section):
    return "您提交的板块是：{0}".format(section)

if __name__ == '__main__':
    app.run(debug=True)


#自定义Url转换器的方式
#1、实现一个类，继承自BaseConverter
#2、在自定义的类中，重写regex，也就是正则表达式
#3、将自定义的类，映射到app.url_map.converters上

#to_python的作用
#这个方法的返回值，将会传递到view函数中作为参数。
#
#to_url的作用
#这个方法的返回值，将会调用url_for函数的时候生成符合要求的url形式。
#
#
