# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SilOnay(object):
    def setupUi(self, SilOnay):
        SilOnay.setObjectName("SilOnay")
        SilOnay.resize(400, 175)
        SilOnay.setMinimumSize(QtCore.QSize(400, 175))
        SilOnay.setMaximumSize(QtCore.QSize(400, 175))
        self.label = QtWidgets.QLabel(SilOnay)
        self.label.setGeometry(QtCore.QRect(30, 30, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(SilOnay)
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SilOnay)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 120, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton.clicked.connect(self.sil)
        self.retranslateUi(SilOnay)
        QtCore.QMetaObject.connectSlotsByName(SilOnay)

    def retranslateUi(self, SilOnay):
        _translate = QtCore.QCoreApplication.translate
        SilOnay.setWindowTitle(_translate("SilOnay", "Kayıt Sil"))
        self.label.setText(_translate("SilOnay", "Kaydı silmek istediğinize emin misiniz?"))
        self.pushButton.setText(_translate("SilOnay", "Hayır"))
        self.pushButton_2.setText(_translate("SilOnay", "Evet"))
        self.pushButton_2.clicked.connect(self.sil)

    
    def sil(self):
        print("45")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SilOnay = QtWidgets.QDialog()
    ui = Ui_SilOnay()
    ui.setupUi(SilOnay)
    SilOnay.show()
    sys.exit(app.exec_())

