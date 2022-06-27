from PyQt5.QtWidgets import QPushButton, QRadioButton, QWidget, QStyleFactory
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
from darkmode import dark_mode, light_mode

class FormWidget(QWidget):
  def __init__(self, parent, app):
    super(FormWidget, self).__init__(parent)
    self.UiComponents(parent, app)

  def UiComponents(self, parent, app):

    self.rb_dark = QRadioButton("Dark", self)
    self.rb_dark.setGeometry(30, 10, 80, 40) #left top width height
    self.rb_dark.clicked.connect(lambda:dark_mode(app))

    self.rb_light = QRadioButton("Light", self)
    self.rb_light.setGeometry(30, 40, 80, 40) #left top width height
    self.rb_light.clicked.connect(lambda:light_mode(app))

    self.button = QPushButton('Ok', self)
    self.button.setGeometry(150, 50, 80, 30)
    self.button.clicked.connect(lambda:parent.close())


class SettingsWindow(QMainWindow):
  def __init__(self):
    super().__init__()

  def createUI(self,main_window,app):
    self.setGeometry((main_window.width()/2)+main_window.x()-(self.width()/5), main_window.y()+(main_window.height()/3), 250, 100) #left top width height
    self.setWindowTitle("Settings")
    self.setStyle(QStyleFactory.create("Fusion"))
    self.setWindowIcon(QtGui.QIcon('assets/tray.png'))
    self.form_widget = FormWidget(self,app)
    self.setCentralWidget(self.form_widget)
    self.setWindowFlags(
        QtCore.Qt.Window |
        QtCore.Qt.CustomizeWindowHint |
        QtCore.Qt.WindowTitleHint |
        QtCore.Qt.WindowCloseButtonHint |
        QtCore.Qt.WindowStaysOnTopHint
        )