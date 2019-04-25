import sys
from random import randint

from PyQt5.QtWidgets import *

from UI import a1


class Action(QMainWindow, a1.Ui_MainWindow):
    """
    Class documentation goes here.

    """

    def __init__(self):

        super().__init__()

        self.setupUi(self)

        self.num = randint(1, 100)

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def on_pushButton_clicked(self):

        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        guessnumber = int(self.lineEdit.text())

        print(self.num)

        if guessnumber > self.num:

            QMessageBox.about(self, '看结果', '猜大了!')

            self.lineEdit.setFocus()

        elif guessnumber < self.num:

            QMessageBox.about(self, '看结果', '猜小了!')

            self.lineEdit.setFocus()

        else:

            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')

            self.num = randint(1, 100)

            self.lineEdit.clear()

            self.lineEdit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    action = Action()

    sys.exit(app.exec_())
