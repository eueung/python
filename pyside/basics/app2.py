from PySide.QtGui import QApplication, QPushButton
#--------------------------------------
app = QApplication([])
#--------------------------------------
button = QPushButton('Exit')
button.clicked.connect(app.exit)
button.show()
#--------------------------------------
app.exec_()
#--------------------------------------
