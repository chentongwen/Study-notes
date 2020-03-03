from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'Hello World!'
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'


if __name__ == '__main__':
    app.run(debug=True,port='9000')
#在局域网中让其他电脑访问我的网站：
    #修改host使别人能访问到项目
    #app.run(host="0.0.0.0")
#指定端口号：
    #Flask默认使用5000端口。替换端口app.run(debug=True,port=9000)
#URL唯一：
    #在定义url的时候，一定要记得在最后加一个斜杠。
        #1、如果不加斜杠，那么浏览器中访问这个url的时候，如果最后加了斜杠，那么久访问不到。这样用户的体验不太好。
        #2、搜如引擎会将不加斜杠的和加斜杠的视为两个不同的url。而其实加斜杠和不加斜杠的都是同一个url，那么就会给搜索引擎造成一个误解。
#get请求和post请求：
    #在网络请求中有许多请求方式，比如：get、post、delete、put请求等。那么最常用的就是get和post请求。
    #1、get请求：只会在服务器上获取资源，不会更改服务器状态。这种请求方式推荐使用get请求
    #2、post请求：会给服务器提交一些数据或者文件。一般post请求是会对服务器的状态产生影响，那么这种请求推荐使用post请求
    #3、关于参数传递
        #get请求：把参数放到url中，通过？xx=xx的形式传递的。因为会把参数放到url中，这样请求不太安全
        #post请求：把参数放到from data中。避免了被偷窥的风险。
    #4、在flask中，route方法，默认将只能使用GET的方式请求url,如果想要设置自己的请求方式，那么应该传递一个methods参数