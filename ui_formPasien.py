# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formPasien.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(841, 636)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(130, 40, 601, 303))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPasienLabel = QLabel(self.formLayoutWidget)
        self.iDPasienLabel.setObjectName(u"iDPasienLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPasienLabel)

        self.EditPasien = QLineEdit(self.formLayoutWidget)
        self.EditPasien.setObjectName(u"EditPasien")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.EditPasien)

        self.namaPasienLabel = QLabel(self.formLayoutWidget)
        self.namaPasienLabel.setObjectName(u"namaPasienLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPasienLabel)

        self.EditNama = QLineEdit(self.formLayoutWidget)
        self.EditNama.setObjectName(u"EditNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.EditNama)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.EditAlamat = QLineEdit(self.formLayoutWidget)
        self.EditAlamat.setObjectName(u"EditAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.EditAlamat)

        self.jenisKelaminLabel = QLabel(self.formLayoutWidget)
        self.jenisKelaminLabel.setObjectName(u"jenisKelaminLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jenisKelaminLabel)

        self.cmbJekel = QComboBox(self.formLayoutWidget)
        self.cmbJekel.addItem("")
        self.cmbJekel.addItem("")
        self.cmbJekel.setObjectName(u"cmbJekel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbJekel)

        self.tanggalLahirLabel = QLabel(self.formLayoutWidget)
        self.tanggalLahirLabel.setObjectName(u"tanggalLahirLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tanggalLahirLabel)

        self.tempatLahirLabel = QLabel(self.formLayoutWidget)
        self.tempatLahirLabel.setObjectName(u"tempatLahirLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.tempatLahirLabel)

        self.EditLahir = QLineEdit(self.formLayoutWidget)
        self.EditLahir.setObjectName(u"EditLahir")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.EditLahir)

        self.noHandPhoneLabel = QLabel(self.formLayoutWidget)
        self.noHandPhoneLabel.setObjectName(u"noHandPhoneLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.noHandPhoneLabel)

        self.EditPhone = QLineEdit(self.formLayoutWidget)
        self.EditPhone.setObjectName(u"EditPhone")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.EditPhone)

        self.jenisPasienLabel = QLabel(self.formLayoutWidget)
        self.jenisPasienLabel.setObjectName(u"jenisPasienLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.jenisPasienLabel)

        self.cmbPasien = QComboBox(self.formLayoutWidget)
        self.cmbPasien.addItem("")
        self.cmbPasien.addItem("")
        self.cmbPasien.setObjectName(u"cmbPasien")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cmbPasien)

        self.EditDate = QDateEdit(self.formLayoutWidget)
        self.EditDate.setObjectName(u"EditDate")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.EditDate)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(280, 370, 90, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(390, 370, 90, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(500, 370, 90, 29))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 420, 771, 192))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(96)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPasienLabel.setText(QCoreApplication.translate("Form", u"ID Pasien", None))
        self.namaPasienLabel.setText(QCoreApplication.translate("Form", u"Nama Pasien", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.jenisKelaminLabel.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None))
        self.cmbJekel.setItemText(0, QCoreApplication.translate("Form", u"Laki - Laki", None))
        self.cmbJekel.setItemText(1, QCoreApplication.translate("Form", u"Perempuan", None))

        self.tanggalLahirLabel.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None))
        self.tempatLahirLabel.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None))
        self.noHandPhoneLabel.setText(QCoreApplication.translate("Form", u"No HandPhone", None))
        self.jenisPasienLabel.setText(QCoreApplication.translate("Form", u"Jenis Pasien", None))
        self.cmbPasien.setItemText(0, QCoreApplication.translate("Form", u"BPJS", None))
        self.cmbPasien.setItemText(1, QCoreApplication.translate("Form", u"Umum", None))

        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pasien", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Pasien", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jenis Kelamin", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal Lahir", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tempat Lahir", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"No HandPhone", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Jenis Pasien", None));
    # retranslateUi

