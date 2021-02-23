from multiprocessing import Process
import time
import os


def child1(interval):
    print('子进程 (%s) 开始执行，父进程为 (%s)' % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print('子进程 (%s) 执行时间为 %0.2f秒' % (os.getpid(), t_end-t_start))


def child2(interval):
    print('子进程 (%s) 开始执行，父进程为 (%s)' % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print('子进程 (%s) 执行时间为 %0.2f秒' % (os.getpid(), t_end-t_start))


if __name__ == '__main__':
    print('-----父进程开始执行-----')
    print('父进程PID: %s' % os.getpid())  # 输出当前程序的 ID
    p1 = Process(target=child1, args=(1,))  # 实例化进程 p1
    p2 = Process(target=child2, name='mrsoft', args=(2,))  # 实例化进程 p2
    p1.start()  # 启动进程 p1
    p2.start()

    # 同时父进程仍然往下执行，如果 p2 进程还在执行，将返回 true
    print('p1.is_alive=%s' % p1.is_alive())
    print('p2.is_alive=%s' % p2.is_alive())

    # 输出p1,p2进程的别名和pid
    print('p1.name=%s' % p1.name)
    print('p1.pid=%s' % p1.pid)

    print('p2.name=%s' % p2.name)
    print('p2.pid=%s' % p2.pid)

    print('-----等待子线程-----')
    p1.join()   #join([timeout])
    p2.join()   #等待进程实例执行结束

    time.sleep(1)
    print('-----父进程执行结束-----')
