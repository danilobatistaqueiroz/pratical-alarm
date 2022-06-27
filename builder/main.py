#!/usr/bin/env python3
# coding=utf-8

from PyQt5.QtWidgets import (
  QApplication,
  QMainWindow,
  QWidget,
  QMessageBox,
  QAction,
  QStyleFactory,
  QMessageBox
)
from PyQt5 import QtGui
import PyQt5
import sys
from settings import SettingsWindow
from tray import SystemTrayIcon
import components
from darkmode import load_settings

from PyQt5.QtWidgets import QAction


trayIcon = None
main_window = None

class FormWidget(QWidget):
  def __init__(self, parent, app):
    super(FormWidget, self).__init__(parent)
    load_settings(app)
    self.UiComponents(parent)
  def UiComponents(self, parent):
    components.UiComponents(self, parent)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

  def createUI(self,app):
    self.setGeometry(400, 200, 470, 260) #left top width height
    self.setWindowTitle("Pratical Alarm")
    self.setStyle(QStyleFactory.create("Fusion"))
    self.setWindowIcon(QtGui.QIcon('assets/tray.png'))

    settings = QAction("Settings", self)
    settings.triggered.connect(lambda:self.open_settings(app))
    quit = QAction("Quit", self)
    quit.triggered.connect(self.exit_window)

    menubar = self.menuBar()
    fmenu = menubar.addMenu("File")
    fmenu.addAction(settings)
    fmenu.addAction(quit)

    self.form_widget = FormWidget(self, app)
    self.setCentralWidget(self.form_widget)


  def open_settings(self,app):
    self.settings = SettingsWindow()
    self.settings.createUI(self, app)
    self.settings.show()

  def closeEvent(self, event):
    close = QMessageBox()
    close.setWindowTitle("Close")
    close.setText("Do you want to exit?")
    close.setGeometry((self.width()/2)+self.x()-100, (self.y()+(self.height()/2)), 50, 50) #left top width height
    buttonoptionA = close.addButton("minimize", QMessageBox.YesRole)
    buttonoptionB = close.addButton("exit app", QMessageBox.NoRole)
    buttonoptionA.setDefault(True)
    buttonoptionA.setStyleSheet("background-color : #535353")
    buttonoptionB.setStyleSheet("background-color : #535353")
    close.setDefaultButton(buttonoptionA)
    close = close.exec()
    if close == 0:
      if isinstance(event,PyQt5.QtGui.QCloseEvent) == True:
        event.ignore()
        self.hide()
      else:
        event = True
      global trayIcon
      global main_window
      if trayIcon == None:
        trayIcon = SystemTrayIcon(QtGui.QIcon(r'assets/app.png'), self)
        trayIcon.show()
    elif close == 1:
      sys.exit()

  def exit_window(self, event):
    self.close()

  def iconify(self, description):
    self.hide()
    global trayIcon
    global main_window
    if trayIcon == None:
      trayIcon = SystemTrayIcon(QtGui.QIcon(r'assets/app.png'), self, description)
      trayIcon.show()

def main():
  app = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.createUI(app)

  main_window.show()

  sys.exit(app.exec_())

if __name__ == '__main__':
  main()