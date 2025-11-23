from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crud_dokter import crud

class form_dokter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formDokter.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formDokter = loader.load(ui_file, self)
        ui_file.close()

        self.mycrud = crud()

        # Event tombol
        self.formDokter.btnSimpan.clicked.connect(self.doSimpanDokter)
        self.formDokter.btnUbah.clicked.connect(self.doUbahDokter)
        self.formDokter.btnHapus.clicked.connect(self.doHapusDokter)
        self.formDokter.lineCari.textChanged.connect(self.filterDataDokter)

        # Klik tabel
        self.formDokter.tableWidget.cellClicked.connect(self.getDataFromTable)

        # Load awal
        self.tampilDataDokter()
        self.show()

    # ===================================================
    # TAMPILKAN DATA
    # ===================================================
    def tampilDataDokter(self):
        table = self.formDokter.tableWidget
        table.setRowCount(0)

        data = self.mycrud.TampilDataDokter()  # <<< SAMA DENGAN CRUD

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pemeriksa"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pemeriksa"]))
            table.setItem(i, 2, QTableWidgetItem(baris["jabatan"]))

    # ===================================================
    # FILTER DATA
    # ===================================================
    def filterDataDokter(self):
        varCari = self.formDokter.lineCari.text()
        table = self.formDokter.tableWidget
        table.setRowCount(0)

        data = self.mycrud.cariDataDokter(varCari)   # <<< SAMA DENGAN CRUD

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pemeriksa"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pemeriksa"]))
            table.setItem(i, 2, QTableWidgetItem(baris["jabatan"]))

    # ===================================================
    # PILIH DATA TABEL
    # ===================================================
    def getDataFromTable(self, row, column):
        table = self.formDokter.tableWidget
        self.formDokter.Editid.setText(table.item(row, 0).text())
        self.formDokter.EditNama.setText(table.item(row, 1).text())
        self.formDokter.cmbJabatan.setCurrentText(table.item(row, 2).text())

    # ===================================================
    # SIMPAN DATA
    # ===================================================
    def doSimpanDokter(self):
        tempnama = self.formDokter.EditNama.text()
        tempjabatan = self.formDokter.cmbJabatan.currentText()

        self.mycrud.simpanDokter(tempnama, tempjabatan)

        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
        self.tampilDataDokter()

    # ===================================================
    # UBAH DATA
    # ===================================================
    def doUbahDokter(self):
        tempid = self.formDokter.Editid.text()
        tempnama = self.formDokter.EditNama.text()
        tempjabatan = self.formDokter.cmbJabatan.currentText()

        if tempid != "":
            self.mycrud.editDokter(tempid, tempnama, tempjabatan)

            QMessageBox.information(None, "Informasi", "Data berhasil diubah")
            self.tampilDataDokter()

    # ===================================================
    # HAPUS DATA
    # ===================================================
    def doHapusDokter(self):
        tempid = self.formDokter.Editid.text()

        if tempid != "":
            self.mycrud.hapusDokter(tempid)

            QMessageBox.information(None, "Informasi", "Data berhasil dihapus")
            self.tampilDataDokter()
