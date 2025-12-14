# This Python file uses the following encoding: utf-8
import mysql.connector

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm


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
    def simpanPoli(self, nama, keterangan):
        cekkursor = self.koneksi.cursor()
        sql = "INSERT INTO poliklinik(nama_poli, keterangan) VALUES (%s, %s)"
        cekkursor.execute(sql, (nama, keterangan))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # EDIT / UBAH DATA
    # =======================================================
    def ubahPoli(self, id_poli, nama, keterangan):
        cekkursor = self.koneksi.cursor()
        sql = """
            UPDATE poliklinik
            SET nama_poli=%s, keterangan=%s
            WHERE id_poli=%s
        """
        cekkursor.execute(sql, (nama, keterangan, id_poli))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # HAPUS DATA
    # =======================================================
    def hapusPoli(self, id_poli):
        cekkursor = self.koneksi.cursor()
        sql = "DELETE FROM poliklinik WHERE id_poli=%s"
        cekkursor.execute(sql, (id_poli,))
        self.koneksi.commit()
        cekkursor.close()

    # =======================================================
    # TAMPIL DATA
    # =======================================================
    def tampilDataPoli(self):
        cekkursor = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM poliklinik ORDER BY id_poli ASC"
        cekkursor.execute(sql)
        return cekkursor.fetchall()

    # =======================================================
    # CARI DATA
    # =======================================================
    def cariDataPoli(self, cari):
        cekkursor = self.koneksi.cursor(dictionary=True)
        sql = """
            SELECT * FROM poliklinik
            WHERE id_poli LIKE %s
            OR nama_poli LIKE %s
            OR keterangan LIKE %s
        """
        like = f"%{cari}%"
        cekkursor.execute(sql, [like, like, like])
        return cekkursor.fetchall()

    # =======================================================
    # LAPORAN PDF
    # =======================================================
    def laporanSemuaPoli(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT id_poli, nama_poli, keterangan FROM poliklinik")
        data = cursor.fetchall()
        cursor.close()

        isidata = [["ID Poli", "Nama Poli", "Keterangan"]]
        for row in data:
            isidata.append([
                str(row[0]),
                str(row[1]),
                str(row[2])
            ])

        pdf = "laporan_poliklinik_semua.pdf"
        file = SimpleDocTemplate(pdf, pagesize=A4)

        table = Table(isidata, colWidths=[4*cm, 8*cm, 8*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        file.build([table])
        return pdf
