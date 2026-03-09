CREATE DATABASE individus_louches;
-- table individu

CREATE TABLE IF NOT EXISTS `individu` (
  `NumIndividu` int(11) NOT NULL DEFAULT '0',
  `Prenom` varchar(30) NOT NULL DEFAULT,
  `Prenom2` varchar(30) DEFAULT NULL,
  `Nom` varchar(30) NOT NULL DEFAULT,
  `DateNaissance` DATE,
  PRIMARY KEY (`NumIndividu`)

ALTER TABLE `individu`
  ADD CONSTRAINT `habitant_ibfk_1` FOREIGN KEY (`NumQualite`) REFERENCES `qualite` (`NumQualite`),
  ADD CONSTRAINT `habitant_ibfk_2` FOREIGN KEY (`NumVillage`) REFERENCES `village` (`NumVillage`);