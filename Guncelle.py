# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtWidgets,QtGui

import baglanti


class Ui_MainWindow( object ):
    def setupUi(self, MainWindow):
        # AnaEkran.Ui_MainWindow.guncellegetir()
        MainWindow.setObjectName( "MainWindow" )
        MainWindow.resize( 408, 311 )
        self.centralwidget = QtWidgets.QWidget( MainWindow )
        self.centralwidget.setObjectName( "centralwidget" )
        self.pushButton = QtWidgets.QPushButton( self.centralwidget )
        self.pushButton.setGeometry( QtCore.QRect( 159, 239, 81, 31 ) )
        self.pushButton.setObjectName( "pushButton" )
        self.layoutWidget = QtWidgets.QWidget( self.centralwidget )
        self.layoutWidget.setGeometry( QtCore.QRect( 20, 10, 351, 221 ) )
        self.layoutWidget.setObjectName( "layoutWidget" )
        self.gridLayout = QtWidgets.QGridLayout( self.layoutWidget )
        self.gridLayout.setContentsMargins( 0, 0, 0, 0 )
        self.gridLayout.setObjectName( "gridLayout" )
        self.label = QtWidgets.QLabel( self.layoutWidget )
        self.label.setObjectName( "label" )
        self.gridLayout.addWidget( self.label, 0, 0, 1, 1 )
        self.lineEdit = QtWidgets.QLineEdit( self.layoutWidget )
        self.lineEdit.setObjectName( "lineEdit" )
        self.gridLayout.addWidget( self.lineEdit, 0, 1, 1, 1 )
        self.label2 = QtWidgets.QLabel( self.layoutWidget )
        self.label2.setObjectName( "label2" )
        self.gridLayout.addWidget( self.label2, 1, 0, 1, 1 )
        self.lineEdit2 = QtWidgets.QLineEdit( self.layoutWidget )
        self.lineEdit2.setObjectName( "lineEdit2" )
        self.gridLayout.addWidget( self.lineEdit2, 1, 1, 1, 1 )
        self.label3 = QtWidgets.QLabel( self.layoutWidget )
        self.label3.setObjectName( "label3" )
        self.gridLayout.addWidget( self.label3, 2, 0, 1, 1 )
        self.lineEdit3 = QtWidgets.QLineEdit( self.layoutWidget )
        self.lineEdit3.setObjectName( "lineEdit3" )
        self.gridLayout.addWidget( self.lineEdit3, 2, 1, 1, 1 )
        self.label4 = QtWidgets.QLabel( self.layoutWidget )
        self.label4.setObjectName( "label4" )
        self.gridLayout.addWidget( self.label4, 3, 0, 1, 1 )
        self.lineEdit4 = QtWidgets.QLineEdit( self.layoutWidget )
        self.lineEdit4.setObjectName( "lineEdit4" )
        self.gridLayout.addWidget( self.lineEdit4, 3, 1, 1, 1 )
        MainWindow.setCentralWidget( self.centralwidget )
        self.menubar = QtWidgets.QMenuBar( MainWindow )
        self.menubar.setGeometry( QtCore.QRect( 0, 0, 408, 21 ) )
        self.menubar.setObjectName( "menubar" )
        MainWindow.setMenuBar( self.menubar )
        self.statusbar = QtWidgets.QStatusBar( MainWindow )
        self.statusbar.setObjectName( "statusbar" )
        MainWindow.setStatusBar( self.statusbar )
        self.retranslateUi( MainWindow )
        QtCore.QMetaObject.connectSlotsByName( MainWindow )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle( _translate( "MainWindow", "Güncelleme" ) )
        self.pushButton.setText( _translate( "MainWindow", "Güncelle" ) )
        self.label.setText( _translate( "MainWindow", "Adı" ) )
        self.label2.setText( _translate( "MainWindow", "Yazarı" ) )
        self.label3.setText( _translate( "MainWindow", "Yayınevi" ) )
        self.label4.setText( _translate( "MainWindow", "Türü" ) )
        self.getir()
        self.pushButton.clicked.connect(self.guncelle)

    def idgetir(self):
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "select kitapid from `geciciid` where id=1"
        imlec.execute( sqlsorgu )
        return imlec.fetchone( )[0]

    def getir(self):
        id1=self.idgetir()
        # print(id1)
        imlec = baglanti.bag.cursor( )
        sqlsorgu = "SELECT * FROM `envanter` WHERE `id`=" + str(id1)
        # print(sqlsorgu)
        imlec.execute( sqlsorgu )
        A=[]
        for i in imlec.fetchall( ):
            for j in i:
                A.append(j)
        self.lineEdit.setText(str(A[0]))
        self.lineEdit2.setText(A[1])
        self.lineEdit3.setText(A[2])
        self.lineEdit4.setText(A[3])
        
    def guncelle(self):
        print("g")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication( sys.argv )
    MainWindow = QtWidgets.QMainWindow( )
    ui = Ui_MainWindow( )
    ui.setupUi( MainWindow )
    MainWindow.show( )
    try:
        sys.exit( app.exec_( ) )
    except:
        print( "Exiting" )
