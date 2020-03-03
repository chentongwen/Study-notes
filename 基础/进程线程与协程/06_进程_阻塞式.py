from multiprocessing import Pool
import time
from random import random
import os


# 阻塞式:添加一个执行一个，如果一个任务不结束另一个任务就进不来。


def task(task_name):
    print('开始任务：', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务：{0}，用时：{1}，进程id：{2}'.format(task_name, (end - start), os.getpid()))
    # return '完成任务：{0}，用时：{1}，进程id：{2}'.format(task_name, (end - start), os.getpid())

#
# container = []
#
#
# def callback_func(n):
#     container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['打游戏', '洗澡', '看电视', '唱歌', '看书', '打球', '吃饭', '跑步', '跳绳', '健身']
    for task1 in tasks:
        pool.apply(task, args=(task1,))
    pool.close()
    pool.join()  # 主进程的挡板，使主进程等待进程池内的任务完成，再进行下一步。
    # for i in container:
    #     print(i)
    # print('over!!!!!')
'''
进程池：
    pool=Pool(max) 创建进程池对象
    pool.apply() 阻塞的
    pool.apply_async()  非阻塞的
    
    pool.close()
    pool.join() 让主进程让步
'''