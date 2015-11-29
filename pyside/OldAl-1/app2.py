import sys
import platform
#----------------------------------
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton, QMessageBox
#----------------------------------
from ui_about import Ui_MainWindow
#----------------------------------
__version__ = '0.0.1'
#----------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.aboutButton.clicked.connect(self.about)
    #----------------------------------
    def about(self):
        QMessageBox.about(self, "About PySide, Platform and the like",
        """<b>Platform Details</b> v {}
        <p>Copyright &copy; 2010 Joe Bloggs.
        All rights reserved in accordance with
        GPL v2 or later - NO WARRANTIES!
        <p>This application can be used for
        displaying platform details.
        <p>Python {} - PySide version {} - Qt version {} on {}""".format(__version__,
        platform.python_version(), PySide.__version__, PySide.QtCore.__version__,
        platform.system()))
#----------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
#----------------------------------
