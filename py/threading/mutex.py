# Mutual exclusion 互斥锁

from threading import Thread,Lock
import time
n = 100

def task():
    global n
    mutex.acquire() #上锁
    temp = n
    time.sleep(0.1)
    n = temp - 1
    print('success, %d'%n)
    mutex.release() #释放锁

if __name__ == '__main__':
    mutex = Lock()
    list_t = []
    for i in range(10):
        t = Thread(target=task)
        list_t.append(t)
        t.start()
    for t in list_t:
        t.join()