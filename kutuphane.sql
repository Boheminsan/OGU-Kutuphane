-- phpMyAdmin SQL Dump
-- version 4.1.4
-- http://www.phpmyadmin.net
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 08 Oca 2017, 18:35:54
-- Sunucu sürümü: 5.6.15-log
-- PHP Sürümü: 5.4.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Veritabanı: `kutuphane`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `envanter`
--

CREATE TABLE IF NOT EXISTS `envanter` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `adi` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `yazar` varchar(100) COLLATE utf8_turkish_ci DEFAULT NULL,
  `yayinevi` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  `tur` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`adi`),
  UNIQUE KEY `id` (`id`),
  KEY `id_2` (`id`),
  KEY `yayinevi` (`yayinevi`),
  KEY `yazar` (`yazar`),
  KEY `tur` (`tur`),
  KEY `adi` (`adi`),
  KEY `id_3` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci COMMENT='Kütüphane içindekiler' AUTO_INCREMENT=1019 ;

--
-- Tablo döküm verisi `envanter`
--

INSERT INTO `envanter` (`id`, `adi`, `yazar`, `yayinevi`, `tur`) VALUES
(1001, 'Python', 'Mustafa Başer', 'Kodlab', 'Eğitim Başvuru'),
(1005, 'Her Yönüyle C# 6.0', 'Sefer Algan', 'Pusula', 'Eğitim Başvuru'),
(1006, 'WPF', 'Aykut Taşdelen', 'Pusula', 'Eğitim Başvuru'),
(1010, 'WPF2', 'afadffdafadfd', 'afadsf', 'Din-Mitoloji'),
(1015, 'WPhgfdcg', 'Aykut Taşdelen', 'c', 'Araştırma'),
(1017, 'efrgftyh', 'defrg', 'rthyuı', 'Çocuk-Genç');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `geciciid`
--

CREATE TABLE IF NOT EXISTS `geciciid` (
  `id` int(11) NOT NULL,
  `kitapid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `geciciid`
--

INSERT INTO `geciciid` (`id`, `kitapid`) VALUES
(1, 1018);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `odunc`
--

CREATE TABLE IF NOT EXISTS `odunc` (
  `kitap` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `onid` int(11) NOT NULL AUTO_INCREMENT,
  `ogr_no` bigint(12) NOT NULL,
  `ogr_adi` varchar(100) COLLATE utf8_turkish_ci NOT NULL,
  `a_tarih` date NOT NULL,
  `v_tarih` date NOT NULL,
  `teslim` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`onid`),
  UNIQUE KEY `onid_2` (`onid`),
  KEY `id` (`kitap`),
  KEY `id_2` (`kitap`),
  KEY `onid` (`onid`),
  KEY `onid_3` (`onid`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=4404046 ;

--
-- Tablo döküm verisi `odunc`
--

INSERT INTO `odunc` (`kitap`, `onid`, `ogr_no`, `ogr_adi`, `a_tarih`, `v_tarih`, `teslim`) VALUES
('Python', 10209, 121620111003, 'Batuhan Aktaş', '2016-12-14', '2017-01-05', 0),
('Python', 10210, 121620111003, 'Batuhan Aktaş', '2016-12-22', '2017-01-19', 0),
('WPF', 10211, 121620111003, 'Batuhan Aktaş', '2016-12-22', '2017-01-05', 0),
('WPhgfdcg', 4404043, 121620111003, 'Batuhan Aktaş', '2016-12-22', '2017-01-05', 1),
('WPF2', 4404044, 1312, 'jhgf', '2017-01-11', '2017-02-08', 1),
('WPF2', 4404045, 121620111003, 'Batuhan', '2017-01-12', '2017-02-09', 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tur`
--

CREATE TABLE IF NOT EXISTS `tur` (
  `turid` int(11) NOT NULL AUTO_INCREMENT,
  `turadi` varchar(30) CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`turadi`),
  UNIQUE KEY `tur_id` (`turid`),
  KEY `tur` (`turadi`),
  KEY `tur_2` (`turadi`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf32 COLLATE=utf32_turkish_ci AUTO_INCREMENT=10 ;

--
-- Tablo döküm verisi `tur`
--

INSERT INTO `tur` (`turid`, `turadi`) VALUES
(1, 'Eğitim Başvuru'),
(2, 'Edebiyat'),
(3, 'Araştırma'),
(4, 'Bilim'),
(5, 'Çocuk-Genç'),
(7, 'Yabancı'),
(8, 'Sanat'),
(6, 'Din-Mitoloji');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yayin`
--

CREATE TABLE IF NOT EXISTS `yayin` (
  `yayinid` int(11) NOT NULL AUTO_INCREMENT,
  `yayinadi` varchar(30) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`yayinadi`),
  UNIQUE KEY `ye_id` (`yayinid`),
  KEY `yayinevi` (`yayinadi`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=15 ;

--
-- Tablo döküm verisi `yayin`
--

INSERT INTO `yayin` (`yayinid`, `yayinadi`) VALUES
(1, 'Kodlab'),
(2, 'Seçkin'),
(3, 'Epsilon'),
(4, 'Arkadaş'),
(6, 'Pusula'),
(7, 'c'),
(8, 'Canevi'),
(9, 'afadsf'),
(10, 'aaasas'),
(11, 'fgfg'),
(12, 'fgew'),
(13, 'rthyuı'),
(14, 'Can');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yazar`
--

CREATE TABLE IF NOT EXISTS `yazar` (
  `yazarid` int(11) NOT NULL AUTO_INCREMENT,
  `yazaradi` varchar(200) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`yazaradi`),
  UNIQUE KEY `yaz_id` (`yazarid`),
  KEY `yazarAdi` (`yazaradi`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci AUTO_INCREMENT=16 ;

--
-- Tablo döküm verisi `yazar`
--

INSERT INTO `yazar` (`yazarid`, `yazaradi`) VALUES
(1, 'Mustafa Başer'),
(2, 'Aykut Taşdelen'),
(3, 'Volkan Aktaş'),
(5, 'Sefer Algan'),
(8, 'Tarık Sonkan'),
(10, 'afadffdafadfd'),
(11, 'aaaaaaa'),
(12, 'dddf'),
(13, 'lfr'),
(14, 'defrg'),
(15, 'gBAtuhan');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yetkili`
--

CREATE TABLE IF NOT EXISTS `yetkili` (
  `id` int(11) NOT NULL,
  `kAdi` varchar(10) COLLATE utf8_turkish_ci NOT NULL,
  `kSifre` varchar(16) COLLATE utf8_turkish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_2` (`id`),
  KEY `id` (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `yetkili`
--

INSERT INTO `yetkili` (`id`, `kAdi`, `kSifre`) VALUES
(1, 'grv01', '23456'),
(2, 'grv02', 'grv002'),
(3, 'grv03', '3456789');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
