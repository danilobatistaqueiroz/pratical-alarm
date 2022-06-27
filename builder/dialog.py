from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QTextEdit, QPlainTextEdit
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import Qt

class PlainTextEdit(QPlainTextEdit):
  def __init__(self):
    super().__init__()
  def keyPressEvent(self, event):
      if event.key() in (Qt.Key_Return, Qt.Key_Enter):
        return
      super().keyPressEvent(event)

class CustomDialog(QDialog):
  def __init__(self, main_window):
    super().__init__()
    QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    self.setWindowTitle("New Alarm")
    self.setFixedSize(300, 100)
    self.center(main_window)
    self.buttonBox = QDialogButtonBox(QBtn)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    self.buttonBox.setStyleSheet("background-color : #535353")
    self.buttonBox.setFocus()
    self.text = PlainTextEdit()
    self.layout = QVBoxLayout()
    message = QLabel("name the alarm:")
    self.layout.addWidget(message)
    self.layout.addWidget(self.text)
    self.layout.addWidget(self.buttonBox)
    self.setLayout(self.layout)

  def center(self, main_window):
    self.setGeometry((main_window.width()/3)+main_window.x()-(self.width()/4), main_window.y()+(main_window.height()/3), 250, 100)

  def center_screen(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

def show_dialog(main_window):
  dlg = CustomDialog(main_window)
  ret = dlg.exec()
  return {'status':ret,'text':dlg.text.toPlainText()}