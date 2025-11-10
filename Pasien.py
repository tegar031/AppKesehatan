from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crud_pasien import crud


class form_pasien(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formPasien.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPasien = loader.load(ui_file, self)
        ui_file.close()

        self.mycrud = crud()

        # Button Events
        self.formPasien.btnSimpan.clicked.connect(self.doSimpanData)
        self.formPasien.btnUbah.clicked.connect(self.doUbahData)
        self.formPasien.btnHapus.clicked.connect(self.doHapusData)

        # Table click
        self.formPasien.tableWidget.cellClicked.connect(self.getDataFromTable)

        self.loadData()
        self.show()


    def loadData(self):
        data = self.mycrud.tampilPasien()
        table = self.formPasien.tableWidget
        table.setRowCount(0)

        for row_number, row_data in enumerate(data):
            table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                table.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))


    def doSimpanData(self):
        tempnama = self.formPasien.EditNama.text().strip()
        tempalamat = self.formPasien.EditAlamat.text().strip()
        tempjekel = self.formPasien.cmbJekel.currentText()
        temptgl = self.formPasien.EditDate.date().toString("yyyy-MM-dd")
        temptempat = self.formPasien.EditLahir.text().strip()
        tempphone = self.formPasien.EditPhone.text().strip()
        tempjenis = self.formPasien.cmbPasien.currentText()

        if tempnama == "" or tempalamat == "":
            QMessageBox.warning(self, "Warning", "Nama dan Alamat tidak boleh kosong!")
            return

        self.mycrud.simpanPasien(tempnama, tempalamat, tempjekel,
                                 temptgl, temptempat, tempphone, tempjenis)

        self.loadData()
        self.resetForm()


    def getDataFromTable(self, row):
        table = self.formPasien.tableWidget

        self.formPasien.EditPasien.setText(table.item(row, 0).text())
        self.formPasien.EditNama.setText(table.item(row, 1).text())
        self.formPasien.EditAlamat.setText(table.item(row, 2).text())
        self.formPasien.cmbJekel.setCurrentText(table.item(row, 3).text())

        tgl = QDate.fromString(table.item(row, 4).text(), "yyyy-MM-dd")
        if tgl.isValid():
            self.formPasien.EditDate.setDate(tgl)

        self.formPasien.EditLahir.setText(table.item(row, 5).text())
        self.formPasien.EditPhone.setText(table.item(row, 6).text())
        self.formPasien.cmbPasien.setCurrentText(table.item(row, 7).text())


    def doUbahData(self):
        tempid = self.formPasien.EditPasien.text()

        if tempid == "":
            QMessageBox.warning(self, "Error", "Pilih data pada tabel terlebih dahulu!")
            return

        tempnama = self.formPasien.EditNama.text()
        tempalamat = self.formPasien.EditAlamat.text()
        tempjekel = self.formPasien.cmbJekel.currentText()
        temptgl = self.formPasien.EditDate.date().toString("yyyy-MM-dd")
        temptempat = self.formPasien.EditLahir.text()
        tempphone = self.formPasien.EditPhone.text()
        tempjenis = self.formPasien.cmbPasien.currentText()

        self.mycrud.ubahPasien(tempid, tempnama, tempalamat, tempjekel,
                               temptgl, temptempat, tempphone, tempjenis)

        self.loadData()
        self.resetForm()


    def doHapusData(self):
        tempid = self.formPasien.EditPasien.text()

        if tempid == "":
            QMessageBox.warning(self, "Error", "Pilih data yang ingin dihapus!")
            return

        self.mycrud.hapusPasien(tempid)
        self.loadData()
        self.resetForm()


    def resetForm(self):
        self.formPasien.EditPasien.clear()
        self.formPasien.EditNama.clear()
        self.formPasien.EditAlamat.clear()
        self.formPasien.EditLahir.clear()
        self.formPasien.EditPhone.clear()
        self.formPasien.cmbJekel.setCurrentIndex(0)
        self.formPasien.cmbPasien.setCurrentIndex(0)
        self.formPasien.EditDate.setDate(QDate.currentDate())
