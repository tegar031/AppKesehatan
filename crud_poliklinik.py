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

    # ====================================
    # SIMPAN
    # ====================================
    def simpanPoli(self, nama, ket):
        cur = self.koneksi.cursor()
        sql = "INSERT INTO poliklinik(nama_poli, keterangan) VALUES (%s, %s)"
        cur.execute(sql, (nama, ket))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # UBAH
    # ====================================
    def ubahPoli(self, id_poli, nama, ket):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE poliklinik
            SET nama_poli=%s, keterangan=%s
            WHERE id_poli=%s
        """
        cur.execute(sql, (nama, ket, id_poli))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # HAPUS
    # ====================================
    def hapusPoli(self, id_poli):
        cur = self.koneksi.cursor()
        sql = "DELETE FROM poliklinik WHERE id_poli=%s"
        cur.execute(sql, (id_poli,))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # TAMPIL
    # ====================================
    def tampilDataPoli(self):
        cur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM poliklinik ORDER BY id_poli ASC"
        cur.execute(sql)
        return cur.fetchall()

    # ====================================
    # CARI
    # ====================================
    def cariDataPoli(self, cari):
        cur = self.koneksi.cursor(dictionary=True)
        like = f"%{cari}%"
        sql = """
            SELECT * FROM poliklinik
            WHERE id_poli LIKE %s OR nama_poli LIKE %s OR keterangan LIKE %s
        """
        cur.execute(sql, (like, like, like))
        return cur.fetchall()
