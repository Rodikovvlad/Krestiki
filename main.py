from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from start import Ui_MainWindow
from game import Ui_Form
from end import Ui_EndWindow
import sys


class endwindow(QWidget):
    def __init__(self):
        super(endwindow, self).__init__()
        self.ui = Ui_EndWindow()
        self.ui.setupUi(self)


class startwindow(QMainWindow):
    def __init__(self):
        
        super(startwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        side_flag = ""
        
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
        self.side_flag = "x"
        
    def nolikClicked(self):
        self.game.show()
        self.side_flag = "o"


class gamewindow(QWidget):
    def __init__(self):
        super(gamewindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.endwindow = endwindow()
        
        self.variants = [["_", "_", "_"],
                        ["_", "_", "_"],
                        ["_", "_", "_"]]
        
        self.cond_arr = [False, False, False, False, False, False, False, False, False]
        
        self.ui.field_1.clicked.connect(self.field_1Clicked)
        self.ui.field_2.clicked.connect(self.field_2Clicked)
        self.ui.field_3.clicked.connect(self.field_3Clicked)
        self.ui.field_4.clicked.connect(self.field_4Clicked)
        self.ui.field_5.clicked.connect(self.field_5Clicked)
        self.ui.field_6.clicked.connect(self.field_6Clicked)
        self.ui.field_7.clicked.connect(self.field_7Clicked)
        self.ui.field_8.clicked.connect(self.field_8Clicked)
        self.ui.field_9.clicked.connect(self.field_9Clicked)

    #<---------Нажатия
    def field_1Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[0]:
            self.variants[0][0] = "x"
            self.ui.field_1.setIcon(QIcon('close.png'))
            self.ui.field_1.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[0] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
            
        elif application.side_flag == "o" and not self.cond_arr[0]:
            self.variants[0][0] = "o"
            self.ui.field_1.setIcon(QIcon('nol.png'))
            self.ui.field_1.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[0] = True
        
    def field_2Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[1]:
            self.variants[0][1] = "x"
            self.ui.field_2.setIcon(QIcon('close.png'))
            self.ui.field_2.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[1] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
            
        elif application.side_flag == "o" and not self.cond_arr[1]:
            self.variants[0][1] = "o"
            self.ui.field_2.setIcon(QIcon('nol.png'))
            self.ui.field_2.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[1] = True
       
    def field_3Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[2]:
            self.variants[0][2] = "x"
            self.ui.field_3.setIcon(QIcon('close.png'))
            self.ui.field_3.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[2] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
           
        elif application.side_flag == "o" and not self.cond_arr[2]:
            self.variants[0][2] = "o"
            self.ui.field_3.setIcon(QIcon('nol.png'))
            self.ui.field_3.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[2] = True
       
    def field_4Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[3]:
            self.variants[1][0] = "x"
            self.ui.field_4.setIcon(QIcon('close.png'))
            self.ui.field_4.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[3] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
            
        elif application.side_flag == "o" and not self.cond_arr[3]:
            self.variants[1][0] = "o"
            self.ui.field_4.setIcon(QIcon('nol.png'))
            self.ui.field_4.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[3] = True
        
    def field_5Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[4]:
            self.variants[1][1] = "x"
            self.ui.field_5.setIcon(QIcon('close.png'))
            self.ui.field_5.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[4] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
        elif application.side_flag == "o" and not self.cond_arr[4]:
            self.variants[1][1] = "o"
            self.ui.field_5.setIcon(QIcon('nol.png'))
            self.ui.field_5.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[4] = True
      
    
    def field_6Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[5]:
            self.variants[1][2] = "x"
            self.ui.field_6.setIcon(QIcon('close.png'))
            self.ui.field_6.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[5] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
        elif application.side_flag == "o" and not self.cond_arr[5]:
            self.variants[1][2] = "o"
            self.ui.field_6.setIcon(QIcon('nol.png'))
            self.ui.field_6.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[5] = True
       
    def field_7Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[6]:
            self.variants[2][0] = "x"
            self.ui.field_7.setIcon(QIcon('close.png'))
            self.ui.field_7.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[6] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):
                self.endwindow.show()  
        elif application.side_flag == "o" and not self.cond_arr[6]:
            self.variants[2][0] = "o"
            self.ui.field_7.setIcon(QIcon('nol.png'))
            self.ui.field_7.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[6] = True
        
    def field_8Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[7]:
            self.variants[2][1] = "x"
            self.ui.field_8.setIcon(QIcon('close.png'))
            self.ui.field_8.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[7] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                              
                self.endwindow.show()
        elif application.side_flag == "o" and not self.cond_arr[7]:
            self.variants[2][1] = "o"
            self.ui.field_8.setIcon(QIcon('nol.png'))
            self.ui.field_8.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[7] = True
        
    def field_9Clicked(self):
        if application.side_flag == "x" and not self.cond_arr[8]:
            self.variants[2][2] = "x"
            self.ui.field_9.setIcon(QIcon('close.png'))
            self.ui.field_9.setIconSize(QSize(80, 80))
            application.side_flag = "o"
            self.cond_arr[8] = True
            if ("x" in self.variants[0][1] and "x" in self.variants[0][2]) or ("x" in self.variants[1][0] and "x" in self.variants[2][0]) or ("x" in self.variants[1][1] and "x" in self.variants[2][2]) or ("x" in self.variants[1][0] and "x" in self.variants[1][1] and "x" in self.variants[1][2]) or ("x" in self.variants[2][0] and "x" in self.variants[2][1] and "x" in self.variants[2][2]) or ("x" in self.variants[0][1] and "x" in self.variants[1][1] and "x" in self.variants[2][1]) or ("x" in self.variants[2][2] and "x" in self.variants[1][2] and "x" in self.variants[0][2]) or ("x" in self.variants[0][2] and "x" in self.variants[1][1] and "x" in self.variants[2][0]):                                                                                                                                                                    
                self.endwindow.show()
           
        elif application.side_flag == "o" and not self.cond_arr[8]:
            self.variants[2][2] = "o"
            self.ui.field_9.setIcon(QIcon('nol.png'))
            self.ui.field_9.setIconSize(QSize(80, 80))
            application.side_flag = "x"
            self.cond_arr[8] = True
        
    # Нажатия-------->


    


            
app = QApplication([])
application = startwindow()
application.show()
 
sys.exit(app.exec_())
