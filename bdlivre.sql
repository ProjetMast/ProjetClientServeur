-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 25 juil. 2019 à 01:56
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `bdlivre`
--

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

DROP TABLE IF EXISTS `livre`;
CREATE TABLE IF NOT EXISTS `livre` (
  `id` int(11) NOT NULL,
  `nom_livre` varchar(500) NOT NULL,
  `nom_auteur` varchar(200) NOT NULL,
  `nombre_page` int(11) NOT NULL,
  `annee_edition` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`id`, `nom_livre`, `nom_auteur`, `nombre_page`, `annee_edition`) VALUES
(1, 'Le grand livre d\'arduino', 'E. Bartmann', 625, 2014),
(2, 'Mooc introduction aux réseaux mobiles', 'A. PELOV', 700, 2014),
(3, 'initiation aux réseaux', 'Guy pujolle', 850, 2010),
(4, 'Réseaux et télécoms', 'Guy pujolle', 1300, 2015),
(5, 'Sécurité informatique', 'Nathan MWAMBA', 1700, 2019),
(6, 'réseaux GSM', 'Xavier LAGRANGE ', 300, 2000),
(7, 'Database engine', 'Henry MALI', 400, 2016),
(8, 'Internet des objets', 'Aser KAHILU', 690, 2001);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
