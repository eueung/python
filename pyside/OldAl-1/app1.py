import sys
from PySide.QtGui import QMainWindow, QPushButton, QApplication
from ui_quitter import Ui_MainWindow
#----------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
#----------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
#----------------------------------
