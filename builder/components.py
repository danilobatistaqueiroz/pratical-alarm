from PyQt5.QtWidgets import QPushButton, QTextEdit
from pydub.playback import play
from pydub import AudioSegment
import threading
from PyQt5 import QtCore, QtGui
from notifier import show_notification
import datetime
from hours import *
from alarms import set_alarm
import dialog

def UiComponents(self, parent):

  buttonV = None

  def click():
    sound = AudioSegment.from_file('assets/click.mp3')
    threading.Thread(target=play, args=(sound,), daemon=True).start()
    buttonV.setFocus()

  button = QPushButton('+30seg', self)
  button.setGeometry(50, 20, 100, 40)
  def bt_clicked():
    self.text.setText(add_sec(self.text.toPlainText(),30))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('+1min', self)
  button.setGeometry(180, 20, 100, 40)
  def bt_clicked():
    self.text.setText(add_min(self.text.toPlainText(),1))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('+10min', self)
  button.setGeometry(310, 20, 100, 40)
  def bt_clicked():
    self.text.setText(add_min(self.text.toPlainText(),10))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('+1h', self)
  button.setGeometry(50, 80, 100, 40)
  def bt_clicked():
    self.text.setText(add_hour(self.text.toPlainText(),1))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('+4hs', self)
  button.setGeometry(180, 80, 100, 40)
  def bt_clicked():
    self.text.setText(add_hour(self.text.toPlainText(),4))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('+8hs', self)
  button.setGeometry(310, 80, 100, 40)
  def bt_clicked():
    self.text.setText(add_hour(self.text.toPlainText(),8))
    self.text.setAlignment(QtCore.Qt.AlignCenter)
    click()
  button.clicked.connect(bt_clicked)

  button = QPushButton('X', self)
  button.setGeometry(66, 153, 50, 62) #left top width height
  custom_font = QtGui.QFont("Courier", 35, QtGui.QFont.Bold)
  button.setAttribute(QtCore.Qt.WA_TranslucentBackground)
  button.setStyleSheet("background-color : #9f0000; color : rgb(255,255,255)")
  button.setFont(custom_font)
  def bt_clicked():
      sound = AudioSegment.from_file('assets/sweep.wav')
      threading.Thread(target=play, args=(sound,), daemon=True).start()
      text.setText(add_time(datetime.datetime.now(),0,0,0))
      text.setAlignment(QtCore.Qt.AlignCenter)
  button.clicked.connect(bt_clicked)

  self.text = QTextEdit(datetime.datetime.now().strftime("%H:%M:%S"), self)
  text = self.text
  text.setGeometry(136, 150, 180, 70) #left top width height
  text.setAlignment(QtCore.Qt.AlignCenter)
  custom_font = QtGui.QFont("Times", 30, QtGui.QFont.Bold)
  text.setFont(custom_font)

  buttonV = QPushButton('V', self)
  buttonV.setGeometry(336, 153, 50, 62) #left top width height
  custom_font = QtGui.QFont("Courier", 35, QtGui.QFont.Bold)
  buttonV.setStyleSheet("background-color : #065f8e")
  buttonV.setFont(custom_font)
  buttonV.setAutoDefault(True)
  buttonV.setDefault(True)
  buttonV.setFocus()
  def bt_clicked():
      ret = dialog.show_dialog(parent)
      if ret['status'] == True:
        show_notification(f"scheduled - {text.toPlainText()} - {ret['text']}")
        parent.iconify(f"scheduled - {text.toPlainText()} - {ret['text']}")
        set_alarm(text.toPlainText(),ret['text'])
  buttonV.clicked.connect(bt_clicked)