import mysql.connector

class crud:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="dbkesehatan"
        )
        self.cursor = self.koneksi.cursor()

    # INSERT ==========================
    def simpanPasien(self, nama, alamat, jekel, tgl, tempat, phone, jenis):
        try:
            sql = """INSERT INTO pasien
                (nama_pasien, alamat, jenis_kelamin, tgl_lahir, tmp_lahir, no_hp, jenis_pasien)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            val = (nama, alamat, jekel, tgl, tempat, phone, jenis)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data pasien berhasil disimpan!")
        except Exception as e:
            print("Gagal simpan pasien:", e)

    # SELECT ==========================
    def tampilPasien(self):
        try:
            sql = "SELECT * FROM pasien ORDER BY id_pasien ASC"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print("Gagal ambil data:", e)
            return []

    # UPDATE ==========================
    def ubahPasien(self, id_pasien, nama, alamat, jekel, tgl, tempat, phone, jenis):
        try:
            sql = """UPDATE pasien SET
                nama_pasien=%s, alamat=%s, jenis_kelamin=%s,
                tgl_lahir=%s, tmp_lahir=%s, no_hp=%s, jenis_pasien=%s
                WHERE id_pasien=%s"""
            val = (nama, alamat, jekel, tgl, tempat, phone, jenis, id_pasien)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data pasien berhasil diubah!")
        except Exception as e:
            print("Gagal ubah pasien:", e)

    # DELETE ==========================
    def hapusPasien(self, id_pasien):
        try:
            sql = "DELETE FROM pasien WHERE id_pasien=%s"
            self.cursor.execute(sql, (id_pasien,))
            self.koneksi.commit()
            print("Data pasien berhasil dihapus!")
        except Exception as e:
            print("Gagal hapus pasien:", e)
