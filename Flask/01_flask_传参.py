from flask import Flask,request
import uuid

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#url传参
#传递参数的语法是：‘/<参数名>/’。然后再视图函数中，也要定义同名的参数。

@app.route('/a/<id>/')
def article(id):
    return '您请求的文章是{0}'.format(id)

#指定传递参数的数据类型

##1、如果没有指定具体的数据类型，那么默认使用string
##2、int数据类型只能传递int类型
##3、float数据类型只能传递float类型
##4、path数据类型和string类型有点类似，都是可以接受任意的字符串，但是path可以接收路径，也就是说包含/.
##5、uuid数据类型只能接收符合uuid的字符串。uuid是一个全宇宙都唯一的字符串，一般可以用来作为表的主键。
##6、any数据类型可以在一个url中指定多个路径。

#接收用户传递的参数
#第一种：使用path的形式（将参数嵌入到路径中），就是上面讲的。
#第二种：使用查询字符串的方式，就是通过“?key=value”的形式传递的。

#整型：int
@app.route('/1/<int:types>/')
def types_int(types):
    return '整型:%d' % types
#string
@app.route('/2/<string:types>/')
def types_str(types):
    return '字符串型:%s' % types  #默认是字符串类型

#float
@app.route('/3/<float:types>/')
def types_float(types):
    return 'float:{0}'.format(types)

#path
@app.route('/4/<path:types>/')
def types_path(types):
    return 'path:{0}'.format(types)

#uuid
@app.route('/6/<uuid:types>/')
def types_uuid(types):
    return 'uuid:{0}'.format(types)
# print (uuid.uuid4())

#any
@app.route('/7/<any(blog,user):url_path>/<id>/')
def types_any(url_path,id):
    if url_path == 'blog':
        return '博客详情:{0}'.format(id)
    else:
        return '用户详情：{0}'.format(id)


##以?的方式传递参数
@app.route('/d/')
def d():
    wd=request.args.get('wd')
    ie=request.args.get('ie')
    print('ie:%s'%ie)
    return '您通过查询字符串的方式传递的参数是:%s' % wd

if __name__ == '__main__':
    app.run(debug=True)
