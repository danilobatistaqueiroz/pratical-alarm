from PyQt5 import QtCore, QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

  menus = []
  window = None

  def __init__(self, icon, parent=None, description="Pratical Alarm"):
    self.window = parent
    QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
    menu = QtWidgets.QMenu(parent)
    openAcction = menu.addAction("Open")
    openAcction.triggered.connect(self.open)
    exitAcction = menu.addAction("Exit")
    exitAcction.triggered.connect(self.exit)
    self.setContextMenu(menu)
    self.setToolTip(description)

  def add_item(self,parent,text,event):
    menu = QtWidgets.QMenu(parent)
    menu.addAction(text)
    self.menus.append(menu)
    self.setContextMenu(menu)
    menu.triggered.connect(self.exit)

  def exit(self):
    QtCore.QCoreApplication.exit()

  def open(self):
    self.window.show()

  def exit_window(self):
    pass

def show_tray():
  w = QtWidgets.QWidget()
  trayIcon = SystemTrayIcon(QtGui.QIcon(r'assets/app.ico'), w)
  trayIcon.show()