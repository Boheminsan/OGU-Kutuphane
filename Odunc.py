# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Odunc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import baglanti


class Ui_OduncEkle(object):
    def setupUi(self, OduncEkle):
        OduncEkle.setObjectName("OduncEkle")
        OduncEkle.resize(657, 430)
        font = QtGui.QFont()
        font.setPointSize(10)
        OduncEkle.setFont(font)
        self.btnKaydet = QtWidgets.QPushButton(OduncEkle)
        self.btnKaydet.setGeometry(QtCore.QRect(290, 350, 111, 41))
        self.btnKaydet.setObjectName("btnKaydet")
        self.layoutWidget = QtWidgets.QWidget(OduncEkle)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 621, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_2.setHorizontalSpacing(22)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblOkul = QtWidgets.QLabel(self.layoutWidget)
        self.lblOkul.setObjectName("lblOkul")
        self.gridLayout_2.addWidget(self.lblOkul, 1, 0, 1, 1)
        self.lblOgrAdi = QtWidgets.QLabel(self.layoutWidget)
        self.lblOgrAdi.setObjectName("lblOgrAdi")
        self.gridLayout_2.addWidget(self.lblOgrAdi, 2, 0, 1, 1)
        self.lblKitapid = QtWidgets.QLabel(self.layoutWidget)
        self.lblKitapid.setObjectName("lblKitapid")
        self.gridLayout_2.addWidget(self.lblKitapid, 0, 0, 1, 1)
        self.lblVTarih = QtWidgets.QLabel(self.layoutWidget)
        self.lblVTarih.setObjectName("lblVTarih")
        self.gridLayout_2.addWidget(self.lblVTarih, 3, 0, 1, 1)
        self.lblATarih = QtWidgets.QLabel(self.layoutWidget)
        self.lblATarih.setObjectName("lblATarih")
        self.gridLayout_2.addWidget(self.lblATarih, 4, 0, 1, 1)
        self.dtVerilis = QtWidgets.QDateEdit(self.layoutWidget)
        self.dtVerilis.setObjectName("dtVerilis")
        self.gridLayout_2.addWidget(self.dtVerilis, 3, 2, 1, 1)
        self.dtAlinis = QtWidgets.QDateEdit(self.layoutWidget)
        self.dtAlinis.setEnabled(True)
        self.dtAlinis.setReadOnly(True)
        self.dtAlinis.setObjectName("dtAlinis")
        self.gridLayout_2.addWidget(self.dtAlinis, 4, 2, 1, 1)
        self.txtOgrAdi = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOgrAdi.sizePolicy().hasHeightForWidth())
        self.txtOgrAdi.setSizePolicy(sizePolicy)
        self.txtOgrAdi.setObjectName("txtOgrAdi")
        self.gridLayout_2.addWidget(self.txtOgrAdi, 2, 2, 1, 1)
        self.txtKitapid = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtKitapid.sizePolicy().hasHeightForWidth())
        self.txtKitapid.setSizePolicy(sizePolicy)
        self.txtKitapid.setObjectName("txtKitapid")
        self.gridLayout_2.addWidget(self.txtKitapid, 0, 2, 1, 1)
        self.txtogrno = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtogrno.sizePolicy().hasHeightForWidth())
        self.txtogrno.setSizePolicy(sizePolicy)
        self.txtogrno.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.txtogrno, 1, 2, 1, 1)
        self.twBilgi = QtWidgets.QTableWidget(OduncEkle)
        self.twBilgi.setEnabled(False)
        self.twBilgi.setGeometry(QtCore.QRect(20, 240, 621, 91))
        self.twBilgi.setAutoFillBackground(False)
        self.twBilgi.setObjectName("twBilgi")
        self.twBilgi.setColumnCount(4)
        self.twBilgi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBilgi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBilgi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBilgi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBilgi.setHorizontalHeaderItem(3, item)
        self.lblBilgiler = QtWidgets.QLabel(OduncEkle)
        self.lblBilgiler.setGeometry(QtCore.QRect(30, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBilgiler.setFont(font)
        self.lblBilgiler.setObjectName("lblBilgiler")

        self.retranslateUi(OduncEkle)
        self.txtKitapid.editingFinished.connect(self.twBilgi.update)
        self.btnKaydet.clicked.connect(self.twBilgi.selectAll)
        QtCore.QMetaObject.connectSlotsByName(OduncEkle)
        OduncEkle.setTabOrder(self.txtKitapid, self.txtogrno)
        OduncEkle.setTabOrder(self.txtogrno, self.txtOgrAdi)
        OduncEkle.setTabOrder(self.txtOgrAdi, self.dtVerilis)
        OduncEkle.setTabOrder(self.dtVerilis, self.dtAlinis)
        OduncEkle.setTabOrder(self.dtAlinis, self.twBilgi)
        OduncEkle.setTabOrder(self.twBilgi, self.btnKaydet)

    def retranslateUi(self, OduncEkle):
        _translate = QtCore.QCoreApplication.translate
        OduncEkle.setWindowTitle(_translate("OduncEkle", "Ödünç Kitap"))
        self.btnKaydet.setText(_translate("OduncEkle", "Kaydet"))
        self.lblOkul.setText(_translate("OduncEkle", "Okul Numarası"))
        self.lblOgrAdi.setText(_translate("OduncEkle", "Ödünç Alanın Adı"))
        self.lblKitapid.setText(_translate("OduncEkle", "Kitap Adı"))
        self.lblVTarih.setText(_translate("OduncEkle", "Ödünç Verildiği Tarihi"))
        self.lblATarih.setText(_translate("OduncEkle", "Kitap İade Tarihi"))
        item = self.twBilgi.horizontalHeaderItem(0)
        item.setText(_translate("OduncEkle", "Kitap Adı"))
        item = self.twBilgi.horizontalHeaderItem(1)
        item.setText(_translate("OduncEkle", "Yazarı"))
        item = self.twBilgi.horizontalHeaderItem(2)
        item.setText(_translate("OduncEkle", "Yayın Evi"))
        item = self.twBilgi.horizontalHeaderItem(3)
        item.setText(_translate("OduncEkle", "Türü"))
        self.lblBilgiler.setText(_translate("OduncEkle", "Kitap Bilgileri"))
    
    def oduncekle(self):
        imlec = baglanti.bag.cursor( )
        sqltarih = "Select `a_tarih` + INTERVAL 14 DAY from `odunc` where `onid`=" + id
        imlec.execute( sqltarih )
        tarih = imlec.fetchone( )
    
    def ekle(self):
            kitapadi = self.txtKitapid.text()
            ogrno = self.txtogrno.text()
            ogradi = self.txtOgrAdi.text()
            atar = "tarihi çek"
            vtar=atar+"14"
            imlec = baglanti.bag.cursor( )
            sqlsorgu = "INSERT INTO `odunc`(`kitap`, `onid`, `ogr_no`, `ogd_adi`, `a_tarih`, `v_tarih`,`teslim`) VALUES (`"+kitapadi+"`,NULL, `" + ogrno + "`,`" + ogradi + "`,`" + atar + "`,`" + vtar + "`,NULL)"
            imlec.execute(sqlsorgu)
            # print(sqlsorgu)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OduncEkle = QtWidgets.QDialog()
    ui = Ui_OduncEkle()
    ui.setupUi(OduncEkle)
    OduncEkle.show()
    sys.exit(app.exec_())

