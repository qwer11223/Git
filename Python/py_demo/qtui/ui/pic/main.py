import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_pic import Ui_Form

class MyMain(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMain()
    ui.show()
    sys.exit(app.exec_())
