# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'end.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EndWindow(object):
    def setupUi(self, EndWindow):
        EndWindow.setObjectName("EndWindow")
        EndWindow.resize(500, 400)
        self.label = QtWidgets.QLabel(EndWindow)
        self.label.setGeometry(QtCore.QRect(60, 60, 351, 201))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: blue;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(EndWindow)
        QtCore.QMetaObject.connectSlotsByName(EndWindow)

    def retranslateUi(self, EndWindow):
        _translate = QtCore.QCoreApplication.translate
        EndWindow.setWindowTitle(_translate("EndWindow", "Крестики-нолики"))
        self.label.setText(_translate("EndWindow", "Крестики\n"
"выиграли!"))

