import sys

from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from interface import Ui_Dialog


def gronsfeld_code(message, key, state, alphabet):
    key *= len(message) // len(key) + 1
    message = message.lower()
    return ''.join([ alphabet[ alphabet.index(j) + int(key[ i ]) * state ] for i, j in enumerate(message) ])


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.alphabet = ''
        self.state = 0
        self.key = ''
        self.message = ''
        self.ui = Ui_Dialog()
        self.initUI()

    def initUI(self):

        self.ui.setupUi(self)
        self.show()

        # Hook logic
        self.ui.buttonGroup.buttonClicked.connect(self.alphabet_init)
        self.ui.buttonGroup_2.buttonClicked.connect(self.state_init)
        self.ui.message_field.editingFinished.connect(self.message_init)
        self.ui.key_field.editingFinished.connect(self.key_init)

        self.ui.pushButton.clicked.connect(self.cipher_init)

    def alphabet_init(self, check_box):
        if check_box.isChecked() and check_box.objectName() == 'Russia':
            self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' * 2
        elif check_box.isChecked() and check_box.objectName() == 'English':
            self.alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
        elif check_box.isChecked() and check_box.objectName() == 'German':
            self.alphabet = 'aäbcdefghijklmnoöpqrsßtuüvwxyz' * 2
        else:
            self.alphabet = self.ui.alphabet_field.text()

    def state_init(self, check_box):
        if check_box.isChecked() and check_box.objectName() == 'encryption':
            self.state = 1
        elif check_box.isChecked() and check_box.objectName() == 'decryption':
            self.state = -1

    def key_init(self):
        self.key = self.ui.key_field.text()

    def message_init(self):
        self.message = self.ui.message_field.text()

    def cipher_init(self):
        result = gronsfeld_code(self.message, self.key, self.state, self.alphabet)
        self.ui.textBrowser.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create app
    ex = Application()
    sys.exit(app.exec_())  # Main loop
