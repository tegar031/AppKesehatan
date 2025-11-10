# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formDokter.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(648, 529)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(120, 90, 431, 131))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPemeriksaLabel = QLabel(self.formLayoutWidget)
        self.iDPemeriksaLabel.setObjectName(u"iDPemeriksaLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPemeriksaLabel)

        self.Editid = QLineEdit(self.formLayoutWidget)
        self.Editid.setObjectName(u"Editid")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.Editid)

        self.namaPemeriksaLabel = QLabel(self.formLayoutWidget)
        self.namaPemeriksaLabel.setObjectName(u"namaPemeriksaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPemeriksaLabel)

        self.EditNama = QLineEdit(self.formLayoutWidget)
        self.EditNama.setObjectName(u"EditNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditNama)

        self.jabatanLabel = QLabel(self.formLayoutWidget)
        self.jabatanLabel.setObjectName(u"jabatanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jabatanLabel)

        self.cmbJabatan = QComboBox(self.formLayoutWidget)
        self.cmbJabatan.addItem("")
        self.cmbJabatan.addItem("")
        self.cmbJabatan.addItem("")
        self.cmbJabatan.addItem("")
        self.cmbJabatan.addItem("")
        self.cmbJabatan.setObjectName(u"cmbJabatan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbJabatan)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(160, 270, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(290, 270, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(420, 270, 90, 29))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 310, 521, 192))
        self.tableWidget.horizontalHeader().setMinimumSectionSize(34)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(173)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPemeriksaLabel.setText(QCoreApplication.translate("Form", u"ID Pemeriksa", None))
        self.namaPemeriksaLabel.setText(QCoreApplication.translate("Form", u"Nama Pemeriksa", None))
        self.jabatanLabel.setText(QCoreApplication.translate("Form", u"Jabatan", None))
        self.cmbJabatan.setItemText(0, QCoreApplication.translate("Form", u"Kepala Puskesmas", None))
        self.cmbJabatan.setItemText(1, QCoreApplication.translate("Form", u"Dokter Umum", None))
        self.cmbJabatan.setItemText(2, QCoreApplication.translate("Form", u"Dokter Gigi", None))
        self.cmbJabatan.setItemText(3, QCoreApplication.translate("Form", u"Dokter Spesialis Anak", None))
        self.cmbJabatan.setItemText(4, QCoreApplication.translate("Form", u"Dokter Spesialis Kandungan", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pemeriksa", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Pemeriksa", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Jabatan", None));
    # retranslateUi

