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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `adminId` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(255) DEFAULT NULL,
  `useable` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`adminId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('17608015960','28a4f048b3b8a087db0752c9929809ab',0);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `goods` VALUES ('0e1d816e46ce11e8a296fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/a847da2f48ca4d44b9cd9963.png','足球',0,'123123',1,'2018-04-23 16:12:24',12.00,12.00,'http://p79ebonvg.bkt.clouddn.com/a847da2f48ca4d44b9cd9963.png/thumb'),('21bca76e4ae411e887bafcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/d4c5bcde5a444001b573cb4a.jpg','签字笔',0,'',1,'2018-04-28 21:00:31',12.00,32.00,'http://p79ebonvg.bkt.clouddn.com/d4c5bcde5a444001b573cb4a.jpg/thumb'),('32d1236e4ae411e8ab12fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/4f3bfcc291f749798f135341.jpg','衣服',0,'',2,'2018-04-28 21:01:00',43.00,123.00,'http://p79ebonvg.bkt.clouddn.com/4f3bfcc291f749798f135341.jpg/thumb'),('36680db84a1011e893ecfcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/bba251b0dd8d4450a59e446a.jpg','4G手机',0,'安装宽带送的',0,'2018-04-27 19:43:32',200.00,400.00,'http://p79ebonvg.bkt.clouddn.com/bba251b0dd8d4450a59e446a.jpg/thumb'),('37ba6622-46ca-11e8-8feb-fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/93013857d59c40489375598d.png','手机',0,'12313',0,'2018-04-23 15:44:56',600.00,3111.00,'http://p79ebonvg.bkt.clouddn.com/93013857d59c40489375598d.png/thumb'),('410bc5944ae411e8ae7efcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/637cfa17743a4599ae22627f.jpg','盆栽',0,'',4,'2018-04-28 21:01:23',1.00,5.00,'http://p79ebonvg.bkt.clouddn.com/637cfa17743a4599ae22627f.jpg/thumb'),('4b12f01c4a0711e8834afcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/8075904794e542cf8c0926e2.jpg','vivo X9',0,'用了一年，外观完好',4,'2018-04-27 18:39:41',500.00,1500.00,'http://p79ebonvg.bkt.clouddn.com/8075904794e542cf8c0926e2.jpg/thumb'),('4e1f7ddc4a1011e8aa3afcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/ca68c4d43359499292795b2c.jpg','T裇',0,'粉红色的',2,'2018-04-27 19:44:12',10.00,30.00,'http://p79ebonvg.bkt.clouddn.com/ca68c4d43359499292795b2c.jpg/thumb'),('684af8fe4a1011e8a7bffcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/533c42aae0ad4da3a446f6ba.jpg','2k电视',0,'夏普电视',0,'2018-04-27 19:44:56',1500.00,2500.00,'http://p79ebonvg.bkt.clouddn.com/533c42aae0ad4da3a446f6ba.jpg/thumb'),('68e1a3b04ad211e891fbfcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/b0e60a5ac094435c8a55319b.png','小说',0,'平凡的世界',1,'2018-04-28 18:53:39',14.00,28.00,'http://p79ebonvg.bkt.clouddn.com/b0e60a5ac094435c8a55319b.png/thumb'),('a29b7ade4ae411e8ae59fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/1221054cbe0c4a6baff21419.jpg','乒乓球拍',0,'',1,'2018-04-28 21:04:07',20.00,40.00,'http://p79ebonvg.bkt.clouddn.com/1221054cbe0c4a6baff21419.jpg/thumb'),('e84487e449ef11e8b147fcaa14e772b6','17608015960','熊大帅','http://p79ebonvg.bkt.clouddn.com/47eb5a2c74c9415992cee18b.jpg','自行车',0,'自己骑了一年，看起来挺新的',4,'2018-04-27 15:52:18',300.00,500.00,'http://p79ebonvg.bkt.clouddn.com/47eb5a2c74c9415992cee18b.jpg/thumb');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_order`
--

DROP TABLE IF EXISTS `goods_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_order` (
  `orderId` varchar(255) NOT NULL DEFAULT '',
  `goodsId` varchar(255) NOT NULL DEFAULT '',
  `ownerId` varchar(255) DEFAULT NULL,
  `ownerName` varchar(255) NOT NULL DEFAULT '',
  `customerId` varchar(255) NOT NULL DEFAULT '',
  `customerName` varchar(255) NOT NULL DEFAULT '',
  `goodsThums` varchar(255) DEFAULT '',
  `price` varchar(255) NOT NULL DEFAULT '',
  `orderStatus` int(1) NOT NULL DEFAULT '0',
  `ownerDisplay` int(1) NOT NULL DEFAULT '0',
  `customerDisplay` int(1) NOT NULL DEFAULT '0',
  `createNy` varchar(20) NOT NULL DEFAULT '2018.01',
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_order`
--

LOCK TABLES `goods_order` WRITE;
/*!40000 ALTER TABLE `goods_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `goods_order` ENABLE KEYS */;
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
  `createNy` varchar(20) NOT NULL DEFAULT '2018.01',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('13550277556','光头强','13550277556',NULL,0,'2018-04-23 13:50:19','13550277556','成都市双流区','2018.01'),('15928728280','熊二','15928728280',NULL,0,'2018-04-28 18:19:38','15928728280','七号楼702','2018.04'),('17608015960','熊大帅','17608015960','http:\\\\www',0,'2018-04-23 13:50:19','986192524@qq.com','十号楼705','2018.01'),('18328810637','小小','18328810637',NULL,0,'2018-04-23 13:50:19','17608015960','十号楼','2018.01');
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

-- Dump completed on 2018-05-04 14:58:01
