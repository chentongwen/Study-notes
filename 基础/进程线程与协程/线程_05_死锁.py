'''
死锁
    -开发过程中使用线程，在线程间共享多个资源的时候，
    如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
    -尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不会做任何事情。
避免出现死锁：
    解决：
    1、重构代码
    2、设置超时 
'''
from threading import Thread, Lock
import time

lockA = Lock()
lockB = Lock()


class myThread1(Thread):
    def run(self):
        if lockA.acquire(timeout=5):
            print(self.name + '获取到A锁')
            time.sleep(0.1)
            if lockB.acquire(timeout=5):
                print(self.name + '获取到B锁\n已经获取A+B锁')
                lockB.release()
            lockA.release()


class myThread2(Thread):
    def run(self):
        if lockB.acquire(timeout=5):
            print(self.name + '获取到B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '获取到A锁\n已经获取A+B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = myThread1()
    t2 = myThread2()

    t1.start()
    t2.start()
