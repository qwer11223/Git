import socket
host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print('等待连接...')
sock, addr = s.accept()
print('连接已建立')
info = sock.recv(1024).decode()
while info != 'bye':
    if info:
        print('接收到的内容：', info)
        send_data = input('输入发送内容：')
        sock.send(send_data.encode())
        if send_data == 'bye':
            break
        info = sock.recv(1024).decode()
sock.close()
s.close()
