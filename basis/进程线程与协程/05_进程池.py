'''
   当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，
   但如果是上百甚至上千个目标,手动的去创建进程的工作量巨大，此事就可以用到multiprocessing模块提供的Pool方法。
   初始化Pool时，可以指定一个最大的进程数，当有新的请求提交到Pool中时，如果池还没有满，
   那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，
   直到池中有进程结束，才会创建新的进程来执行。

pool
    阻塞式：
    非阻塞式：全部添加到队列中，立刻返回，并没有其他的进程执行完毕，但是回调函数是等待任务完成之后才调用。
'''

from multiprocessing import Pool
import time
from random import random
import os


# 非阻塞式


def task(task_name):
    print('开始任务：', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random() * 2)
    end = time.time()
    return '完成任务：{0}，用时：{1}，进程id：{2}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['打游戏', '洗澡', '看电视', '唱歌', '看书', '打球', '吃饭', '跑步', '跳绳', '健身']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)
    pool.close()
    pool.join()  # 主进程的挡板，使主进程等待进程池内的任务完成，再进行下一步。
    for i in container:
        print(i)
    print('over!!!!!')


