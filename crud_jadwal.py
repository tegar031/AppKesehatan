# crud_jadwal.py
import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm

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

    def laporanSemuaJadwal(self):
        cursor = self.koneksi.cursor()
        cursor.execute("""
            SELECT id_jadwal, id_poli, id_pemeriksa,
                   jam_mulai, jam_selesai, hari
            FROM jadwal
        """)
        data = cursor.fetchall()
        cursor.close()

        isidata = [[
            "id_jadwal",
            "id_poli",
            "id_pemeriksa",
            "jam_mulai",
            "jam_selesai",
            "hari"
        ]]

        for row in data:
            isidata.append([
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5])
            ])

        pdf = "laporan_jadwal_semua.pdf"
        file = SimpleDocTemplate(pdf, pagesize=A4)

        table = Table(
            isidata,
            colWidths=[3*cm, 3*cm, 4*cm, 3*cm, 3*cm, 3*cm]
        )

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        file.build([table])
        return pdf
