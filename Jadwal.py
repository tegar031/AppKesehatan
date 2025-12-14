from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTime
from crud_jadwal import crud_jadwal
import os
import platform



class form_jadwal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load UI
        ui_file = QFile("formJadwal.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.form = loader.load(ui_file, self)
        ui_file.close()

        # CRUD
        self.mycrud = crud_jadwal()

        # Buttons
        self.form.btnSimpan.clicked.connect(self.doSimpan)
        self.form.btnUbah.clicked.connect(self.doUbah)
        self.form.btnHapus.clicked.connect(self.doHapus)
        self.form.lineCari.textChanged.connect(self.filterData)
        self.form.btnCetak.clicked.connect(self.cetaklapJadwal)


        # Table click
        self.form.tableWidget.cellClicked.connect(self.getDataFromTable)

        # Load awal
        self.tampilData()
        self.show()

    # ==================================================
    # TAMPIL DATA
    # ==================================================
    def tampilData(self):
        t = self.form.tableWidget
        t.setRowCount(0)

        data = self.mycrud.tampilData()

        for i, row in enumerate(data):
            t.insertRow(i)
            t.setItem(i, 0, QTableWidgetItem(str(row["id_jadwal"])))
            t.setItem(i, 1, QTableWidgetItem(str(row["id_poli"])))
            t.setItem(i, 2, QTableWidgetItem(str(row["id_pemeriksa"])))
            t.setItem(i, 3, QTableWidgetItem(str(row["jam_mulai"])))
            t.setItem(i, 4, QTableWidgetItem(str(row["jam_selesai"])))
            t.setItem(i, 5, QTableWidgetItem(str(row["hari"])))

    # ==================================================
    # FILTER DATA
    # ==================================================
    def filterData(self):
        cari = self.form.lineCari.text()
        t = self.form.tableWidget
        t.setRowCount(0)

        data = self.mycrud.cariData(cari)

        for i, row in enumerate(data):
            t.insertRow(i)
            t.setItem(i, 0, QTableWidgetItem(str(row["id_jadwal"])))
            t.setItem(i, 1, QTableWidgetItem(str(row["id_poli"])))
            t.setItem(i, 2, QTableWidgetItem(str(row["id_pemeriksa"])))
            t.setItem(i, 3, QTableWidgetItem(str(row["jam_mulai"])))
            t.setItem(i, 4, QTableWidgetItem(str(row["jam_selesai"])))
            t.setItem(i, 5, QTableWidgetItem(str(row["hari"])))

    # ==================================================
    # GET DATA FROM TABLE
    # ==================================================
    def getDataFromTable(self, row):
        t = self.form.tableWidget

        self.form.EditJadwal.setText(t.item(row, 0).text())
        self.form.EditPoli.setText(t.item(row, 1).text())
        self.form.EditPeriksa.setText(t.item(row, 2).text())

        jam_mulai = t.item(row, 3).text()
        jam_selesai = t.item(row, 4).text()

        self.form.TimeMulai.setTime(QTime.fromString(jam_mulai, "HH:mm"))
        self.form.EditSelesai.setTime(QTime.fromString(jam_selesai, "HH:mm"))

        self.form.cmbHari.setCurrentText(t.item(row, 5).text())

    # ==================================================
    # SIMPAN
    # ==================================================
    def doSimpan(self):
        id_poli = self.form.EditPoli.text()
        id_pemeriksa = self.form.EditPeriksa.text()
        jam_mulai = self.form.TimeMulai.time().toString("HH:mm")
        jam_selesai = self.form.EditSelesai.time().toString("HH:mm")
        hari = self.form.cmbHari.currentText()

        self.mycrud.insertData(id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari)

        QMessageBox.information(self, "Informasi", "Data berhasil disimpan")
        self.tampilData()

    # ==================================================
    # UBAH
    # ==================================================
    def doUbah(self):
        id_jadwal = self.form.EditJadwal.text()
        if id_jadwal == "":
            return

        id_poli = self.form.EditPoli.text()
        id_pemeriksa = self.form.EditPeriksa.text()
        jam_mulai = self.form.TimeMulai.time().toString("HH:mm")
        jam_selesai = self.form.EditSelesai.time().toString("HH:mm")
        hari = self.form.cmbHari.currentText()

        self.mycrud.updateData(id_jadwal, id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari)

        QMessageBox.information(self, "Informasi", "Data berhasil diubah")
        self.tampilData()

    # ==================================================
    # HAPUS
    # ==================================================
    def doHapus(self):
        id_jadwal = self.form.EditJadwal.text()
        if id_jadwal == "":
            return

        self.mycrud.deleteData(id_jadwal)
        QMessageBox.information(self, "Informasi", "Data berhasil dihapus")
        self.tampilData()


    # ================= CETAK =================
    def cetaklapJadwal(self):
        try:
            pdf = self.mycrud.laporanSemuaJadwal()
            QMessageBox.information(self, "Sukses", f"Laporan dicetak:\n{pdf}")
            self.bukaPDF(pdf)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


    # ================= BUKA PDF =================
    def bukaPDF(self, filename):
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":
            os.system(f'open "{filename}"')
        else:
            os.system(f'xdg-open "{filename}"')
