import threading
'''
GIL  全局解释器锁

python底层只要用线程默认加锁GIL
当运算量比较大的时候，GIL锁会自动释放，就会涉及到数据不安全。
'''
n = 0


def task1():
    global n
    for i in range(1000000):
        n += 1
    print('task1中n的值是：', n)


def task2():
    global n
    for i in range(1000000):
        n += 1
    print('task2中n的值是：', n)


if __name__ == '__main__':
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print('最终N值：', n)
