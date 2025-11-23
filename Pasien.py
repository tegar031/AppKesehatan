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

        # Tombol
        self.formPasien.btnSimpan.clicked.connect(self.doSimpanPasien)
        self.formPasien.btnUbah.clicked.connect(self.doUbahPasien)
        self.formPasien.btnHapus.clicked.connect(self.doHapusPasien)

        # Pencarian
        self.formPasien.lineCari.textChanged.connect(self.filterDataPasien)

        # Klik tabel
        self.formPasien.tableWidget.cellClicked.connect(self.getDataFromTable)

        # Load data awal
        self.tampilDataPasien()
        self.show()

    # ===================================================
    # TAMPIL DATA
    # ===================================================
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

    # ===================================================
    # FILTER DATA
    # ===================================================
    def filterDataPasien(self):
        varCari = self.formPasien.lineCari.text()
        table = self.formPasien.tableWidget
        table.setRowCount(0)

        data = self.mycrud.cariDataPasien(varCari)

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

    # ===================================================
    # GET DATA DARI TABEL
    # ===================================================
    def getDataFromTable(self, row, column):
        table = self.formPasien.tableWidget

        self.formPasien.EditPasien.setText(table.item(row, 0).text())  # ID
        self.formPasien.EditNama.setText(table.item(row, 1).text())    # Nama
        self.formPasien.EditAlamat.setText(table.item(row, 2).text())  # Alamat
        self.formPasien.cmbJekel.setCurrentText(table.item(row, 3).text())

        # Tanggal lahir
        tgl_str = table.item(row, 4).text()
        tgl = QDate.fromString(tgl_str, "yyyy-MM-dd")
        if tgl.isValid():
            self.formPasien.EditDate.setDate(tgl)

        # Tempat lahir
        self.formPasien.EditLahir.setText(table.item(row, 5).text())

        # No HP
        self.formPasien.EditPhone.setText(table.item(row, 6).text())

        # Jenis pasien
        self.formPasien.cmbPasien.setCurrentText(table.item(row, 7).text())

    # ===================================================
    # SIMPAN DATA
    # ===================================================
    def doSimpanPasien(self):
        nama = self.formPasien.EditNama.text()
        alamat = self.formPasien.EditAlamat.text()
        jk = self.formPasien.cmbJekel.currentText()
        tgl = self.formPasien.EditDate.date().toString("yyyy-MM-dd")
        tmp = self.formPasien.EditLahir.text()
        hp = self.formPasien.EditPhone.text()
        jenis = self.formPasien.cmbPasien.currentText()

        self.mycrud.simpanPasien(nama, alamat, jk, tgl, tmp, hp, jenis)

        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
        self.tampilDataPasien()

    # ===================================================
    # UBAH DATA
    # ===================================================
    def doUbahPasien(self):
        tempid = self.formPasien.EditPasien.text()
        nama = self.formPasien.EditNama.text()
        alamat = self.formPasien.EditAlamat.text()
        jk = self.formPasien.cmbJekel.currentText()
        tgl = self.formPasien.EditDate.date().toString("yyyy-MM-dd")
        tmp = self.formPasien.EditLahir.text()
        hp = self.formPasien.EditPhone.text()
        jenis = self.formPasien.cmbPasien.currentText()

        if tempid != "":
            self.mycrud.ubahPasien(tempid, nama, alamat, jk, tgl, tmp, hp, jenis)

            QMessageBox.information(None, "Informasi", "Data berhasil diubah")
            self.tampilDataPasien()

    # ===================================================
    # HAPUS DATA
    # ===================================================
    def doHapusPasien(self):
        tempid = self.formPasien.EditPasien.text()

        if tempid != "":
            self.mycrud.hapusPasien(tempid)

            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")
            self.tampilDataPasien()
