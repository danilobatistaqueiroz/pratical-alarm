from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QSettings

def save_settings(mode):
  settings = QSettings('PraticalAlarm', 'pratical_alarm')
  settings.setValue('darkmode', mode )

def load_settings(app):
  settings = QSettings('PraticalAlarm', 'pratical_alarm')
  try:
      if settings.value('darkmode') == 'dark':
        dark_mode(app)
      else:
        light_mode(app)
  except:
      pass


def dark_mode(app):
  palette = QPalette()
  palette.setColor(QPalette.Window, QColor(53, 53, 53))
  palette.setColor(QPalette.WindowText, Qt.white)
  palette.setColor(QPalette.Base, QColor(25, 25, 25))
  palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
  palette.setColor(QPalette.ToolTipBase, Qt.black)
  palette.setColor(QPalette.ToolTipText, Qt.white)
  palette.setColor(QPalette.Text, Qt.white)
  palette.setColor(QPalette.Button, QColor(159, 00, 00))
  palette.setColor(QPalette.ButtonText, Qt.white)
  palette.setColor(QPalette.BrightText, Qt.red)
  palette.setColor(QPalette.Link, QColor(42, 130, 218))
  palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
  palette.setColor(QPalette.HighlightedText, Qt.black)
  app.setPalette(palette)
  save_settings("dark")

def light_mode(app):
  palette = QPalette()
  palette.setColor(QPalette.Window, QColor("#efefef"))
  palette.setColor(QPalette.WindowText, QColor("#000000"))
  palette.setColor(QPalette.Base, QColor("#ffffff"))
  palette.setColor(QPalette.AlternateBase, QColor("#f7f7f7"))
  palette.setColor(QPalette.ToolTipBase, QColor("#ffffdc"))
  palette.setColor(QPalette.ToolTipText, QColor("#000000"))
  palette.setColor(QPalette.Text, QColor("#000000"))
  palette.setColor(QPalette.Button, QColor("#efefef"))
  palette.setColor(QPalette.ButtonText, QColor("#000000"))
  palette.setColor(QPalette.BrightText, QColor("#ffffff"))
  palette.setColor(QPalette.Link, QColor("#0000ff"))
  palette.setColor(QPalette.Highlight, QColor("#308cc6"))
  palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
  app.setPalette(palette)
  save_settings("light")
