from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from start import Ui_MainWindow
from game import Ui_Form
# импорт нашего сгенерированного файла
import sys


class startwindow(QMainWindow):
    def __init__(self):
        super(startwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #<-- Установка изображений 
        self.ui.krestik.setIcon(QIcon('close.png'))
        self.ui.krestik.setIconSize(QSize(80, 80))

        self.ui.nolik.setIcon(QIcon('nol.png'))
        self.ui.nolik.setIconSize(QSize(80, 80))
        #-->

        self.game = gamewindow()
        
        self.ui.krestik.clicked.connect(self.krestikClicked)
        self.ui.nolik.clicked.connect(self.nolikClicked)
        
    def krestikClicked(self):
        self.game.show()
        
    def nolikClicked(self):
        pass


class gamewindow(QWidget):
    def __init__(self):
        super(gamewindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

app = QApplication([])
application = startwindow()
application.show()
 
sys.exit(app.exec_())
