import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False) # mac系统对menu的理解不一样


        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impMenu.addAction(QAction('Import mail', self))
        fileMenu.addMenu(impMenu)


        newAct = QAction('New', self)
        fileMenu.addAction(newAct)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())