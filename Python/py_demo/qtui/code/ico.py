#coding:utf-8
import sys
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip

class Icon(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300,300,250,150)
        self.setWindowIcon(QIcon("./images/ico.ico"))

        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Tip</b>')

app = QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec())