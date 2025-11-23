from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crud_poliklinik import crud


class form_poliklinik(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        ui_file = QFile("formPoliKlinik.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPoli = loader.load(ui_file, self)
        ui_file.close()

        # CRUD
        self.mycrud = crud()

        # Event Button
        self.formPoli.btnSimpan.clicked.connect(self.doSimpanPoli)
        self.formPoli.btnUbah.clicked.connect(self.doUbahPoli)
        self.formPoli.btnHapus.clicked.connect(self.doHapusPoli)

        # Event Cari
        self.formPoli.lineCari.textChanged.connect(self.filterDataPoli)

        # Klik tabel
        self.formPoli.tableWidget.cellClicked.connect(self.getDataFromTable)

        # Load awal
        self.tampilDataPoli()
        self.show()

    # ===================================================
    # TAMPILKAN DATA
    # ===================================================
    def tampilDataPoli(self):
        table = self.formPoli.tableWidget
        table.setRowCount(0)

        data = self.mycrud.tampilDataPoli()

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_poli"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_poli"]))
            table.setItem(i, 2, QTableWidgetItem(baris["keterangan"]))

    # ===================================================
    # FILTER DATA
    # ===================================================
    def filterDataPoli(self):
        varCari = self.formPoli.lineCari.text()
        table = self.formPoli.tableWidget
        table.setRowCount(0)

        data = self.mycrud.cariDataPoli(varCari)

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_poli"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_poli"]))
            table.setItem(i, 2, QTableWidgetItem(baris["keterangan"]))

    # ===================================================
    # PILIH DATA TABEL
    # ===================================================
    def getDataFromTable(self, row, column):
        table = self.formPoli.tableWidget

        self.formPoli.EditPoli.setText(table.item(row, 0).text())
        self.formPoli.cmbPoli.setCurrentText(table.item(row, 1).text())
        self.formPoli.EditKeterangan.setText(table.item(row, 2).text())

    # ===================================================
    # SIMPAN DATA
    # ===================================================
    def doSimpanPoli(self):
        nama = self.formPoli.cmbPoli.currentText()
        ket  = self.formPoli.EditKeterangan.text()

        self.mycrud.simpanPoli(nama, ket)

        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
        self.tampilDataPoli()

    # ===================================================
    # UBAH DATA
    # ===================================================
    def doUbahPoli(self):
        tempid = self.formPoli.EditPoli.text()
        nama   = self.formPoli.cmbPoli.currentText()
        ket    = self.formPoli.EditKeterangan.text()

        if tempid != "":
            self.mycrud.ubahPoli(tempid, nama, ket)

            QMessageBox.information(None, "Informasi", "Data berhasil diubah")
            self.tampilDataPoli()

    # ===================================================
    # HAPUS DATA
    # ===================================================
    def doHapusPoli(self):
        tempid = self.formPoli.EditPoli.text()

        if tempid != "":
            self.mycrud.hapusPoli(tempid)

            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")
            self.tampilDataPoli()
