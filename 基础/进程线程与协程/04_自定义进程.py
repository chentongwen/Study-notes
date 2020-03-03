# 进程:自定义
from multiprocessing import Process


class myProcess(Process):
    def __init__(self, name):
        # Process.__init__(self)
        super(myProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            print('{0}----------->自定义进程,n:{1}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
    P = myProcess('小明')
    P.start()
    P1 = myProcess('小红')
    P1.start()
