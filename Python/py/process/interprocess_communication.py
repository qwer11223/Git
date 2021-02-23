# 使用队列在进程中通信

from multiprocessing import Process,Queue
import time

# 向队列中写入数据
def writeTask(q):
    if not q.full():
        for i in range(5):
            msg = '消息' + str(i)
            q.put(msg)
            print('写入：%s'%msg)

# 从队列中读取数据
def readTask(q):
    time.sleep(1)
    while not q.empty():
        print('读取：%s'%q.get(True,2)) #等待2秒，如果还未读到任何消息，则抛出 Queue.Empty 异常

if __name__ == '__main__':
    print('---父进程开始---')
    q = Queue()
    pw = Process(target=writeTask,args=(q,))
    pr = Process(target=readTask,args=(q,))
    pw.start()
    pr.start()
    pw.join()   #等待pw结束
    pr.join()
    print('---父进程结束---')