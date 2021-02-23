#-*- conding:utf-8 -*-

import socket   #导入socket模块
host = '127.0.0.1'
port = 8080
web = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建socket对象，internet进程间通信，tcp协议
web.bind((host,port))   #绑定端口
web.listen(5)   #设置最多连接数
print('Waiting for client connection...')

while 1:
    conn,addr = web.accept() #被动接受tcp客户端连接
    print(conn,addr)    #获取客户端请求数据
    data = conn.recv(1024)  #打印接收到的数据
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello World')
    conn.close()