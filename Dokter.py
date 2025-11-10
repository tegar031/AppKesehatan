from PySide6.QtWidgets import QWidget, QTableWidgetItem
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
        self.formDokter.btnSimpan.clicked.connect(self.doSimpanAnggota)
        self.formDokter.btnUbah.clicked.connect(self.doUbahAnggota)
        self.formDokter.btnHapus.clicked.connect(self.doHapusAnggota)

        # Klik tabel → isi form
        self.formDokter.tableWidget.cellClicked.connect(self.getDataFromTable)

        self.loadData()
        self.show()

    # TAMPIL DATA
    def loadData(self):
        data = self.mycrud.tampilDokter()
        table = self.formDokter.tableWidget
        table.setRowCount(0)

        for row_number, row_data in enumerate(data):
            table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                table.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

    # SIMPAN DATA
    def doSimpanAnggota(self):
        tempnama = self.formDokter.EditNama.text()
        tempjabatan = self.formDokter.cmbJabatan.currentText()
        self.mycrud.simpanDokter(tempnama, tempjabatan)
        self.loadData()

    # PILIH DATA PADA TABEL → TAMPIL DI FORM
    def getDataFromTable(self, row, column):
        table = self.formDokter.tableWidget
        self.formDokter.Editid.setText(table.item(row, 0).text())
        self.formDokter.EditNama.setText(table.item(row, 1).text())
        self.formDokter.cmbJabatan.setCurrentText(table.item(row, 2).text())

    # UBAH DATA
    def doUbahAnggota(self):
        tempid = self.formDokter.Editid.text()
        tempnama = self.formDokter.EditNama.text()
        tempjabatan = self.formDokter.cmbJabatan.currentText()
        if tempid != "":
            self.mycrud.ubahDokter(tempid, tempnama, tempjabatan)
            self.loadData()

    # HAPUS DATA
    def doHapusAnggota(self):
        tempid = self.formDokter.Editid.text()
        if tempid != "":
            self.mycrud.hapusDokter(tempid)
            self.loadData()
