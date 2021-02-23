from multiprocessing import Pool
import os,time

def task(name):
    print('子进程 %s 执行 task %s ...'%(os.getpid(),name))
    time.sleep(1)

if __name__ == '__main__':
    print('父进程 (%s) '%os.getpid())
    p = Pool(3) #定义一个进程池，最大进程数为3
    for i in range(10):
        p.apply_async(task,args=(i,))
    print('等待所有子进程结束')
    p.close()   #关闭进程池，关闭后p不再接受新的请求
    p.join()    #等待子进程结束
    print('所有子进程结束')