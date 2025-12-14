from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crud_pasien import crud
import os
import platform


class form_pasien(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formPasien.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPasien = loader.load(ui_file, self)
        ui_file.close()

        self.mycrud = crud()

        # ====== TOMBOL ======
        self.formPasien.btnSimpan.clicked.connect(self.doSimpanPasien)
        self.formPasien.btnUbah.clicked.connect(self.doUbahPasien)
        self.formPasien.btnHapus.clicked.connect(self.doHapusPasien)
        self.formPasien.btnCetak.clicked.connect(self.cetaklapPasien)

        # ====== FILTER & TABEL ======
        self.formPasien.lineCari.textChanged.connect(self.filterDataPasien)
        self.formPasien.tableWidget.cellClicked.connect(self.getDataFromTable)

        self.tampilDataPasien()
        self.show()

    # ================= TAMPIL DATA =================
    def tampilDataPasien(self):
        table = self.formPasien.tableWidget
        table.setRowCount(0)

        data = self.mycrud.tampilDataPasien()

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pasien"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pasien"]))
            table.setItem(i, 2, QTableWidgetItem(baris["alamat"]))
            table.setItem(i, 3, QTableWidgetItem(baris["jenis_kelamin"]))
            table.setItem(i, 4, QTableWidgetItem(str(baris["tgl_lahir"])))
            table.setItem(i, 5, QTableWidgetItem(baris["tmp_lahir"]))
            table.setItem(i, 6, QTableWidgetItem(baris["no_hp"]))
            table.setItem(i, 7, QTableWidgetItem(baris["jenis_pasien"]))

    # ================= FILTER DATA =================
    def filterDataPasien(self):
        keyword = self.formPasien.lineCari.text()
        table = self.formPasien.tableWidget
        table.setRowCount(0)

        data = self.mycrud.cariDataPasien(keyword)

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pasien"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pasien"]))
            table.setItem(i, 2, QTableWidgetItem(baris["alamat"]))
            table.setItem(i, 3, QTableWidgetItem(baris["jenis_kelamin"]))
            table.setItem(i, 4, QTableWidgetItem(str(baris["tgl_lahir"])))
            table.setItem(i, 5, QTableWidgetItem(baris["tmp_lahir"]))
            table.setItem(i, 6, QTableWidgetItem(baris["no_hp"]))
            table.setItem(i, 7, QTableWidgetItem(baris["jenis_pasien"]))

    # ================= AMBIL DATA DARI TABEL =================
    def getDataFromTable(self, row, column):
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

    # ================= SIMPAN =================
    def doSimpanPasien(self):
        self.mycrud.simpanPasien(
            self.formPasien.EditNama.text(),
            self.formPasien.EditAlamat.text(),
            self.formPasien.cmbJekel.currentText(),
            self.formPasien.EditDate.date().toString("yyyy-MM-dd"),
            self.formPasien.EditLahir.text(),
            self.formPasien.EditPhone.text(),
            self.formPasien.cmbPasien.currentText()
        )
        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
        self.tampilDataPasien()

    # ================= UBAH =================
    def doUbahPasien(self):
        tempid = self.formPasien.EditPasien.text()
        if tempid:
            self.mycrud.ubahPasien(
                tempid,
                self.formPasien.EditNama.text(),
                self.formPasien.EditAlamat.text(),
                self.formPasien.cmbJekel.currentText(),
                self.formPasien.EditDate.date().toString("yyyy-MM-dd"),
                self.formPasien.EditLahir.text(),
                self.formPasien.EditPhone.text(),
                self.formPasien.cmbPasien.currentText()
            )
            QMessageBox.information(None, "Informasi", "Data berhasil diubah")
            self.tampilDataPasien()

    # ================= HAPUS =================
    def doHapusPasien(self):
        tempid = self.formPasien.EditPasien.text()
        if tempid:
            self.mycrud.hapusPasien(tempid)
            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")
            self.tampilDataPasien()

    # ================= CETAK =================
    def cetaklapPasien(self):
        pdf = self.mycrud.laporanSemuaPasien()
        QMessageBox.information(self, "Sukses", f"Laporan dicetak:\n{pdf}")
        self.bukaPDF(pdf)

    # ================= BUKA PDF =================
    def bukaPDF(self, filename):
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":
            os.system(f'open "{filename}"')
        else:
            os.system(f'xdg-open "{filename}"')
