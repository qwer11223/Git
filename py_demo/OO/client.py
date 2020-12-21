import sys
import socket,threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.Ui_client import Ui_MainWindow


class Tcp(QThread):

    connect_ = pyqtSignal(str)  # 创建信号
    update_date = pyqtSignal(str)
    send_signal = pyqtSignal(str)


    def __init__(self,main_):
        super().__init__()  # 调用父类初始化方法
        main_.send_.connect(self.send_text)

        self.e = threading.Event()
        self.text_data = ''

    def run(self):  # 重载run
        host = socket.gethostname()
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP套接字
        s.connect((host,port))
        print('连接已建立...')
        self.connect_.emit('连接已建立')  # 发射信号
        info = ''
        while 1:
            self.e.wait()   #等待set()
            self.e.clear()  #重置
            send_data = self.text_data
            self.send_signal.emit(send_data)
            print('send:',send_data)
            s.send(send_data.encode())  # 编码为二进制数据
            info = s.recv(1024).decode()
            print('receive:', info)
            self.update_date.emit(info)
        s.close()

    def send_text(self,str1):
        self.text_data = str1
        self.e.set()


class MainWindow(QMainWindow, Ui_MainWindow):

    send_ = pyqtSignal(str)

    def __init__(self):
        super(MainWindow, self).__init__()  # 初始化窗口
        self.setupUi(self)  # 绘制Ui

        self.net = Tcp(self)

        self.send_btn.clicked.connect(self.send)
        self.net.connect_.connect(self.connectSuccess)
        self.net.update_date.connect(self.recv_)
        self.net.send_signal.connect(self.res)

        self.net.start()

    def send(self):
        text = self.textEdit.toPlainText()
        self.send_.emit(text)
        self.textEdit.clear()

    def connectSuccess(self, msg):
        data = '<p style="text-align: center;color: #ccc;font-size: 16px;">'+msg+'</p>'
        self.textShow.append(data)

    def res(self,msg):
        data = '<p align="left" style=";color: #f00;font-size: 20px;font-size:blod;">client:</p>'
        self.textShow.append(data)
        data = '<p align="left" style=";color: #000;font-size: 16px;">'+msg+'</p>'
        self.textShow.append(data)

    def recv_(self,msg):
        data = '<p align="right" style=";color: #0f0;font-size: 20px;font-size:blod;">server:</p>'
        self.textShow.append(data)
        data = '<p align="right" style=";color: #000;font-size: 16px;">'+msg+'</p>'
        self.textShow.append(data)

# ------------ main -----------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
