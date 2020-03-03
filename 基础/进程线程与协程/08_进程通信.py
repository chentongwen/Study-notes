# 进程通信
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['A.jpg', 'B.jpg', 'C.jpg']
    for image in images:
        print('正在下载', image)
        sleep(1)
        q.put(image)


def saveFile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print('{0}保存成功'.format(file))
        except:
            print('队列中值null，全部保存完毕！！')
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=saveFile, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print('进程执行完毕')