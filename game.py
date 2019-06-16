# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.krestik_1 = QtWidgets.QPushButton(Form)
        self.krestik_1.setGeometry(QtCore.QRect(50, 30, 141, 111))
        self.krestik_1.setText("")
        self.krestik_1.setObjectName("krestik_1")
        self.krestik_5 = QtWidgets.QPushButton(Form)
        self.krestik_5.setGeometry(QtCore.QRect(190, 140, 141, 111))
        self.krestik_5.setText("")
        self.krestik_5.setObjectName("krestik_5")
        self.krestik_7 = QtWidgets.QPushButton(Form)
        self.krestik_7.setGeometry(QtCore.QRect(50, 250, 141, 111))
        self.krestik_7.setText("")
        self.krestik_7.setObjectName("krestik_7")
        self.krestik_4 = QtWidgets.QPushButton(Form)
        self.krestik_4.setGeometry(QtCore.QRect(50, 140, 141, 111))
        self.krestik_4.setText("")
        self.krestik_4.setObjectName("krestik_4")
        self.krestik_2 = QtWidgets.QPushButton(Form)
        self.krestik_2.setGeometry(QtCore.QRect(190, 30, 141, 111))
        self.krestik_2.setText("")
        self.krestik_2.setObjectName("krestik_2")
        self.krestik_8 = QtWidgets.QPushButton(Form)
        self.krestik_8.setGeometry(QtCore.QRect(190, 250, 141, 111))
        self.krestik_8.setText("")
        self.krestik_8.setObjectName("krestik_8")
        self.krestik_6 = QtWidgets.QPushButton(Form)
        self.krestik_6.setGeometry(QtCore.QRect(330, 140, 141, 111))
        self.krestik_6.setText("")
        self.krestik_6.setObjectName("krestik_6")
        self.krestik_3 = QtWidgets.QPushButton(Form)
        self.krestik_3.setGeometry(QtCore.QRect(330, 30, 141, 111))
        self.krestik_3.setText("")
        self.krestik_3.setObjectName("krestik_3")
        self.krestik_9 = QtWidgets.QPushButton(Form)
        self.krestik_9.setGeometry(QtCore.QRect(330, 250, 141, 111))
        self.krestik_9.setText("")
        self.krestik_9.setObjectName("krestik_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Крестики-нолики"))

