# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaEkran2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

import Kitaplar
import Oduncler


class Ui_frmAnaMenu(object):
    def setupUi(self, frmAnaMenu):
        frmAnaMenu.setObjectName("frmAnaMenu")
        frmAnaMenu.setWindowModality(QtCore.Qt.NonModal)
        frmAnaMenu.setEnabled(True)
        frmAnaMenu.resize(492, 316)
        frmAnaMenu.setMinimumSize(QtCore.QSize(492, 316))
        frmAnaMenu.setAutoFillBackground(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(frmAnaMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GrafikGelecek = QtWidgets.QWidget(frmAnaMenu)
        self.GrafikGelecek.setStyleSheet("background-color:rgb(0, 170, 255);")
        self.GrafikGelecek.setObjectName("GrafikGelecek")
        self.horizontalLayout_3.addWidget(self.GrafikGelecek)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gB_Butonlar = QtWidgets.QGroupBox(frmAnaMenu)
        self.gB_Butonlar.setObjectName("gB_Butonlar")
        self.pB_Cikis = QtWidgets.QPushButton(self.gB_Butonlar)
        self.pB_Cikis.setEnabled(True)
        self.pB_Cikis.setGeometry(QtCore.QRect(360, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pB_Cikis.setFont(font)
        # self.pB_Cikis.setStyleSheet("border-image:'indir.png';")
        self.pB_Cikis.setText("Çıkış")
        self.pB_Cikis.setObjectName("pB_Cikis")
        self.gridLayoutWidget = QtWidgets.QWidget(self.gB_Butonlar)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 20, 291, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pB_Kitap = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Kitap.sizePolicy().hasHeightForWidth())
        self.pB_Kitap.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pB_Kitap.setFont(font)
        self.pB_Kitap.setStyleSheet("background-color:rgb(170, 255, 0)")
        self.pB_Kitap.setObjectName("pB_Kitap")
        self.gridLayout.addWidget(self.pB_Kitap, 0, 0, 1, 1)
        self.pB_Odunc = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Odunc.sizePolicy().hasHeightForWidth())
        self.pB_Odunc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pB_Odunc.setFont(font)
        self.pB_Odunc.setStyleSheet("background-color:rgb(100, 230,150)")
        self.pB_Odunc.setObjectName("pB_Odunc")
        self.gridLayout.addWidget(self.pB_Odunc, 0, 1, 1, 1)
        self.pB_Cikis.raise_()
        self.gridLayoutWidget.raise_()
        self.pB_Kitap.raise_()
        self.horizontalLayout_2.addWidget(self.gB_Butonlar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.retranslateUi(frmAnaMenu)
        QtCore.QMetaObject.connectSlotsByName(frmAnaMenu)
        self.pB_Kitap.clicked.connect(self.kitaplargetir)
        self.pB_Odunc.clicked.connect(self.oduncgetir)
        self.pB_Cikis.clicked.connect(QCoreApplication.instance().quit)
    def retranslateUi(self, frmAnaMenu):
        _translate = QtCore.QCoreApplication.translate
        frmAnaMenu.setWindowTitle(_translate("frmAnaMenu", "Ogü Kütüphane"))
        self.gB_Butonlar.setTitle(_translate("frmAnaMenu", "İşlemler"))
        self.pB_Kitap.setText(_translate("frmAnaMenu", "Kütüphane"))
        self.pB_Odunc.setText(_translate("frmAnaMenu", "Ödünç Kitap"))
    
    def kitaplargetir(self):
        dialog = QtWidgets.QDialog( )
        dialog.ui = Kitaplar.Ui_kitaplar( )
        dialog.ui.setupUi( dialog )
        dialog.exec_( )
        dialog.show( )
        
    def oduncgetir(self):
        dialog = QtWidgets.QDialog( )
        dialog.ui = Oduncler.Ui_OduncVer( )
        dialog.ui.setupUi( dialog )
        dialog.exec_( )
        dialog.show( )
# import kaynak.qrc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmAnaMenu = QtWidgets.QDialog()
    ui = Ui_frmAnaMenu()
    ui.setupUi(frmAnaMenu)
    frmAnaMenu.show()
    sys.exit(app.exec_())

