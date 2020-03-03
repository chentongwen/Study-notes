import threading
'''
采用
    进程：计算密集型
    线程：耗时操作，下载、爬虫、io
线程是可以共享全局变量

python底层只要用线程默认加锁GIL

GIL  全局解释器锁
'''
money = 1000


def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


if __name__ == '__main__':
    th1 = threading.Thread(target=run1, name='th1')
    th2 = threading.Thread(target=run2, name='th2')
    # 启动
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('money:', money)
