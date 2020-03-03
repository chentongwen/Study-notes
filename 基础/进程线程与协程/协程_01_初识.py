'''
协程：微线程
协程：耗时操作
耗时操作：网络请求，网络下载（爬虫），IO，文件的读写，阻塞
进程>线程>协程
Process Thread  生成器完成
目的：高效的利用CPU
生成器：yield

greenlet：完成协程切换任务

gevent:
Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。
gevent是第三方库，通过greenlet实现协程，其基本思想是：
    当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
    由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：

猴子补丁
from gevent import monkey

monkey.patch_all()
'''
import time

import gevent
from gevent import monkey

monkey.patch_all()


def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


def c():
    for i in range(5):
        print('c' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()
    print('END')
