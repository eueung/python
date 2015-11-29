from PySide.QtGui import QApplication, QPushButton, QColorDialog, QMessageBox, QPixmap
#--------------------------------------
def choose_color():
    color  = QColorDialog().getColor()
    
    msgbox = QMessageBox()
    if color.isValid():
        pixmap = QPixmap(50, 50)
        pixmap.fill(color)
        msgbox.setWindowTitle(u'Selected Color')
        msgbox.setIconPixmap(pixmap)
    else:
        msgbox.setWindowTitle(u'No Color was Selected')
    msgbox.exec_()
#--------------------------------------
app = QApplication([])
#--------------------------------------    
button = QPushButton('Choose Color')
button.clicked.connect(choose_color)
button.show()
#--------------------------------------
app.exec_()
#--------------------------------------