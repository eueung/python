from PySide.QtGui import QApplication, QLabel
#--------------------------------------
app = QApplication([])
#--------------------------------------
window = QLabel('Window from label')
window.show()
#--------------------------------------
app.exec_()
#--------------------------------------
