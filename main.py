from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #<-- Установка изображений 
        self.ui.krestik.setIcon(QIcon('close.png'))
        self.ui.krestik.setIconSize(QSize(80, 80))

        self.ui.nolik.setIcon(QIcon('nol.png'))
        self.ui.nolik.setIconSize(QSize(80, 80)
        #-->            
app = QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec_())
