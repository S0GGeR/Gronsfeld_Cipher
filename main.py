import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QRect

from PySide2.QtWidgets import *

from interface import Ui_Dialog


def gronsfeld_code(message, key, state, alphabet):
    key *= len(message) // len(key) + 1
    return ''.join([ alphabet[ alphabet.index(j) + int(key[ i ]) * state ] for i, j in enumerate(message) ])


def caesar_code(message, key, state, alphabet):
    key = int(key)
    return ''.join([ alphabet[ alphabet.index(j) + int(key) * state ] for i, j in enumerate(message) ])


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.method = 0
        self.alphabet = ''
        self.state = 0
        self.key = '0'
        self.message = ''
        self.ui = Ui_Dialog()
        self.initUI()

    def initUI(self):

        self.ui.setupUi(self)
        self.show()

        # Hook logic
        self.ui.buttonGroup.buttonClicked.connect(self.alphabet_init)
        self.ui.buttonGroup_2.buttonClicked.connect(self.state_init)
        self.ui.buttonGroup_3.buttonClicked.connect(self.method_init)
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
            self.alphabet = self.ui.alphabet_field.text().replace(' ', '')

    def state_init(self, check_box):
        if check_box.isChecked() and check_box.objectName() == 'encryption':
            self.state = 1
        elif check_box.isChecked() and check_box.objectName() == 'decryption':
            self.state = -1

    def key_init(self):
        self.key = self.ui.key_field.text().replace(' ', '')
        try:
            int(self.key)
        except:
            self.ui.error_label_3.setText(
                'Пожалуйста, используйте в поле ключа только арабские цифры в десятичной системе счисления!')

    def message_init(self):
        self.message = self.ui.message_field.text().lower().replace(' ', '')
        # Checking for letters in a message that are not in the alphabet
        j = 0
        for letter in self.message:
            for i in range(0, len(self.alphabet)):
                if letter == self.alphabet[ i ]:
                    j += 1
                    break
        if j != len(self.message):
            self.ui.error_label_2.setText('Пожалуйста, используйте символы только из алфавита!')
            # self.ui.error_label.setGeometry(QRect(200, 290, 570, 20))
            self.message = ''
            self.ui.message_field.setText('')
        elif j == len(self.message) and self.ui.error_label.text() == (
                'Пожалуйста, используйте символы только из алфавита!'):
            self.ui.error_label.setText(' ')

    def cipher_init(self):
        if self.alphabet != '' and self.state != 0 and self.key != '0' and self.message != '' and self.method != 0:
            self.ui.error_label.setText('')
            if self.method == 1:
                result = caesar_code(self.message, self.key, self.state, self.alphabet)
            elif self.method == 2:
                result = gronsfeld_code(self.message, self.key, self.state, self.alphabet)
            self.ui.textBrowser.setText(result)

        else:
            self.ui.error_label.setText('Пожалуйста, заполните все поля!')

    def method_init(self, check_box):
        if check_box.isChecked() and check_box.objectName() == 'caesar':
            self.method = 1
        elif check_box.isChecked() and check_box.objectName() == 'gronsfeld':
            self.method = 2


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create app
    ex = Application()
    sys.exit(app.exec_())  # Main loop
