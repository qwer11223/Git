import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):  # 创建MainWindow 窗口
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)  # 初始化窗口
        self.resize(800, 600)  # 改变客户区的面积
        self.center()  # 自定义函数，将窗口放在屏幕中间
        self.status = self.statusBar()  # 获得状态栏对象
        self.status.showMessage('这是状态栏提示,停留5s', 5000)  # 显示状态栏信息，停留5秒
        self.setWindowTitle('PyQt MainWindow example')  # 设置窗口标题

        self.button1 = QPushButton('Close Window')
        self.button1.clicked.connect(self.onButtonClick)
        
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def center(self):
        screen = QDesktopWidget().screenGeometry()  # 获取屏幕大小
        size = self.geometry()  # 获取窗口大小
        self.move((screen.width()-size.width())/2,
                  (screen.height()-size.height())/2)  # 将窗口移动到屏幕中间

    def onButtonClick(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text()+' pressed')
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./c.ico'))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
