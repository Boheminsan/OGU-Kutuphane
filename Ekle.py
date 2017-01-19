# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file `Ekle.ui`
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import baglanti

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(338, 326)
        self.btnEkle = QtWidgets.QPushButton(Dialog)
        self.btnEkle.setGeometry(QtCore.QRect(110, 280, 101, 31))
        self.btnEkle.setObjectName("btnEkle")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 291, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.cBTur = QtWidgets.QComboBox(self.layoutWidget)
        self.cBTur.setObjectName("cBTur")
        self.gridLayout.addWidget(self.cBTur, 3, 1, 1, 1)
        self.txtYayinEvi = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtYayinEvi.setObjectName("txtYayinEvi")
        self.gridLayout.addWidget(self.txtYayinEvi, 2, 1, 1, 1)
        self.lblYayinEvi = QtWidgets.QLabel(self.layoutWidget)
        self.lblYayinEvi.setObjectName("lblYayinEvi")
        self.gridLayout.addWidget(self.lblYayinEvi, 2, 0, 1, 1)
        self.txtYazari = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtYazari.setObjectName("txtYazari")
        self.gridLayout.addWidget(self.txtYazari, 1, 1, 1, 1)
        self.lblTur = QtWidgets.QLabel(self.layoutWidget)
        self.lblTur.setObjectName("lblTur")
        self.gridLayout.addWidget(self.lblTur, 3, 0, 1, 1)
        self.lblYazari = QtWidgets.QLabel(self.layoutWidget)
        self.lblYazari.setObjectName("lblYazari")
        self.gridLayout.addWidget(self.lblYazari, 1, 0, 1, 1)
        self.txtKitapAdi = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtKitapAdi.setObjectName("txtKitapAdi")
        self.gridLayout.addWidget(self.txtKitapAdi, 0, 1, 1, 1)
        self.lblKitapAdi = QtWidgets.QLabel(self.layoutWidget)
        self.lblKitapAdi.setObjectName("lblKitapAdi")
        self.gridLayout.addWidget(self.lblKitapAdi, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnEkle.clicked.connect(self.ekle)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kitap Ekle"))
        self.btnEkle.setText(_translate("Dialog", "Ekle"))
        self.lblYayinEvi.setText(_translate("Dialog", "Yayın Evi"))
        self.lblTur.setText(_translate("Dialog", "Türü"))
        self.lblYazari.setText(_translate("Dialog", "Yazarı"))
        self.lblKitapAdi.setText(_translate("Dialog", "Adı"))
        self.turcek()

    def ekle(self):
            kitap = self.txtKitapAdi.text()
            yazar = self.txtYazari.text()
            yevi = self.txtYayinEvi.text()
            tur = str( self.cBTur.currentText())
            imlec = baglanti.bag.cursor( )
            ysorgu = "select yazarAdi from yazarlar"
            imlec.execute( ysorgu )
            dizi = []
            yazarlar = imlec.fetchall( )
            for i in yazarlar:
                for j in i:
                    dizi.append( j )
            for k in dizi:
                if yazar != k:
                    sqlsorgu2 = self.sorgu( "yazar", yazar )
                    sqlsorgu3 = self.sorgu( "yayin", yevi )
                    imlec.execute(sqlsorgu2)
                    imlec.execute(sqlsorgu3)
            sqlsorgu4 = "INSERT INTO `envanter`(`id`, `adi`, `yazar`, `yayinevi`, `tur`) VALUES (NULL, `" + kitap + "`,`" + yazar + "`,`" + yevi + "`,`" + tur + "`)"
            imlec.execute(sqlsorgu4)
            print(sqlsorgu4)

    def sorgu(self,tablo,isim):
        return "INSERT INTO `" + tablo + "`(`" + tablo + "id`, `" + tablo + "adi`) VALUES (NULL ,`" + isim + "`)"
    
    def turcek(self):
        idler={}
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "SELECT turadi from tur order by turid asc"
        # for i in veri:
        #     for j in i:
        imlec.execute( sqlsorgu)
        idl = imlec.fetchall( )
        for i in idl:
            for j in i:
                idler[i[0]]=j
            self.cBTur.addItem(str(j))
        # print( idler )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

