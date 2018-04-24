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
  `goodsId` varchar(255) NOT NULL DEFAULT '',
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
  `goodsThums` varchar(255) DEFAULT '',
  PRIMARY KEY (`goodsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES ('0e1d816e46ce11e8a296fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/a847da2f48ca4d44b9cd9963.png','足球',0,'123123',1,'2018-04-23 16:12:24',12.00,12.00,'http://p79ebonvg.bkt.clouddn.com/a847da2f48ca4d44b9cd9963.png/thumb'),('37ba6622-46ca-11e8-8feb-fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/93013857d59c40489375598d.png','手机',0,'12313',0,'2018-04-23 15:44:56',600.00,3111.00,'http://p79ebonvg.bkt.clouddn.com/93013857d59c40489375598d.png/thumb');
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
  `userPhone` varchar(11) NOT NULL DEFAULT '',
  `userPhoto` varchar(255) DEFAULT NULL,
  `userStatus` int(1) NOT NULL DEFAULT '0',
  `createTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `alipay` varchar(255) NOT NULL DEFAULT '',
  `stress` varchar(255) NOT NULL DEFAULT '十号楼',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('13550277556','夏天阿塞阀啊安','13550277556',NULL,1,'2018-04-23 13:50:19','13550277556','成都市双流区'),('17608015960','熊大帅','17608015960','http:\\\\www',1,'0000-00-00 00:00:00','','十号楼'),('18328810637',NULL,'18328810637',NULL,0,'0000-00-00 00:00:00','','十号楼');
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

-- Dump completed on 2018-04-24 18:25:16
