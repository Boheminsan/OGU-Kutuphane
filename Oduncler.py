# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Oduncler.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import Odunc
import Sil
import baglanti


class Ui_OduncVer(object):
    def setupUi(self, OduncVer):
        OduncVer.setObjectName("OduncVer")
        OduncVer.resize(682, 468)
        self.verticalLayoutWidget = QtWidgets.QWidget(OduncVer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 671, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.twOKitap = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.twOKitap.setObjectName("twOKitap")
        self.twOKitap.setColumnCount(6)
        self.twOKitap.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twOKitap.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.twOKitap)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 30, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnYeni = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnYeni.sizePolicy().hasHeightForWidth())
        self.btnYeni.setSizePolicy(sizePolicy)
        self.btnYeni.setMinimumSize(QtCore.QSize(60, 30))
        self.btnYeni.setMaximumSize(QtCore.QSize(170, 30))
        self.btnYeni.setObjectName("btnYeni")
        self.horizontalLayout.addWidget(self.btnYeni)
        self.btnUzat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUzat.sizePolicy().hasHeightForWidth())
        self.btnUzat.setSizePolicy(sizePolicy)
        self.btnUzat.setMinimumSize(QtCore.QSize(60, 30))
        self.btnUzat.setMaximumSize(QtCore.QSize(170, 30))
        self.btnUzat.setObjectName("btnUzat")
        self.horizontalLayout.addWidget(self.btnUzat)
        self.btnSil = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSil.sizePolicy().hasHeightForWidth())
        self.btnSil.setSizePolicy(sizePolicy)
        self.btnSil.setMinimumSize(QtCore.QSize(60, 30))
        self.btnSil.setMaximumSize(QtCore.QSize(170, 30))
        self.btnSil.setObjectName("btnSil")
        self.horizontalLayout.addWidget(self.btnSil)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(OduncVer)
        self.btnYeni.clicked.connect(self.oduncgetir)
        self.btnSil.clicked.connect(self.iade)
        QtCore.QMetaObject.connectSlotsByName(OduncVer)
        self.createTable()
        self.getir()

    def retranslateUi(self, OduncVer):
        _translate = QtCore.QCoreApplication.translate
        OduncVer.setWindowTitle(_translate("OduncVer", "Ödünç Kitap"))
        # 
        self.btnYeni.setText(_translate("OduncVer", "Yeni"))
        self.btnUzat.setText(_translate("OduncVer", "Süre Uzat"))
        self.btnSil.setText(_translate("OduncVer", "Teslim Al"))
        self.twOKitap.cellClicked.connect(self.idgonder)
        self.btnUzat.clicked.connect(self.sureuzat)

    def oduncgetir(self):
        dialog = QtWidgets.QDialog( )
        dialog.ui = Odunc.Ui_OduncEkle( )
        dialog.ui.setupUi( dialog )
        dialog.exec_( )
        dialog.show( )
    
    def iade(self):
        id=self.idgonder()
        imlec=baglanti.bag.cursor()
        sql="UPDATE `odunc` SET `teslim`=1 WHERE `onid`="+id
        print(sql)
        imlec.execute(sql)
        # self.twOKitap.repaint()
        # yenileyemedim     
    
    def idgonder(self):
        indexes = []
        for selectionRange in self.twOKitap.selectedRanges( ):
            indexes.extend( range( selectionRange.topRow( ), selectionRange.bottomRow( ) + 1 ) )
        results = []
        for i in indexes:
            results.append( str( self.twOKitap.item( i, 0 ).text( ) ) )
        # print(self.twOKitap.item( i, 1 ).text( ))
        return self.twOKitap.item( i, 1 ).text( )

    def createTable(self):
        # Create table
        _translate = QtCore.QCoreApplication.translate
        # self.twOKitap = QTableWidget( )
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select * from odunc"
        imlec.execute( sqlsorgu )
        satir = imlec.rowcount
        self.twOKitap.setRowCount( satir )
        self.twOKitap.setColumnCount( 7 )
        item = QtWidgets.QTableWidgetItem( )
        _translate = QtCore.QCoreApplication.translate
        for i in [0, 1, 2, 3, 4, 5, 6]:
            self.twOKitap.setHorizontalHeaderItem( i, item )
            item = QtWidgets.QTableWidgetItem( )
        item = self.twOKitap.horizontalHeaderItem( 0 )
        item.setText( _translate( "OduncVer", "Kitap Adı" ) )
        item = self.twOKitap.horizontalHeaderItem( 1 )
        item.setText( _translate( "OduncVer", "Odünç Kitap No" ) )
        item = self.twOKitap.horizontalHeaderItem( 2 )
        item.setText( _translate( "OduncVer", "Öğrenci Numarası" ) )
        item = self.twOKitap.horizontalHeaderItem( 3 )
        item.setText( _translate( "OduncVer", "Öğrenci Adı" ) )
        item = self.twOKitap.horizontalHeaderItem( 4 )
        item.setText( _translate( "OduncVer", "Ödünç Alma Tarihi" ) )
        item = self.twOKitap.horizontalHeaderItem( 5 )
        item.setText( _translate( "OduncVer", "İade Tarihi" ) )
        item = self.twOKitap.horizontalHeaderItem( 6 )
        item.setText( _translate( "OduncVer", "Teslim Edildi mi?" ) )
        self.twOKitap.move( 0, 0 )

    def sureuzat(self):
        id=self.idgonder()
        imlec = baglanti.bag.cursor( )
        sqltarih = "Select `v_tarih` + INTERVAL 14 DAY from `odunc` where `onid`=" + id
        imlec.execute( sqltarih )
        tarih = imlec.fetchone( )
        # print(tarih)
        # for i in tarih:
        #     year, month, day = map( int, i.split( '-' ) )
        #     tarih2 = datetime( year, month, day )
        # sql = "UPDATE `odunc` SET `v_tarihi`=`"+tarih2+"` WHERE `onid`=" + id
        # # print( sqltarih )
        # # print( sql )
        # imlec.execute( sql )

    def getir(self):
        # _translate = QtCore.QCoreApplication.translate
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select * from odunc"
        imlec.execute( sqlsorgu )
        c = 0
        d = 0
        for i in imlec.fetchall( ):
            d = 0
            for j in i:
                self.twOKitap.setItem( c, d, QTableWidgetItem( str( j ) ) )
                d += 1
                # print("c",c,"d",d ,j)
            c += 1
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OduncVer = QtWidgets.QDialog()
    ui = Ui_OduncVer()
    ui.setupUi(OduncVer)
    OduncVer.show()
    sys.exit(app.exec_())

