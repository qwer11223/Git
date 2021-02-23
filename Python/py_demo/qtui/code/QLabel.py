from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 1 初始化标签
        label1.setText('font label')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI 应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('This is a pic label')
        label3.setPixmap(QPixmap("./images/default.jpg"))

        label4.setText("<a href='https://www.baidu.com'>cloud</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('This is a href')

        # 2 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec())
