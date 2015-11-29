import sys
import platform
import PySide
from PySide.QtGui import (QApplication, QMainWindow, QMessageBox, QIcon)
#------------------------------------------------------
__version__ = '3.1.5'
from ui_combine import Ui_MainWindow as Ui
import qrc_combine
#------------------------------------------------------   
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Store Ui() as class variable self.ui
        self.ui = Ui()
        self.ui.setupUi(self)
        self.setWindowTitle('Combine Code Blocks.')        
        self.ui.actionShow_CCPL.triggered.connect(self.showCCPL)
        self.ui.action_About.triggered.connect(self.about)        
        iconToolBar = self.addToolBar("iconBar.png") 
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        self.ui.actionShow_CCPL.setIcon(QIcon(":/showgpl.png"))
        self.ui.action_About.setIcon(QIcon(":/about.png"))
        self.ui.action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        self.ui.actionShow_CCPL.setStatusTip("Show CC Licence")
        self.ui.action_About.setStatusTip("Pop up the About dialog.")
        self.ui.action_Close.setStatusTip("Close the program.")
#------------------------------------------------------        
        iconToolBar.addAction(self.ui.actionShow_CCPL)
        iconToolBar.addAction(self.ui.action_About)
        iconToolBar.addAction(self.ui.action_Close)

    def showCCPL(self):
        with open('CCPL.txt') as fi:                  
            self.ui.textEdit.setText(fi.read())        
        
    def about(self):
        QMessageBox.about(self, "About PySide, Platform and the like",
                """<b> about.py version %s </b> 
                <p>Copyright &copy; 2013 by Algis Kabaila. This work is made available under  the terms of
                Creative Commons Attribution-ShareAlike 3.0 license, http://creativecommons.org/licenses/by-sa/3.0/.
                <p>This application is useful for displaying Qt version and other details.
                <p>Python %s -  PySide version %s - Qt version %s on %s""" %
                (__version__, platform.python_version(), PySide.__version__, PySide.QtCore.__version__, platform.system()))                        
#------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
#------------------------------------------------------