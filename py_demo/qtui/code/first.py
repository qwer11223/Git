#coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)    #创建一个app对象
window = QWidget()  #QWidget基类，创建一个窗口控件
window.resize(300,200)  #改变窗口控件大小
window.move(250,150)    #设置窗口初始化位置
window.setWindowTitle('first window')   #设置窗口控件标题
window.show()   #将窗口空间显示在桌面上
exec_ = app.exec_() #进入程序主循环
sys.exit(exec_) #完整结束程序