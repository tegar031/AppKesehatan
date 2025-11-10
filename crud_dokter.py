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

    # ===============================
    # CREATE
    # ===============================
    def simpanDokter(self, nama, jabatan):
        try:
            sql = "INSERT INTO dokter (nama_pemeriksa, jabatan) VALUES (%s, %s)"
            val = (nama, jabatan)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data berhasil disimpan!")
        except Exception as e:
            print("Gagal menyimpan data:", e)

    # ===============================
    # READ
    # ===============================
    def tampilDokter(self):
        try:
            sql = "SELECT * FROM dokter ORDER BY id_pemeriksa ASC"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print("Gagal mengambil data:", e)
            return []

    # ===============================
    # UPDATE
    # ===============================
    def ubahDokter(self, id_pemeriksa, nama, jabatan):
        try:
            sql = "UPDATE dokter SET nama_pemeriksa=%s, jabatan=%s WHERE id_pemeriksa=%s"
            val = (nama, jabatan, id_pemeriksa)
            self.cursor.execute(sql, val)
            self.koneksi.commit()
            print("Data berhasil diubah!")
        except Exception as e:
            print("Gagal mengubah data:", e)

    # ===============================
    # DELETE
    # ===============================
    def hapusDokter(self, id_pemeriksa):
        try:
            sql = "DELETE FROM dokter WHERE id_pemeriksa=%s"
            self.cursor.execute(sql, (id_pemeriksa,))
            self.koneksi.commit()
            print("Data berhasil dihapus!")
        except Exception as e:
            print("Gagal menghapus data:", e)

    # ===============================
    # CLOSE CONNECTION
    # ===============================
    def tutupKoneksi(self):
        self.cursor.close()
        self.koneksi.close()
