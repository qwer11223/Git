from multiprocessing import Process
import time
import os


class SubProcess(Process):  # 继承Process类
    def __init__(self, interval, name=''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    def run(self):  # 重写 Process 类中的 run() 方法
        print('子进程 (%s) 开始执行，父进程为 (%s)' % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_end = time.time()
        print('子进程 (%s) 执行时间为 %0.2f秒' % (os.getpid(), t_end-t_start))


if __name__ == '__main__':
    print('-'*5, '父进程开始执行', '-'*5)
    print('父进程 PID: %s' % os.getpid())

    p1 = SubProcess(1, 'mrsoft')
    p2 = SubProcess(2)
    p3 = SubProcess(3)

    p1.start()
    p2.start()
    p3.start()

    # 同时父进程仍然往下执行，如果 p2 进程还在执行，将返回 true
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())
    print('p3.is_alive=%s' % p3.is_alive())

    # 输出p1,p2进程的别名和pid
    print('p1.name=%s' % p1.name)
    print('p1.pid=%s' % p1.pid)

    print('p2.name=%s' % p2.name)
    print('p2.pid=%s' % p2.pid)

    print('p3.name=%s' % p3.name)
    print('p3.pid=%s' % p3.pid)

    print('-----等待子线程-----')
    p1.join()  # join([timeout])
    p2.join()  # 等待进程实例执行结束
    p3.join()

    time.sleep(1)
    print('-----父进程执行结束-----')
