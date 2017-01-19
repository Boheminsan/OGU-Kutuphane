# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KGiris.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from AnaEkran import Ui_MainWindow_Ana
import sys

class Ui_KGiris(object):
    def anaekranigetir(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Ana( )
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def giris(self):
        host = "localhost"  # Veritabanı host adresi
        dbuser = "root"  # Veritabanı kullanıcı adı
        dbpass = ""  # Veritabanı kullanıcı adının şifresi
        db_adi = "kutuphane"  # Veritabanı adı
        bag = pymysql.connect(host, dbuser, dbpass, db_adi)
        imlec = bag.cursor()
        var_mi = imlec.execute("select * from yetkili where kAdi=%s and kSifre=%s",
                               (self.txtKadi.text(), self.txtSifre.text()))
        if var_mi:
            self.anaekranigetir()
        imlec.close()
        bag.close()

    def setupUi(self, KGiris):
        KGiris.setObjectName("KGiris")
        KGiris.resize(349, 257)
        self.groupBoxAna = QtWidgets.QGroupBox(KGiris)
        self.groupBoxAna.setGeometry(QtCore.QRect(30, 20, 291, 211))
        self.groupBoxAna.setObjectName("groupBoxAna")
        self.btnGiris = QtWidgets.QPushButton(self.groupBoxAna)
        self.btnGiris.setGeometry(QtCore.QRect(100, 140, 91, 41))
        self.btnGiris.setObjectName("btnGiris")
        self.txtSifre = QtWidgets.QLineEdit(self.groupBoxAna)
        self.txtSifre.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.txtSifre.setObjectName("txtSifre")
        self.lblSifre = QtWidgets.QLabel(self.groupBoxAna)
        self.lblSifre.setGeometry(QtCore.QRect(50, 80, 71, 21))
        self.lblSifre.setObjectName("lblSifre")
        self.txtKadi = QtWidgets.QLineEdit(self.groupBoxAna)
        self.txtKadi.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.txtKadi.setObjectName("txtKadi")
        self.lblKadi = QtWidgets.QLabel(self.groupBoxAna)
        self.lblKadi.setGeometry(QtCore.QRect(50, 40, 61, 21))
        self.lblKadi.setObjectName("lblKadi")
        self.retranslateUi(KGiris)
        # button event
        self.btnGiris.clicked.connect(self.giris)
        QtCore.QMetaObject.connectSlotsByName(KGiris)

    def retranslateUi(self, KGiris):
        _translate = QtCore.QCoreApplication.translate
        KGiris.setWindowTitle(_translate("KGiris", "OGÜ Kütüphane Otomasyonu"))
        self.groupBoxAna.setTitle(_translate("KGiris", "Yetkili Girişi"))
        self.btnGiris.setText(_translate("KGiris", "Giriş"))
        self.lblSifre.setText(_translate("KGiris", "Şifre"))
        self.lblKadi.setText(_translate("KGiris", "Kullanıcı Adı:"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    KGiris = QtWidgets.QDialog()
    ui = Ui_KGiris()
    ui.setupUi(KGiris)
    KGiris.show()
    sys.exit(app.exec_())

