from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crud_poliklinik import crud
import os
import platform


class form_poliklinik(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("formPoliKlinik.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPoli = loader.load(ui_file, self)
        ui_file.close()

        self.mycrud = crud()

        # Event tombol (SAMA SEPERTI DOKTER)
        self.formPoli.btnSimpan.clicked.connect(self.doSimpanPoli)
        self.formPoli.btnUbah.clicked.connect(self.doUbahPoli)
        self.formPoli.btnHapus.clicked.connect(self.doHapusPoli)
        self.formPoli.btnCetak.clicked.connect(self.cetaklapPoli)
        self.formPoli.lineCari.textChanged.connect(self.filterDataPoli)

        # Klik tabel
        self.formPoli.tableWidget.cellClicked.connect(self.getDataFromTable)

        self.tampilDataPoli()
        self.show()

    # ================= TAMPIL DATA =================
    def tampilDataPoli(self):
        table = self.formPoli.tableWidget
        table.setRowCount(0)
        data = self.mycrud.tampilDataPoli()

        for i, baris in enumerate(data):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(baris["id_poli"])))
            table.setItem(i, 1, QTableWidgetItem(baris["nama_poli"]))
            table.setItem(i, 2, QTableWidgetItem(baris["keterangan"]))

    # ================= FILTER =================
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

    # ================= AMBIL DATA TABEL =================
    def getDataFromTable(self, row, column):
        table = self.formPoli.tableWidget
        self.formPoli.EditPoli.setText(table.item(row, 0).text())
        self.formPoli.cmbPoli.setCurrentText(table.item(row, 1).text())
        self.formPoli.EditKeterangan.setText(table.item(row, 2).text())

    # ================= SIMPAN =================
    def doSimpanPoli(self):
        self.mycrud.simpanPoli(
            self.formPoli.cmbPoli.currentText(),
            self.formPoli.EditKeterangan.text()
        )
        QMessageBox.information(None, "Info", "Data berhasil disimpan")
        self.tampilDataPoli()

    # ================= UBAH =================
    def doUbahPoli(self):
        if self.formPoli.EditPoli.text():
            self.mycrud.ubahPoli(
                self.formPoli.EditPoli.text(),
                self.formPoli.cmbPoli.currentText(),
                self.formPoli.EditKeterangan.text()
            )
            QMessageBox.information(None, "Info", "Data berhasil diubah")
            self.tampilDataPoli()

    # ================= HAPUS =================
    def doHapusPoli(self):
        if self.formPoli.EditPoli.text():
            self.mycrud.hapusPoli(self.formPoli.EditPoli.text())
            QMessageBox.information(None, "Info", "Data berhasil dihapus")
            self.tampilDataPoli()

    # ================= CETAK =================
    def cetaklapPoli(self):
        try:
            pdf = self.mycrud.laporanSemuaPoli()
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
