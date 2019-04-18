import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon



class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("haha")
        self.setWindowIcon(QIcon('test.png'))  # mac 好像支持icon  https://stackoverflow.com/questions/44080247/pyqt5-does-now-show-icons/45439678#45439678
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())