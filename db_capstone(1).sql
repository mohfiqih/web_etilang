-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 22 Des 2022 pada 05.06
-- Versi server: 10.4.24-MariaDB
-- Versi PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_capstone`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `log_tilang`
--

CREATE TABLE `log_tilang` (
  `id` int(11) NOT NULL,
  `no_plat` varchar(50) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `filename_pelanggaran` varchar(200) NOT NULL,
  `pelanggaran` varchar(50) NOT NULL,
  `akurasi` varchar(100) NOT NULL,
  `tanggal` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `log_tilang`
--

INSERT INTO `log_tilang` (`id`, `no_plat`, `filename`, `filename_pelanggaran`, `pelanggaran`, `akurasi`, `tanggal`) VALUES
(24, '', 'image/Plate-2.png', 'testing2.png', '0 Tidak Pakai Helm', '99.98186230659485', '2022-12-21 11:10:32'),
(25, '', 'image/Plate-2.png', 'testing2.png', '0 Tidak Pakai Helm', '99.98186230659485', '2022-12-21 11:21:08'),
(27, '', 'image/Plate-2.png', 'testing2.png', '0 Tidak Pakai Helm', '99.98186230659485', '2022-12-21 13:38:25'),
(28, 'G 1234', 'image/Plate-1.png', 'testinghelm.png', '1 Pakai Helm', '99.84233379364014', '2022-12-21 13:38:44'),
(29, '', 'image/Plate-2.png', 'image_picker-315255100.png', '0 Tidak Pakai Helm', '99.98186230659485', '2022-12-21 14:08:11'),
(30, '37451:”', 'image/Plate-1.png', 'testing2.png', '0 Tidak Pakai Helm\n', '99.98186230659485', '2022-12-21 15:37:35'),
(31, 'raur:\n\n', 'image/Plate-11.png', 'testingmba.jpg', '1 Pakai Helm\n', '95.93461155891418', '2022-12-21 15:38:06'),
(32, '\'73?‘W“', 'image/Plate-2.png', 'cobatesting.jpeg', '1 Pakai Helm\n', '79.49985265731812', '2022-12-21 15:38:26'),
(33, '', 'image/Plate-4.png', 'image_picker-315255100.jpg', '1 Pakai Helm\n', '99.85699653625488', '2022-12-21 15:41:37'),
(34, '   \n\n1.7 7«/2 xl\n\n', 'image/Plate-2.png', 'image_picker1657431523.png', '1 Pakai Helm\n', '99.84233379364014', '2022-12-21 15:42:11'),
(35, '', 'image/Plate-17.png', 'testing2.png', '0 Tidak Pakai Helm\n', '99.98186230659485', '2022-12-21 15:49:26'),
(36, '', 'image/Plate-14.png', 'testinghelm.png', '1 Pakai Helm\n', '99.84233379364014', '2022-12-21 15:49:50'),
(37, '', 'image/Plate-69.png', 'cobatesting.jpeg', '1 Pakai Helm\n', '79.49985265731812', '2022-12-21 15:50:29'),
(38, '', 'image/Plate-81.png', '1.png', '1 Pakai Helm\n', '99.75804090499878', '2022-12-21 15:51:36'),
(39, ' \n\n', 'image/Plate-2.png', 'cobatesting.jpeg', '1 Pakai Helm\n', '79.49985265731812', '2022-12-21 15:54:43'),
(40, '', 'image/Plate-16.png', '2.png', '0 Tidak Pakai Helm\n', '82.07183480262756', '2022-12-21 15:55:10'),
(41, ' \n\n', 'image/Plate-4.png', 'image_picker-315255100.jpg', '1 Pakai Helm\n', '99.85699653625488', '2022-12-21 21:24:37'),
(42, ' \n\n', 'image/Plate-4.png', 'image_picker-315255100.jpg', '0 Tidak Pakai Helm\n', '73.19580316543579', '2022-12-21 22:19:33'),
(43, '', 'image/Plate-3.png', 'IMG-20221221-WA0025.jpg', '1 Pakai Helm\n', '82.80614018440247', '2022-12-21 22:20:31'),
(44, ' \n\nr\n\n', 'image/Plate-4.png', 'IMG-20221221-WA0019.jpg', '1 Pakai Helm\n', '99.94922876358032', '2022-12-21 22:20:53'),
(45, '', 'image/Plate-2.png', 'IMG-20221221-WA0022.jpg', '1 Pakai Helm\n', '99.9998927116394', '2022-12-21 22:21:13');

-- --------------------------------------------------------

--
-- Struktur dari tabel `log_users`
--

CREATE TABLE `log_users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `log_users`
--

INSERT INTO `log_users` (`id`, `username`, `password`, `email`) VALUES
(1, 'mohfiqih', '12345', 'mohfiqih@gmail.com'),
(12, 'admin', 'admin', 'admin@gmail.com'),
(16, 'capstone', 'capstone', 'capstone@gmail.com'),
(17, 'admin123', '12345', 'admin123@gmail.com'),
(18, 'erinsyah', '12345', 'erinsyah@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `log_tilang`
--
ALTER TABLE `log_tilang`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `log_users`
--
ALTER TABLE `log_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `log_tilang`
--
ALTER TABLE `log_tilang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT untuk tabel `log_users`
--
ALTER TABLE `log_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
