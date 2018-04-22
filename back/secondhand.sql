-- MySQL dump 10.13  Distrib 5.5.53, for Win32 (AMD64)
--
-- Host: localhost    Database: secondhand
-- ------------------------------------------------------
-- Server version	5.5.53

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `goodsId` varchar(30) NOT NULL DEFAULT '',
  `ownerId` varchar(30) NOT NULL DEFAULT '',
  `ownerName` varchar(255) NOT NULL DEFAULT '',
  `goodsImg` varchar(255) DEFAULT NULL,
  `goodsName` varchar(255) NOT NULL DEFAULT '',
  `isSale` int(1) NOT NULL DEFAULT '0',
  `goodsDesc` varchar(255) DEFAULT NULL,
  `attrCatId` int(1) NOT NULL DEFAULT '0',
  `createTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `currentPrice` float(8,2) NOT NULL DEFAULT '0.00',
  `originalPrice` float(8,2) NOT NULL DEFAULT '0.00',
  `goodsThums` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`goodsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES ('123','123','123','https://img.alicdn.com/bao/uploaded/i3/6000000006716/TB2cnQqomhlpuFjSspkXXa1ApXa_!!0-fleamarket.jpg_160x160.jpg','123',0,NULL,0,'0000-00-00 00:00:00',0.00,0.00,'123'),('321','321','321','https://img.alicdn.com/bao/uploaded/i1/2354695424/TB28ckgayqAXuNjy1XdXXaYcVXa_!!2354695424.jpg_200x200.jpg','321',0,NULL,0,'0000-00-00 00:00:00',0.00,0.00,'321');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userId` varchar(30) NOT NULL DEFAULT '',
  `loginName` varchar(50) DEFAULT NULL,
  `loginPwd` varchar(50) NOT NULL DEFAULT '',
  `userPhone` varchar(11) NOT NULL DEFAULT '',
  `userPhoto` varchar(255) DEFAULT NULL,
  `userStatus` int(1) NOT NULL DEFAULT '0',
  `createTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('17608015960','熊大帅','6ac1e56bc78f031059be7be854522c4c','17608015960','http:\\\\www',1,'0000-00-00 00:00:00'),('18328810637',NULL,'6ac1e56bc78f031059be7be854522c4c','18328810637',NULL,0,'0000-00-00 00:00:00');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-19 20:16:28
