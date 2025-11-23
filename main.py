# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from Dokter import form_dokter
from Pasien import form_pasien
from Poliklinik import form_poliklinik
from Jadwal import form_jadwal

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formUtama = loader.load(ui_file, self)
        ui_file.close()

        if hasattr(self.formUtama, "menuBar"):
            self.setMenuBar(self.formUtama.menuBar())

        self.setCentralWidget(self.formUtama)
        self.resize(self.formUtama.size())


        self.formUtama.actionDokter.triggered.connect(self.bukaDokter)
        self.formUtama.actionPasien.triggered.connect(self.bukaPasien)
        self.formUtama.actionPoliKlinik.triggered.connect(self.bukaPoliklinik)
        self.formUtama.actionJadwal.triggered.connect(self.bukaJadwal)



    def bukaDokter(self):
        self.buka = form_dokter()
        self.buka.show()


    def bukaPasien(self):
        self.buka = form_pasien()
        self.buka.show()

    def bukaPoliklinik(self):
        self.buka = form_poliklinik()
        self.buka.show()

    def bukaJadwal(self):
        self.buka = form_jadwal()
        self.buka.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
