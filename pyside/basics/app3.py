import sys
#--------------------------------------
from PySide.QtGui import QApplication, QLabel
#--------------------------------------
app = QApplication(sys.argv)
label = QLabel("<font color=red size=40>Hello World</font>")
label.show()
#--------------------------------------
app.exec_()
sys.exit()
#--------------------------------------