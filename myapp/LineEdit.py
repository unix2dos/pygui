from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    def __int__(self):
        super().__init__()

    def lineEditText(self):
        print(self.text(), "jaja")
