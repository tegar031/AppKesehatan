# crud_jadwal.py
import mysql.connector

class crud_jadwal:   # ← NAMANYA HARUS crud_jadwal !!!
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbkesehatan'
        )
        self.cursor = self.koneksi.cursor()

    def insertData(self, id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari):
        c = self.koneksi.cursor()
        sql = """
            INSERT INTO jadwal(id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari)
            VALUES (%s, %s, %s, %s, %s)
        """
        c.execute(sql, (id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari))
        self.koneksi.commit()
        c.close()

    def updateData(self, id_jadwal, id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari):
        c = self.koneksi.cursor()
        sql = """
            UPDATE jadwal SET
                id_poli=%s,
                id_pemeriksa=%s,
                jam_mulai=%s,
                jam_selesai=%s,
                hari=%s
            WHERE id_jadwal=%s
        """
        c.execute(sql, (id_poli, id_pemeriksa, jam_mulai, jam_selesai, hari, id_jadwal))
        self.koneksi.commit()
        c.close()

    def deleteData(self, id_jadwal):
        c = self.koneksi.cursor()
        sql = "DELETE FROM jadwal WHERE id_jadwal=%s"
        c.execute(sql, (id_jadwal,))
        self.koneksi.commit()
        c.close()

    def tampilData(self):
        c = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM jadwal ORDER BY id_jadwal ASC"
        c.execute(sql)
        return c.fetchall()

    def cariData(self, cari):
        c = self.koneksi.cursor(dictionary=True)
        sql = """
            SELECT * FROM jadwal
            WHERE id_jadwal LIKE %s
               OR id_poli LIKE %s
               OR id_pemeriksa LIKE %s
               OR hari LIKE %s
        """
        like = f"%{cari}%"
        c.execute(sql, (like, like, like, like))
        return c.fetchall()
