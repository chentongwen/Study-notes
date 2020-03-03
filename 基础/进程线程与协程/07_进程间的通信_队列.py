'''
进程间通信：队列（queue）

put()  如果队列满了则只能等待，除非有'空地'则添加成功
full() 判断队列是否满
empty()  判断队列是否是空的
get()   取出队列数据
qsize()  打印队列长度
'''
from multiprocessing import Queue


q = Queue(5)
q.put('A')
put = q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())

if not q.full():
    q.put('F', timeout=2)
else:
    print('队列满')

# 取出队列值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
if q.empty():
    print('队列空')
else:
    print(q.get(timeout=2))

# 思考：
# q.put_nowait()
# q.get_nowait()
