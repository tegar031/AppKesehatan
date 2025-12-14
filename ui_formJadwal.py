# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formJadwal.ui'
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
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(705, 638)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 50, 551, 211))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDJadwalLabel = QLabel(self.formLayoutWidget)
        self.iDJadwalLabel.setObjectName(u"iDJadwalLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDJadwalLabel)

        self.EditJadwal = QLineEdit(self.formLayoutWidget)
        self.EditJadwal.setObjectName(u"EditJadwal")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditJadwal)

        self.iDPoliklinikLabel = QLabel(self.formLayoutWidget)
        self.iDPoliklinikLabel.setObjectName(u"iDPoliklinikLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDPoliklinikLabel)

        self.EditPoli = QLineEdit(self.formLayoutWidget)
        self.EditPoli.setObjectName(u"EditPoli")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditPoli)

        self.iDPemeriksaLabel = QLabel(self.formLayoutWidget)
        self.iDPemeriksaLabel.setObjectName(u"iDPemeriksaLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.iDPemeriksaLabel)

        self.EditPeriksa = QLineEdit(self.formLayoutWidget)
        self.EditPeriksa.setObjectName(u"EditPeriksa")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditPeriksa)

        self.jamMulaiLabel = QLabel(self.formLayoutWidget)
        self.jamMulaiLabel.setObjectName(u"jamMulaiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jamMulaiLabel)

        self.TimeMulai = QTimeEdit(self.formLayoutWidget)
        self.TimeMulai.setObjectName(u"TimeMulai")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.TimeMulai)

        self.jamSelesaiLabel = QLabel(self.formLayoutWidget)
        self.jamSelesaiLabel.setObjectName(u"jamSelesaiLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jamSelesaiLabel)

        self.EditSelesai = QTimeEdit(self.formLayoutWidget)
        self.EditSelesai.setObjectName(u"EditSelesai")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.EditSelesai)

        self.hariLabel = QLabel(self.formLayoutWidget)
        self.hariLabel.setObjectName(u"hariLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.hariLabel)

        self.cmbHari = QComboBox(self.formLayoutWidget)
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.addItem("")
        self.cmbHari.setObjectName(u"cmbHari")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.cmbHari)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(110, 290, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(250, 290, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(390, 290, 90, 29))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(90, 350, 551, 28))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(90, 420, 551, 191))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(93)
        self.btnCetak = QPushButton(Form)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(520, 290, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDJadwalLabel.setText(QCoreApplication.translate("Form", u"ID Jadwal", None))
        self.iDPoliklinikLabel.setText(QCoreApplication.translate("Form", u"ID Poliklinik", None))
        self.iDPemeriksaLabel.setText(QCoreApplication.translate("Form", u"ID Pemeriksa", None))
        self.jamMulaiLabel.setText(QCoreApplication.translate("Form", u"Jam Mulai", None))
        self.jamSelesaiLabel.setText(QCoreApplication.translate("Form", u"Jam Selesai", None))
        self.hariLabel.setText(QCoreApplication.translate("Form", u"Hari", None))
        self.cmbHari.setItemText(0, QCoreApplication.translate("Form", u"Senin", None))
        self.cmbHari.setItemText(1, QCoreApplication.translate("Form", u"Selasa", None))
        self.cmbHari.setItemText(2, QCoreApplication.translate("Form", u"Rabu", None))
        self.cmbHari.setItemText(3, QCoreApplication.translate("Form", u"Kamis", None))
        self.cmbHari.setItemText(4, QCoreApplication.translate("Form", u"Jum'at", None))
        self.cmbHari.setItemText(5, QCoreApplication.translate("Form", u"Sabtu", None))
        self.cmbHari.setItemText(6, QCoreApplication.translate("Form", u"Minggu", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Jadwal", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID Poliklinik", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID Pemeriksa", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jam Mulai", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jam Selesai", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Hari", None));
        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

