from PySide.QtGui import QApplication, QPushButton, QColorDialog, QMessageBox
#--------------------------------------
class ButtonPainter(object):
  def __init__(self, button):
    self.button = button

  def choose_color(self):
    color  = QColorDialog().getColor()
    
    if color.isValid():
        self.button.setStyleSheet(u'background-color:' + color.name())
    else:
        msgbox = QMessageBox()
        msgbox.setWindowTitle(u'No Color was Selected')
        msgbox.exec_()
#--------------------------------------
app = QApplication([])
#--------------------------------------  
button = QPushButton('Choose Color')
button_painter = ButtonPainter(button)
button.clicked.connect(button_painter.choose_color)
button.show()
#--------------------------------------
app.exec_()
#--------------------------------------