'''
生产者与消费者：两个线程之间的通信

Python的queue模块中提供了同步的，线程安全的队列类，包括FIFO(先入先出)队列Queue，
LIFO（后入先出）队列LifoQueue和优先级队列PriorityQueue.这些队列都实现了锁原理（
可以理解为原子操作，即要么不做，要么就做完），能够在多线程中直接使用。
可以使用队列来实现线程同步。

'''
import threading
import queue
from time import sleep
import random


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据:{0}'.format(num))
        print('生产者产生数据:{0}'.format(num))
        sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到：{0}'.format(item))
        sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    #创建生产者
    t1 = threading.Thread(target=produce, args=(q,))
    t1.start()
    # 创建消费者
    t2 = threading.Thread(target=consume, args=(q,))
    t2.start()

    t1.join()
    t2.join()
    print('END')

'''
总结：
    A、创建线程
        t=thread(target=func,name='',args=(),kwargs={})新建状态
        t.start() ------>就绪状态
        run()
        join()
    B、自定义线程
        class myThread(Thread):
            def __init__(self.name):
                super().__init__()
                self.name=name
            def run(self):
                任务
        t=myThread('name')
        t.start()
    C、数据共享
        进程共享数据与线程共享数据区别：
        进程是每个进程中都有一份
        线程是共同一个数据--------》数据安全性问题
        
        GIL ---------》伪线程
        
        lock=Lock()
        lock.acquire()
        .........
        lock.release()
        
        ------->只要使用锁，死锁
        避免死锁
        
    D、线程间通信：生产者与消费者
    生产者：线程
    消费者：线程
    import queue
    
    q=queue.Queue()
    #创建生产者
    t1 = threading.Thread(target=produce, args=(q,))
    t1.start()
    # 创建消费者
    t2 = threading.Thread(target=consume, args=(q,))
    t2.start()
    
    GIL扩展
    
'''
