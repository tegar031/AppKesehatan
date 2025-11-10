# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionDokter = QAction(Main)
        self.actionDokter.setObjectName(u"actionDokter")
        self.actionPasien = QAction(Main)
        self.actionPasien.setObjectName(u"actionPasien")
        self.actionPoliKlinik = QAction(Main)
        self.actionPoliKlinik.setObjectName(u"actionPoliKlinik")
        self.actionJadwal = QAction(Main)
        self.actionJadwal.setObjectName(u"actionJadwal")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuHalaman_Aplikasi = QMenu(self.menubar)
        self.menuHalaman_Aplikasi.setObjectName(u"menuHalaman_Aplikasi")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Aplikasi.menuAction())
        self.menuHalaman_Aplikasi.addAction(self.actionDokter)
        self.menuHalaman_Aplikasi.addAction(self.actionPasien)
        self.menuHalaman_Aplikasi.addAction(self.actionPoliKlinik)
        self.menuHalaman_Aplikasi.addAction(self.actionJadwal)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionDokter.setText(QCoreApplication.translate("Main", u"Dokter", None))
        self.actionPasien.setText(QCoreApplication.translate("Main", u"Pasien", None))
        self.actionPoliKlinik.setText(QCoreApplication.translate("Main", u"PoliKlinik", None))
        self.actionJadwal.setText(QCoreApplication.translate("Main", u"Jadwal", None))
        self.menuHalaman_Aplikasi.setTitle(QCoreApplication.translate("Main", u"Halaman Aplikasi", None))
    # retranslateUi

