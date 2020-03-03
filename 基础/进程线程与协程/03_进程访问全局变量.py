'''
多进程对于全局变量访问，在每个全局变量里面都放一个m变量，
保证每个进程访问变量互不干扰

m=1 #不可变类型
list1=[] #可变类型
运算类的才会用进程去做
下载是耗时类的一般用线程。
'''
import os
from multiprocessing import Process
from time import sleep
#进程的创建


m=1 #不可变类型
list1=[] #可变类型

def task1(s,name):
    global m
    while True:
        sleep(s)
        m+=1
        list1.append(str(m)+'task1')
        print ('任务1-------------',m,list1)
def task2(s,name):
    global m
    while True:
        sleep(s)
        m+=1
        list1.append(str(m) + 'task2')
        print('任务2*****************',m,list1)
number=1
if __name__ == "__main__":
    #子进程
    p=Process(target=task1,name='one',args=(1,"aa"))
    p.start()

    p1=Process(target=task2,name='two',args=(2,'bb'))
    p1.start()

    while True:
        sleep(3)
        m+=1
        list1.append(str(m) + 'task主')
        print ('##########main:',m)
    # 传参 args
    # 传参 args