from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_mainui import Ui_MainWindow


class LayoutDemo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)

    #@pyqtSlot()
    def click(self):
        print('s_min:', self.doubleSpinBox.text())
        print('s_max', self.doubleSpinBox_2.text())
        print('h_min:',self.doubleSpinBox_3.text())
        print('h_max:',self.doubleSpinBox_4.text())
        print('sharp_min:',self.doubleSpinBox_5.text())
        print('sharp_max:',self.doubleSpinBox_6.text())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
