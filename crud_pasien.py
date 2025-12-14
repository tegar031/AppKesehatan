import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4, landscape
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

    # ====================================
    # SIMPAN
    # ====================================
    def simpanPasien(self, nama, alamat, jk, tgl, tmp, hp, jenis):
        cur = self.koneksi.cursor()
        sql = """
            INSERT INTO pasien(nama_pasien, alamat, jenis_kelamin, tgl_lahir, tmp_lahir, no_hp, jenis_pasien)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (nama, alamat, jk, tgl, tmp, hp, jenis))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # UBAH
    # ====================================
    def ubahPasien(self, idp, nama, alamat, jk, tgl, tmp, hp, jenis):
        cur = self.koneksi.cursor()
        sql = """
            UPDATE pasien
            SET nama_pasien=%s, alamat=%s, jenis_kelamin=%s, tgl_lahir=%s,
                tmp_lahir=%s, no_hp=%s, jenis_pasien=%s
            WHERE id_pasien=%s
        """
        cur.execute(sql, (nama, alamat, jk, tgl, tmp, hp, jenis, idp))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # HAPUS
    # ====================================
    def hapusPasien(self, idp):
        cur = self.koneksi.cursor()
        sql = "DELETE FROM pasien WHERE id_pasien=%s"
        cur.execute(sql, (idp,))
        self.koneksi.commit()
        cur.close()

    # ====================================
    # TAMPIL
    # ====================================
    def tampilDataPasien(self):
        cur = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM pasien ORDER BY id_pasien ASC"
        cur.execute(sql)
        return cur.fetchall()

    # ====================================
    # CARI
    # ====================================
    def cariDataPasien(self, cari):
        cur = self.koneksi.cursor(dictionary=True)
        like = f"%{cari}%"
        sql = """
            SELECT * FROM pasien
            WHERE id_pasien LIKE %s
            OR nama_pasien LIKE %s
            OR alamat LIKE %s
            OR jenis_kelamin LIKE %s
            OR jenis_pasien LIKE %s
        """
        cur.execute(sql, (like, like, like, like, like))
        return cur.fetchall()

    # ====================================
    # Cetak
    # ====================================

    def laporanSemuaPasien(self):
        cursor = self.koneksi.cursor()
        cursor.execute("""
            SELECT id_pasien, nama_pasien, alamat, jenis_kelamin,
                   tgl_lahir, tmp_lahir, no_hp, jenis_pasien
            FROM pasien
        """)
        data = cursor.fetchall()
        cursor.close()

        isidata = [[
            "id_pasien",
            "nama_pasien",
            "alamat",
            "jenis_kelamin",
            "tgl_lahir",
            "tmp_lahir",
            "no_hp",
            "jenis_pasien"
        ]]

        for row in data:
            isidata.append([
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5]),
                str(row[6]),
                str(row[7])
            ])

            pdf = "laporan_pasien_semua.pdf"

            file = SimpleDocTemplate(
                pdf,
                pagesize=landscape(A4),
                rightMargin=1*cm,
                leftMargin=1*cm,
                topMargin=1*cm,
                bottomMargin=1*cm
            )

            table = Table(
                isidata,
                colWidths=[
                    2*cm, 4*cm, 5*cm, 3*cm,
                    3*cm, 4*cm, 4*cm, 3*cm
                ]
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

