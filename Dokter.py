from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crud_dokter import crud
import os
import platform


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
        self.formDokter.btnCetak.clicked.connect(self.cetaklapDokter)
        self.formDokter.lineCari.textChanged.connect(self.filterDataDokter)

        # Klik tabel
        self.formDokter.tableWidget.cellClicked.connect(self.getDataFromTable)

        self.tampilDataDokter()
        self.show()

    # ================= TAMPIL DATA =================
    def tampilDataDokter(self):
        table = self.formDokter.tableWidget
        table.setRowCount(0)
        data = self.mycrud.TampilDataDokter()
        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pemeriksa"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pemeriksa"]))
            table.setItem(i, 2, QTableWidgetItem(baris["jabatan"]))

    # ================= FILTER =================
    def filterDataDokter(self):
        varCari = self.formDokter.lineCari.text()
        table = self.formDokter.tableWidget
        table.setRowCount(0)
        data = self.mycrud.cariDataDokter(varCari)
        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_pemeriksa"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_pemeriksa"]))
            table.setItem(i, 2, QTableWidgetItem(baris["jabatan"]))

    # ================= AMBIL DATA TABEL =================
    def getDataFromTable(self, row, column):
        table = self.formDokter.tableWidget
        self.formDokter.Editid.setText(table.item(row, 0).text())
        self.formDokter.EditNama.setText(table.item(row, 1).text())
        self.formDokter.cmbJabatan.setCurrentText(table.item(row, 2).text())

    # ================= SIMPAN =================
    def doSimpanDokter(self):
        self.mycrud.simpanDokter(
            self.formDokter.EditNama.text(),
            self.formDokter.cmbJabatan.currentText()
        )
        QMessageBox.information(None, "Info", "Data berhasil disimpan")
        self.tampilDataDokter()

    # ================= UBAH =================
    def doUbahDokter(self):
        if self.formDokter.Editid.text():
            self.mycrud.editDokter(
                self.formDokter.Editid.text(),
                self.formDokter.EditNama.text(),
                self.formDokter.cmbJabatan.currentText()
            )
            QMessageBox.information(None, "Info", "Data berhasil diubah")
            self.tampilDataDokter()

    # ================= HAPUS =================
    def doHapusDokter(self):
        if self.formDokter.Editid.text():
            self.mycrud.hapusDokter(self.formDokter.Editid.text())
            QMessageBox.information(None, "Info", "Data berhasil dihapus")
            self.tampilDataDokter()

    # ================= CETAK =================
    def cetaklapDokter(self):
        try:
            pdf = self.mycrud.laporanSemuaDokter()
            QMessageBox.information(None, "Sukses", f"Laporan dicetak:\n{pdf}")
            self.bukaPDF(pdf)
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))

    # ================= BUKA PDF =================
    def bukaPDF(self, filename):
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":
            os.system(f'open "{filename}"')
        else:
            os.system(f'xdg-open "{filename}"')
