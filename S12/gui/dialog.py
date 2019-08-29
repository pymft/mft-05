# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 30, 100, 13))
        self.label.setText("")

        self.buttons = []
        for i in range(10):
            self.buttons.append(QtWidgets.QPushButton(Dialog))
            self.buttons[-1].setGeometry(QtCore.QRect(10 + 40 * i, 50, 30, 30))
            self.buttons[-1].setText(str(i))

        for i in range(10):
            self.buttons[i].clicked.connect(self.some_method(i))

    def some_method(self,i):
        def inner():
            temp = self.label.text()

            self.label.setText(temp + str(i))
        return inner

