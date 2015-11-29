import sys
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton
from ui_licence import Ui_MainWindow
#----------------------------------
__version__ = '3.3.0'
#----------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showButton.clicked.connect(self.fileRead)
        
    def fileRead(self):
        '''Read and display licence.'''
        with open('CCPL.txt') as nonamefile:
            self.textEdit.setText(nonamefile.read())
#----------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
#----------------------------------