-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Des 2025 pada 15.26
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbkesehatan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dokter`
--

CREATE TABLE `dokter` (
  `id_pemeriksa` int(15) NOT NULL,
  `nama_pemeriksa` varchar(255) NOT NULL,
  `jabatan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `dokter`
--

INSERT INTO `dokter` (`id_pemeriksa`, `nama_pemeriksa`, `jabatan`) VALUES
(15, 'Azril', 'Dokter Umum'),
(16, 'Adit', 'Kepala Puskesmas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwal`
--

CREATE TABLE `jadwal` (
  `id_jadwal` int(11) NOT NULL,
  `id_poli` int(11) NOT NULL,
  `id_pemeriksa` int(11) NOT NULL,
  `jam_mulai` time NOT NULL,
  `jam_selesai` time NOT NULL,
  `hari` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `jadwal`
--

INSERT INTO `jadwal` (`id_jadwal`, `id_poli`, `id_pemeriksa`, `jam_mulai`, `jam_selesai`, `hari`) VALUES
(4, 7, 16, '11:00:00', '14:00:00', 'Kamis'),
(5, 8, 15, '10:00:00', '14:00:00', 'Jum\'at');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pasien`
--

CREATE TABLE `pasien` (
  `id_pasien` int(111) NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `jenis_kelamin` char(11) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `tmp_lahir` varchar(255) NOT NULL,
  `no_hp` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `jenis_pasien` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pasien`
--

INSERT INTO `pasien` (`id_pasien`, `nama_pasien`, `alamat`, `jenis_kelamin`, `tgl_lahir`, `tmp_lahir`, `no_hp`, `jenis_pasien`) VALUES
(1, 'Zikry', 'Handil Bakti', 'Laki - Laki', '2004-07-10', 'Kapuas', '081352772890', 'BPJS'),
(4, 'Tegar', 'hksn', 'Laki - Laki', '2000-01-01', 'barabai', '081352778321', 'BPJS'),
(5, 'Kitha', 'Sultan Adam', 'Laki - Laki', '2004-07-10', 'Kota Baru', '081352882492', 'BPJS');

-- --------------------------------------------------------

--
-- Struktur dari tabel `poliklinik`
--

CREATE TABLE `poliklinik` (
  `id_poli` int(11) NOT NULL,
  `nama_poli` varchar(255) NOT NULL,
  `keterangan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `poliklinik`
--

INSERT INTO `poliklinik` (`id_poli`, `nama_poli`, `keterangan`) VALUES
(3, 'Pelayanan konsultasi dan administrasi', 'konsultasi'),
(4, 'Poli Umum', 'Pemeriksaan kesehatan umum'),
(5, 'Poli Gigi', 'Layanan kesehatan gigi dan mulut'),
(6, 'Poli Anak', 'Pelayanan kesehatan anak'),
(7, 'Poli Kulit', 'Pemeriksaan dan perawatan kulit'),
(8, 'Pelayanan konsultasi dan administrasi', 'Pemeriksaan kesehatan umum');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`id_pemeriksa`);

--
-- Indeks untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`id_jadwal`),
  ADD KEY `id_poli` (`id_poli`,`id_pemeriksa`),
  ADD KEY `fk_jadwal_pemeriksa` (`id_pemeriksa`);

--
-- Indeks untuk tabel `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`id_pasien`);

--
-- Indeks untuk tabel `poliklinik`
--
ALTER TABLE `poliklinik`
  ADD PRIMARY KEY (`id_poli`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `dokter`
--
ALTER TABLE `dokter`
  MODIFY `id_pemeriksa` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `id_jadwal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `pasien`
--
ALTER TABLE `pasien`
  MODIFY `id_pasien` int(111) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `poliklinik`
--
ALTER TABLE `poliklinik`
  MODIFY `id_poli` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  ADD CONSTRAINT `fk_jadwal_pemeriksa` FOREIGN KEY (`id_pemeriksa`) REFERENCES `dokter` (`id_pemeriksa`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_jadwal_poli` FOREIGN KEY (`id_poli`) REFERENCES `poliklinik` (`id_poli`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
