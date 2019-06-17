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
        self.field_1 = QtWidgets.QPushButton(Form)
        self.field_1.setGeometry(QtCore.QRect(50, 30, 141, 111))
        self.field_1.setText("")
        self.field_1.setObjectName("field_1")
        self.field_5 = QtWidgets.QPushButton(Form)
        self.field_5.setGeometry(QtCore.QRect(190, 140, 141, 111))
        self.field_5.setText("")
        self.field_5.setObjectName("field_5")
        self.field_7 = QtWidgets.QPushButton(Form)
        self.field_7.setGeometry(QtCore.QRect(50, 250, 141, 111))
        self.field_7.setText("")
        self.field_7.setObjectName("field_7")
        self.field_4 = QtWidgets.QPushButton(Form)
        self.field_4.setGeometry(QtCore.QRect(50, 140, 141, 111))
        self.field_4.setText("")
        self.field_4.setObjectName("field_4")
        self.field_2 = QtWidgets.QPushButton(Form)
        self.field_2.setGeometry(QtCore.QRect(190, 30, 141, 111))
        self.field_2.setText("")
        self.field_2.setObjectName("field_2")
        self.field_8 = QtWidgets.QPushButton(Form)
        self.field_8.setGeometry(QtCore.QRect(190, 250, 141, 111))
        self.field_8.setText("")
        self.field_8.setObjectName("field_8")
        self.field_6 = QtWidgets.QPushButton(Form)
        self.field_6.setGeometry(QtCore.QRect(330, 140, 141, 111))
        self.field_6.setText("")
        self.field_6.setObjectName("field_6")
        self.field_3 = QtWidgets.QPushButton(Form)
        self.field_3.setGeometry(QtCore.QRect(330, 30, 141, 111))
        self.field_3.setText("")
        self.field_3.setObjectName("field_3")
        self.field_9 = QtWidgets.QPushButton(Form)
        self.field_9.setGeometry(QtCore.QRect(330, 250, 141, 111))
        self.field_9.setText("")
        self.field_9.setObjectName("field_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Крестики-нолики"))

