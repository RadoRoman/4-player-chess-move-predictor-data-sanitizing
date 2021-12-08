CREATE DATABASE  IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8;
USE `mydb`;
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1sys_configvariableset_timesys_config_insert_set_user

SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT ;
SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS ;
SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION ;
SET NAMES utf8 ;
SET GLOBAL time_zone = '+02:00';
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 ;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 ;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' ;
SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 ;


--
-- Table structure for table `steps`
--

DROP TABLE IF EXISTS `steps`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8 ;
CREATE TABLE `steps` (
  `idsteps` int(11) NOT NULL AUTO_INCREMENT,
  `green` int(11) DEFAULT NULL,
  `yellow` int(11) DEFAULT NULL,
  `red` int(11) DEFAULT NULL,
  `blue` int(11) DEFAULT NULL,
  PRIMARY KEY (`idsteps`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `users` (
  `idusers` int(11) NOT NULL AUTO_INCREMENT,
  `player1` varchar(50) DEFAULT NULL,
  `player2` varchar(50) DEFAULT NULL,
  `player3` varchar(50) DEFAULT NULL,
  `player4` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idusers`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT;
SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS;
SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION;
SET SQL_NOTES=@OLD_SQL_NOTES;

