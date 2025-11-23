# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbkesehatan'
        )
        self.cursor = self.koneksi.cursor()

    # =======================================================
    # SIMPAN DATA
    # =======================================================
    def simpanDokter(self, nama, jabatan):
        cekkursor = self.koneksi.cursor()
        sql = "INSERT INTO dokter(nama_pemeriksa, jabatan) VALUES (%s, %s)"
        cekkursor.execute(sql, (nama, jabatan))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # EDIT / UBAH DATA
    # =======================================================
    def editDokter(self, id_dokter, nama, jabatan):
        cekkursor = self.koneksi.cursor()
        sql = """
            UPDATE dokter
            SET nama_pemeriksa=%s, jabatan=%s
            WHERE id_pemeriksa=%s
        """
        cekkursor.execute(sql, (nama, jabatan, id_dokter))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # HAPUS DATA
    # =======================================================
    def hapusDokter(self, id_dokter):
        cekkursor = self.koneksi.cursor()
        sql = "DELETE FROM dokter WHERE id_pemeriksa=%s"
        cekkursor.execute(sql, (id_dokter,))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # TAMPIL DATA
    # =======================================================
    def TampilDataDokter(self):
        cekkursor = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM dokter ORDER BY id_pemeriksa ASC"
        cekkursor.execute(sql)
        return cekkursor.fetchall()

    # =======================================================
    # CARI DATA
    # =======================================================
    def cariDataDokter(self, cari):
        cekkursor = self.koneksi.cursor(dictionary=True)
        sql = """
            SELECT * FROM dokter
            WHERE id_pemeriksa LIKE %s
            OR nama_pemeriksa LIKE %s
            OR jabatan LIKE %s
        """
        like = f"%{cari}%"
        cekkursor.execute(sql, [like, like, like])
        return cekkursor.fetchall()
