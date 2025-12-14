# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPoliKlinik.ui'
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
        Form.resize(662, 573)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 100, 481, 131))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPoliklinikLabel = QLabel(self.formLayoutWidget)
        self.iDPoliklinikLabel.setObjectName(u"iDPoliklinikLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPoliklinikLabel)

        self.EditPoli = QLineEdit(self.formLayoutWidget)
        self.EditPoli.setObjectName(u"EditPoli")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditPoli)

        self.namaPoliklinikLabel = QLabel(self.formLayoutWidget)
        self.namaPoliklinikLabel.setObjectName(u"namaPoliklinikLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPoliklinikLabel)

        self.cmbPoli = QComboBox(self.formLayoutWidget)
        self.cmbPoli.addItem("")
        self.cmbPoli.addItem("")
        self.cmbPoli.addItem("")
        self.cmbPoli.addItem("")
        self.cmbPoli.addItem("")
        self.cmbPoli.setObjectName(u"cmbPoli")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbPoli)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.EditKeterangan = QLineEdit(self.formLayoutWidget)
        self.EditKeterangan.setObjectName(u"EditKeterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditKeterangan)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(110, 270, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(220, 270, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(330, 270, 90, 29))
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
        self.tableWidget.setGeometry(QRect(80, 350, 491, 192))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(82, 310, 491, 28))
        self.btnCetak = QPushButton(Form)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(440, 270, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPoliklinikLabel.setText(QCoreApplication.translate("Form", u"ID Poliklinik", None))
        self.namaPoliklinikLabel.setText(QCoreApplication.translate("Form", u"Nama Poliklinik", None))
        self.cmbPoli.setItemText(0, QCoreApplication.translate("Form", u"Pelayanan konsultasi dan administrasi", None))
        self.cmbPoli.setItemText(1, QCoreApplication.translate("Form", u"Pelayanan kesehatan dasar umum", None))
        self.cmbPoli.setItemText(2, QCoreApplication.translate("Form", u"Pelayanan kesehatan gigi dan mulut", None))
        self.cmbPoli.setItemText(3, QCoreApplication.translate("Form", u"Pelayanan kesehatan anak (pediatri)", None))
        self.cmbPoli.setItemText(4, QCoreApplication.translate("Form", u"Pelayanan obstetri dan ginekologi", None))

        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Poliklinik", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Poliklinik", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

