# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kitaplar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem

from Ekle import *
from Guncelle import *


class Ui_kitaplar(object):
    def setupUi(self, kitaplar):
        kitaplar.setObjectName("kitaplar")
        kitaplar.resize(672, 597)
        self.gridLayout = QtWidgets.QGridLayout(kitaplar)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblAra = QtWidgets.QLabel(kitaplar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAra.setFont(font)
        self.lblAra.setScaledContents(False)
        self.lblAra.setWordWrap(False)
        self.lblAra.setObjectName("lblAra")
        self.horizontalLayout_4.addWidget(self.lblAra)
        self.lineEdit = QtWidgets.QLineEdit(kitaplar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tWEnvanter = QtWidgets.QTableWidget(kitaplar)
        self.tWEnvanter.setObjectName("tWEnvanter")
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select * from envanter"
        imlec.execute( sqlsorgu )
        satir = imlec.rowcount
        self.tWEnvanter.setRowCount( satir )
        self.tWEnvanter.setColumnCount( 10 )
        item = QtWidgets.QTableWidgetItem( )
        self.tWEnvanter.setVerticalHeaderItem( 0, item )
        item = QtWidgets.QTableWidgetItem( )
        for i in range( 0, 4 ):
            self.tWEnvanter.setHorizontalHeaderItem( i, item )
            self.tWEnvanter.setItem( 0, i, item )
            item = QtWidgets.QTableWidgetItem( )
        self.verticalLayout_2.addWidget(self.tWEnvanter)
        self.groupBox = QtWidgets.QGroupBox(kitaplar)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.groupBox)
        self.btnEkle.setMinimumSize(QtCore.QSize(0, 40))
        self.btnEkle.setObjectName("btnEkle")
        self.horizontalLayout_2.addWidget(self.btnEkle, 0, QtCore.Qt.AlignHCenter)
        self.btnDuzenle_2 = QtWidgets.QPushButton(self.groupBox)
        self.btnDuzenle_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDuzenle_2.setObjectName("btnDuzenle_2")
        self.horizontalLayout_2.addWidget(self.btnDuzenle_2, 0, QtCore.Qt.AlignHCenter)
        self.btnKaldir_2 = QtWidgets.QPushButton(self.groupBox)
        self.btnKaldir_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btnKaldir_2.setObjectName("btnKaldir_2")
        self.horizontalLayout_2.addWidget(self.btnKaldir_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.btnEkle.clicked.connect(self.eklegetir)
        self.btnDuzenle_2.clicked.connect(self.duzenlegetir)
        self.retranslateUi(kitaplar)
        self.btnDuzenle_2.clicked.connect(self.tWEnvanter.update)
        self.tWEnvanter.cellClicked['int','int'].connect(self.tWEnvanter.selectRow)
        self.tWEnvanter.cellDoubleClicked['int','int'].connect(self.btnDuzenle_2.click)
        QtCore.QMetaObject.connectSlotsByName(kitaplar)
        self.tWEnvanter.cellClicked.connect(self.idgonder)
        
    def retranslateUi(self, kitaplar):
        _translate = QtCore.QCoreApplication.translate
        kitaplar.setWindowTitle(_translate("kitaplar", "Kitaplar"))
        self.lblAra.setText(_translate("kitaplar", "Arama"))
        self.groupBox.setTitle(_translate("kitaplar", "İşlemler"))
        self.btnEkle.setText(_translate("kitaplar", "İçerik Ekle"))
        self.btnDuzenle_2.setText(_translate("kitaplar", "Düzenle"))
        self.btnKaldir_2.setText(_translate("kitaplar", "Kaldır"))
        self.createTable()
        self.getir()

    def createTable(self):
        # Create table
        _translate = QtCore.QCoreApplication.translate
        # self.tWEnvanter = QTableWidget( )
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select * from envanter"
        imlec.execute( sqlsorgu )
        satir = imlec.rowcount
        self.tWEnvanter.setRowCount( satir )
        self.tWEnvanter.setColumnCount( 5 )
        item = QtWidgets.QTableWidgetItem( )
        _translate = QtCore.QCoreApplication.translate
        for i in [0, 1, 2, 3, 4]:
            self.tWEnvanter.setHorizontalHeaderItem( i, item )
            item = QtWidgets.QTableWidgetItem( )
        item = self.tWEnvanter.horizontalHeaderItem( 0 )
        item.setText( _translate( "MainWindow", "id" ) )
        item = self.tWEnvanter.horizontalHeaderItem( 1 )
        item.setText( _translate( "MainWindow", "Kitap Adı" ) )
        item = self.tWEnvanter.horizontalHeaderItem( 2 )
        item.setText( _translate( "MainWindow", "Yazarı" ) )
        item = self.tWEnvanter.horizontalHeaderItem( 3 )
        item.setText( _translate( "MainWindow", "Yayınevi" ) )
        item = self.tWEnvanter.horizontalHeaderItem( 4 )
        item.setText( _translate( "MainWindow", "Türü" ) )
        self.tWEnvanter.move( 0, 0 )
        # self.lineEdit.editingFinished.connect(self.arama)
    
    def kaldir(self,id):
        self.mesaj()
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "DELETE FROM envanter WHERE id =" + self.idgonder()
        imlec.execute( sqlsorgu )

    def duzenlegetir(self):
        self.gecidgonder()
        self.welcomeWindow = QMainWindow( )
        self.ui = Ui_MainWindow( )
        self.ui.setupUi( self.welcomeWindow )
        self.welcomeWindow.show( )

    def eklegetir(self):
        self.welcomeWindow = QtWidgets.QDialog( )
        self.ui = Ui_Dialog( )
        self.ui.setupUi( self.welcomeWindow )
        self.welcomeWindow.show( )

    def getir(self):
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select * from envanter"
        imlec.execute( sqlsorgu )
        c = 0
        d = 0
        for i in imlec.fetchall( ):
            d = 0
            for j in i:
                self.tWEnvanter.setItem(c, d, QTableWidgetItem(str(j)))
                d += 1
                # print("c",c,"d",d ,j)
            c += 1
    
    def gecidgonder(self):
        idgonder=self.idgonder()
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "TRUNCATE geciciid"
        imlec.execute( sqlsorgu )
        sqlsorgu = "INSERT INTO geciciid(id, kitapid) VALUES(1,%s)"
        args = (idgonder)
        imlec.execute( sqlsorgu, args )
    
    def idgonder(self):
        indexes = []
        for selectionRange in self.tWEnvanter.selectedRanges( ):
            indexes.extend( range( selectionRange.topRow( ), selectionRange.bottomRow( ) + 1 ) )
        results = []
        for i in indexes:
            results.append( str( self.tWEnvanter.item( i, 0 ).text( ) ) )
        # print(self.tWEnvanter.item( i, 1 ).text( ))
        return self.tWEnvanter.item( i, 0 ).text( )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kitaplar = QtWidgets.QDialog()
    ui = Ui_kitaplar()
    ui.setupUi(kitaplar)
    kitaplar.show()
    sys.exit(app.exec_())

