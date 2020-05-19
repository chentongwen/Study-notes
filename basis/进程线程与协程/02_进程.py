'''
- 单核CPU实现多任务原理:操作系统轮流让各个任务交替执行。

- 多核CPU实现多任务原理:真正的秉性执行多任务只能在多核CPU上实现，但是由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

- 并发和并行
    - **并发**：当有多个线程在操作时，如果系统只有一个cpu，则它根本不可能真正同时进行一个以上的线程，他只能把cpu运行时间划分成若干个时间段，再将时间段分配给各个线程执行，在一个时间段的线程代码运行时，其他线程处于挂起状态，这种方式我们称之为并发（Concurrent）
    - **并行**：当系统有一个以上cpu时，则线程的操作有可能非并发。当一个cpu执行一个线程时，另一个cpu可以执行另一个线程，两个线程互不抢占cpu资源，可以同时进行，这种方式我们称之为并行（Parallel）.


- 实现多任务的方式：
    - 多进程模式：
    - 多线程模式：
    - 协程
一个进程可以包含多个线程，一个线程可以包含多个协程


二丶多进程
进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础。
在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向对象的线程设计的计算机结构中，进程是线程的容器，程序是指令、数据及组织形势的描述，进程是程序的实体。
    - 优点：
        稳定性高，一个进程崩溃了，不会影响其他进程。
    - 缺点：
        创建进程开销巨大
        操作系统能同时运行进程数目有限。


1、进程创建
在linux下可以使用fork函数创建进程，在windows系统上可以引入multiprocessing模块，创建进程。我们可以使用multiprocessing模块中Process类创建新的进程。

    from multiorocessing import Process
    process=Process(target=函数，name=进程的名字，args=（给函数传递的参数）)
    process 对象

    对象调用方法：
    process.start()  启动进程并执行任务
    process.run()    只是执行了任务但是没有启动进程
    terminate()      终止

'''
import os
from multiprocessing import Process
from time import sleep
#进程的创建
def task1(s,name):
    while True:
        sleep(s)
        print ('任务1-------------',os.getpid(),'-------',os.getppid(),name)

def task2(s,name):
    while True:
        sleep(s)
        print('任务2*****************',os.getpid(),'-------',os.getppid(),name)
number=1
if __name__ == "__main__":
    #子进程
    p=Process(target=task1,name='one',args=(1,"aa"))
    p.start()
    print (p.name)
    p1=Process(target=task2,name='two',args=(2,'bb'))
    p1.start()
    print(p1.name)
    while True:
        number +=1
        sleep(0.2)
        if number==100:
            p.terminate()
            p1.terminate()
            break
        else:
            print ('=============>',number)

    print ('--------------')
    print ('**************')

    # 传参 args