#多进程队列的使用

from multiprocessing import Queue

if __name__ == '__main__':
    q=Queue(3) #初始化一个Queue对象，最多可接受3条put信息
    q.put('message1')
    q.put('message2')
    print(q.full())   #false
    q.put('message3')
    print(q.full())   #true

    try:
        q.put('message4',True,2)
    except:
        print('消息队列已满，现有消息数量：%s'%q.qsize())

    try:
        q.put_nowait('message4') #相当于 q.put('message4',False)
    except:
        print('消息队列已满，现有消息数量：%s'%q.qsize())

    #先判断消息队列是否为空，再读取消息
    if not q.empty():
        print('---从队列中读取消息---')
        for i in range(q.qsize()):
            print(q.get_nowait())
        
    if not q.full():
        q.put_nowait('message4')
