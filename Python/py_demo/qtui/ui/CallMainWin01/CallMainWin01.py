import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from Ui_mainForm import Ui_MainWindow
from Ui_ChildrenForm import Ui_Form

class MainForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)

        self.child = ChildrenForm() #生成子窗口实例

        self.actionopen.triggered.connect(self.open)
        self.actionclose.triggered.connect(self.close)

        self.addWinAction.triggered.connect(self.childShow)

    def open(self):
        file,ok = QFileDialog.getOpenFileName(self,'打开','C://','AllFiles (*);;Text Files (*.txt)')
        self.statusBar.showMessage(file)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

class ChildrenForm(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainForm()
    ui.show()
    sys.exit(app.exec_())
