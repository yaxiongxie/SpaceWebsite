-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: SpaceWebsite
-- ------------------------------------------------------
-- Server version	5.7.18

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add office building',7,'add_officebuilding'),(20,'Can change office building',7,'change_officebuilding'),(21,'Can delete office building',7,'delete_officebuilding'),(22,'Can add country',8,'add_country'),(23,'Can change country',8,'change_country'),(24,'Can delete country',8,'delete_country'),(25,'Can add cms status',9,'add_cmsstatus'),(26,'Can change cms status',9,'change_cmsstatus'),(27,'Can delete cms status',9,'delete_cmsstatus'),(28,'Can add rent',10,'add_rent'),(29,'Can change rent',10,'change_rent'),(30,'Can delete rent',10,'delete_rent'),(31,'Can add subway',11,'add_subway'),(32,'Can change subway',11,'change_subway'),(33,'Can delete subway',11,'delete_subway'),(34,'Can add room type',12,'add_roomtype'),(35,'Can change room type',12,'change_roomtype'),(36,'Can delete room type',12,'delete_roomtype'),(37,'Can add room direction',13,'add_roomdirection'),(38,'Can change room direction',13,'change_roomdirection'),(39,'Can delete room direction',13,'delete_roomdirection'),(40,'Can add user',14,'add_user'),(41,'Can change user',14,'change_user'),(42,'Can delete user',14,'delete_user'),(43,'Can add 所有订单',15,'add_order'),(44,'Can change 所有订单',15,'change_order'),(45,'Can delete 所有订单',15,'delete_order'),(46,'Can add 服务需求',16,'add_servicerequirement'),(47,'Can change 服务需求',16,'change_servicerequirement'),(48,'Can delete 服务需求',16,'delete_servicerequirement'),(49,'Can add 消息中心',17,'add_messages'),(50,'Can change 消息中心',17,'change_messages'),(51,'Can delete 消息中心',17,'delete_messages'),(52,'Can add 注册企业',18,'add_corporation'),(53,'Can change 注册企业',18,'change_corporation'),(54,'Can delete 注册企业',18,'delete_corporation'),(55,'Can add 用户房源',19,'add_housesource'),(56,'Can change 用户房源',19,'change_housesource'),(57,'Can delete 用户房源',19,'delete_housesource'),(58,'Can add 用户',20,'add_account'),(59,'Can change 用户',20,'change_account'),(60,'Can delete 用户',20,'delete_account'),(61,'Can add 用户需求',21,'add_houserequirement'),(62,'Can change 用户需求',21,'change_houserequirement'),(63,'Can delete 用户需求',21,'delete_houserequirement'),(64,'Can add 写字楼',22,'add_officebuildinglist'),(65,'Can change 写字楼',22,'change_officebuildinglist'),(66,'Can delete 写字楼',22,'delete_officebuildinglist'),(67,'Can add 新闻',23,'add_news'),(68,'Can change 新闻',23,'change_news'),(69,'Can delete 新闻',23,'delete_news'),(70,'Can add 写字楼',24,'add_officelist'),(71,'Can change 写字楼',24,'change_officelist'),(72,'Can delete 写字楼',24,'delete_officelist'),(73,'Can add 房源用途',25,'add_usetype'),(74,'Can change 房源用途',25,'change_usetype'),(75,'Can delete 房源用途',25,'delete_usetype'),(76,'Can add 性别',26,'add_sex'),(77,'Can change 性别',26,'change_sex'),(78,'Can delete 性别',26,'delete_sex'),(79,'Can add 街道',27,'add_district'),(80,'Can change 街道',27,'change_district'),(81,'Can delete 街道',27,'delete_district'),(82,'Can add 地铁',28,'add_subway'),(83,'Can change 地铁',28,'change_subway'),(84,'Can delete 地铁',28,'delete_subway'),(85,'Can add 新闻类别',29,'add_newtype'),(86,'Can change 新闻类别',29,'change_newtype'),(87,'Can delete 新闻类别',29,'delete_newtype'),(88,'Can add 房源类型',30,'add_sourcetype'),(89,'Can change 房源类型',30,'change_sourcetype'),(90,'Can delete 房源类型',30,'delete_sourcetype'),(91,'Can add 状态',31,'add_status'),(92,'Can change 状态',31,'change_status'),(93,'Can delete 状态',31,'delete_status'),(94,'Can add 装修程序',32,'add_decoratedegree'),(95,'Can change 装修程序',32,'change_decoratedegree'),(96,'Can delete 装修程序',32,'delete_decoratedegree'),(97,'Can add 区',33,'add_area'),(98,'Can change 区',33,'change_area'),(99,'Can delete 区',33,'delete_area');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$MGT3qo3kELPx$MXxE4weqdcvNZGjPUdHHSPDA8D8wtp+AIhdf4zozhBo=','2017-05-31 09:32:31.509529',1,'admin','','','xieyaxiong@163.com',1,1,'2017-05-09 09:54:11.515512'),(2,'pbkdf2_sha256$36000$FYrVb254x6Qp$MtYCaEdVi0aRL4dNVoq6UhTt7AYSzZflvE2snIJU4Bc=','2017-05-11 05:51:41.982939',0,'test','xie','yaxiong','xieyaxiong@163.com',1,1,'2017-05-11 05:46:33.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,31);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_area`
--

DROP TABLE IF EXISTS `commonData_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_area`
--

LOCK TABLES `commonData_area` WRITE;
/*!40000 ALTER TABLE `commonData_area` DISABLE KEYS */;
INSERT INTO `commonData_area` VALUES (4,'江岸',1),(5,'江汉',2),(6,'硚口',3),(7,'东西湖',4),(8,'武昌',5),(9,'青山',6),(10,'洪山',7),(11,'汉阳',8),(12,'东湖高新',9),(13,'江厦',10);
/*!40000 ALTER TABLE `commonData_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_decoratedegree`
--

DROP TABLE IF EXISTS `commonData_decoratedegree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_decoratedegree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `decorate_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_decoratedegree`
--

LOCK TABLES `commonData_decoratedegree` WRITE;
/*!40000 ALTER TABLE `commonData_decoratedegree` DISABLE KEYS */;
INSERT INTO `commonData_decoratedegree` VALUES (1,'精装修',1),(2,'简装修',2),(3,'土坯',3);
/*!40000 ALTER TABLE `commonData_decoratedegree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_district`
--

DROP TABLE IF EXISTS `commonData_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(200) NOT NULL,
  `district_firstChar` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  `area_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `commonData_district_area_type_id_a984c312_fk_commonData_area_id` (`area_type_id`),
  CONSTRAINT `commonData_district_area_type_id_a984c312_fk_commonData_area_id` FOREIGN KEY (`area_type_id`) REFERENCES `commonData_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_district`
--

LOCK TABLES `commonData_district` WRITE;
/*!40000 ALTER TABLE `commonData_district` DISABLE KEYS */;
INSERT INTO `commonData_district` VALUES (1,'百步亭','B',1,4),(2,'大智路','D',2,4),(3,'堤角','D',3,4),(4,'二七','E',4,4),(5,'黄埔永清','H',5,4),(6,'后湖','H',6,4),(7,'前进江汉','Q',7,4),(8,'三阳路','S',8,4),(9,'塔子湖','T',9,4),(10,'台北香港路','T',10,4),(11,'竹叶山花桥','Z',11,4),(12,'宝丰崇仁','B',1,5),(13,'常青路','C',2,5),(14,'长丰常码头','C',3,5),(15,'CBD西北湖','C',4,5),(16,'长港路','C',5,5),(17,'前进江汉','Q',6,5),(18,'塔子湖','T',8,5),(19,'台北香港路','T',9,5),(20,'唐家墩','T',11,5),(21,'武广万松园','W',12,5),(22,'杨汊湖','Y',13,5),(23,'宝丰崇仁','B',1,6),(24,'长丰常码头','C',2,6),(25,'CBD西北湖','C',3,6),(26,'古田','G',4,6),(27,'汉正街','H',5,6),(28,'集贤','J',6,6),(29,'吴家山','W',7,6),(30,'宗关','Z',10,6),(31,'常青花园','C',1,7),(32,'东西湖其它','D',2,7),(33,'金银湖','J',3,7),(34,'将军路','J',4,7),(35,'吴家山','W',5,7),(36,'白沙洲','B',1,8),(37,'楚河汉街','C',2,8),(38,'东湖东亭','D',3,8),(39,'街道口','J',4,7),(40,'积玉桥','J',5,8),(41,'水果湖','S',6,8),(42,'首义','S',7,8),(43,'沙湖','S',1,8),(44,'团结大道','T',2,8),(45,'武昌火车站','W',2,8),(46,'徐东','X',2,8),(47,'杨园','Y',2,7),(48,'中北路','Z',3,8),(49,'中南丁字桥','Z',3,8),(50,'洪山其它','H',1,9),(51,'青山','Q',2,9),(52,'白沙洲','B',1,10),(53,'楚河汉街','C',2,10),(54,'东湖东亭','D',2,10),(55,'洪山其它','H',2,10),(56,'虎泉杨家弯','H',2,10),(57,'街道口','J',3,10),(58,'珞狮南路','L',2,10),(59,'老南湖','L',2,10),(60,'南湖沃尔玛','N',3,10),(61,'青山','Q',3,10),(62,'沙湖','S',4,10),(63,'团结大道','T',4,10),(64,'武昌火车站','W',4,10),(65,'徐东','X',5,10),(66,'新南湖','X',7,10),(67,'中南丁字桥','Z',2,10),(68,'卓刀泉','Z',5,10),(69,'七里庙','Q',1,11),(70,'四新','S',2,11),(71,'王家湾','W',3,11),(72,'钟家村','Z',4,11),(73,'关西长职','G',1,12),(74,'光谷广场','G',2,12),(75,'关山大道','G',3,12),(76,'光谷南','G',4,12),(77,'光谷东','G',5,12),(78,'洪山其它','H',2,12),(79,'华科大','H',3,12),(80,'江厦其它','J',4,12),(81,'金融港','J',5,12),(82,'民族大道','M',3,12),(83,'三环南','S',4,12),(84,'汤逊湖藏龙岛','T',5,12),(85,'江厦其它','J',1,13);
/*!40000 ALTER TABLE `commonData_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_newtype`
--

DROP TABLE IF EXISTS `commonData_newtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_newtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_newtype`
--

LOCK TABLES `commonData_newtype` WRITE;
/*!40000 ALTER TABLE `commonData_newtype` DISABLE KEYS */;
INSERT INTO `commonData_newtype` VALUES (1,'行业新闻',1),(2,'活动动态',2),(3,'最新要闻',3);
/*!40000 ALTER TABLE `commonData_newtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_sex`
--

DROP TABLE IF EXISTS `commonData_sex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_sex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sex_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_sex`
--

LOCK TABLES `commonData_sex` WRITE;
/*!40000 ALTER TABLE `commonData_sex` DISABLE KEYS */;
INSERT INTO `commonData_sex` VALUES (1,'男',1),(2,'女',2);
/*!40000 ALTER TABLE `commonData_sex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_sourcetype`
--

DROP TABLE IF EXISTS `commonData_sourcetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_sourcetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source_type_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_sourcetype`
--

LOCK TABLES `commonData_sourcetype` WRITE;
/*!40000 ALTER TABLE `commonData_sourcetype` DISABLE KEYS */;
INSERT INTO `commonData_sourcetype` VALUES (1,'写字楼',1),(2,'商铺',2),(3,'住宅',3);
/*!40000 ALTER TABLE `commonData_sourcetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_status`
--

DROP TABLE IF EXISTS `commonData_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_status`
--

LOCK TABLES `commonData_status` WRITE;
/*!40000 ALTER TABLE `commonData_status` DISABLE KEYS */;
INSERT INTO `commonData_status` VALUES (1,'有效',1),(2,'无效',2);
/*!40000 ALTER TABLE `commonData_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_subway`
--

DROP TABLE IF EXISTS `commonData_subway`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_subway` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subway_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_subway`
--

LOCK TABLES `commonData_subway` WRITE;
/*!40000 ALTER TABLE `commonData_subway` DISABLE KEYS */;
INSERT INTO `commonData_subway` VALUES (1,'1号线',1),(2,'2号线',2),(3,'3号线',3),(4,'4号线',4),(5,'6号线',6);
/*!40000 ALTER TABLE `commonData_subway` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commonData_usetype`
--

DROP TABLE IF EXISTS `commonData_usetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commonData_usetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `use_name` varchar(200) NOT NULL,
  `sort_int` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonData_usetype`
--

LOCK TABLES `commonData_usetype` WRITE;
/*!40000 ALTER TABLE `commonData_usetype` DISABLE KEYS */;
INSERT INTO `commonData_usetype` VALUES (1,'居住',1),(2,'办公',2),(3,'其它',3);
/*!40000 ALTER TABLE `commonData_usetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=143 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-05-11 05:46:33.710488','2','test',1,'[{\"added\": {}}]',4,1),(2,'2017-05-11 05:47:35.514719','2','test',2,'[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\", \"last_login\"]}}]',4,1),(3,'2017-05-11 05:49:01.900737','2','test',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(4,'2017-05-11 05:50:32.596594','2','test',2,'[]',4,1),(5,'2017-05-11 05:51:06.866323','2','test',2,'[{\"changed\": {\"fields\": [\"is_staff\"]}}]',4,1),(6,'2017-05-11 05:51:48.768672','1','qwe',1,'[{\"added\": {}}]',11,2),(7,'2017-05-11 05:51:58.372122','2','212',1,'[{\"added\": {}}]',11,2),(8,'2017-05-17 07:28:08.954469','1','123',1,'[{\"added\": {}}]',8,1),(9,'2017-05-17 07:28:13.639667','3','1',1,'[{\"added\": {}}]',11,1),(10,'2017-05-17 07:28:30.064594','1','1',1,'[{\"added\": {}}]',9,1),(11,'2017-05-17 07:28:55.523252','1','d',1,'[{\"added\": {}}]',7,1),(12,'2017-05-17 07:37:13.812420','1','d',3,'',7,1),(13,'2017-05-17 07:37:54.740426','3','1',3,'',11,1),(14,'2017-05-17 07:37:54.742415','2','212',3,'',11,1),(15,'2017-05-17 07:37:54.744049','1','qwe',3,'',11,1),(16,'2017-05-17 07:38:03.448032','1','123',3,'',8,1),(17,'2017-05-17 08:17:59.193631','2','1',1,'[{\"added\": {}}]',8,1),(18,'2017-05-17 08:18:05.547980','4','2',1,'[{\"added\": {}}]',11,1),(19,'2017-05-17 08:18:35.684404','2','123',1,'[{\"added\": {}}]',7,1),(20,'2017-05-27 09:29:28.688290','1','西湖区',1,'[{\"added\": {}}]',33,1),(21,'2017-05-27 09:29:34.872006','2','江干区',1,'[{\"added\": {}}]',33,1),(22,'2017-05-27 09:29:46.592878','3','余杭区',1,'[{\"added\": {}}]',33,1),(23,'2017-05-27 09:33:39.824461','1','男',1,'[{\"added\": {}}]',26,1),(24,'2017-05-27 09:33:44.534070','2','女',1,'[{\"added\": {}}]',26,1),(25,'2017-05-27 09:34:34.725812','1','1号线',1,'[{\"added\": {}}]',28,1),(26,'2017-05-27 09:34:39.506009','2','2号线',1,'[{\"added\": {}}]',28,1),(27,'2017-05-27 09:34:44.561024','3','3号线',1,'[{\"added\": {}}]',28,1),(28,'2017-05-27 09:34:50.030273','4','4号线',1,'[{\"added\": {}}]',28,1),(29,'2017-05-27 09:34:54.857013','5','6号线',1,'[{\"added\": {}}]',28,1),(30,'2017-05-27 09:35:18.558204','1','居住',1,'[{\"added\": {}}]',25,1),(31,'2017-05-27 09:35:23.527525','2','办公',1,'[{\"added\": {}}]',25,1),(32,'2017-05-27 09:57:39.477276','1','行业新闻',1,'[{\"added\": {}}]',29,1),(33,'2017-05-27 09:57:49.379277','2','活动动态',1,'[{\"added\": {}}]',29,1),(34,'2017-05-27 09:58:12.288240','3','最新要闻',1,'[{\"added\": {}}]',29,1),(35,'2017-05-27 10:18:27.586883','3','其它',1,'[{\"added\": {}}]',25,1),(36,'2017-05-31 05:14:51.034643','3','余杭区',2,'[{\"changed\": {\"fields\": [\"sort_int\"]}}]',33,1),(37,'2017-06-01 06:46:03.630989','1','有效',1,'[{\"added\": {}}]',31,1),(38,'2017-06-01 06:46:08.966586','2','无效',1,'[{\"added\": {}}]',31,1),(39,'2017-06-01 06:46:27.851764','1','精装修',1,'[{\"added\": {}}]',32,1),(40,'2017-06-01 06:46:38.203762','2','简装修',1,'[{\"added\": {}}]',32,1),(41,'2017-06-01 06:46:45.953800','3','土坯',1,'[{\"added\": {}}]',32,1),(42,'2017-06-01 06:47:50.813720','1','写字楼',1,'[{\"added\": {}}]',30,1),(43,'2017-06-01 06:47:57.794028','2','商铺',1,'[{\"added\": {}}]',30,1),(44,'2017-06-01 06:48:05.843349','3','住宅',1,'[{\"added\": {}}]',30,1),(45,'2017-06-01 06:48:25.694926','3','余杭区',3,'',33,1),(46,'2017-06-01 06:48:25.698417','2','江干区',3,'',33,1),(47,'2017-06-01 06:48:25.700700','1','西湖区',3,'',33,1),(48,'2017-06-01 06:51:20.022266','4','江岸',1,'[{\"added\": {}}]',33,1),(49,'2017-06-01 06:51:30.456166','5','江汉',1,'[{\"added\": {}}]',33,1),(50,'2017-06-01 06:51:46.696779','6','硚口',1,'[{\"added\": {}}]',33,1),(51,'2017-06-01 06:52:01.670074','7','东西湖',1,'[{\"added\": {}}]',33,1),(52,'2017-06-01 06:52:07.875544','8','武昌',1,'[{\"added\": {}}]',33,1),(53,'2017-06-01 06:52:14.832273','9','青山',1,'[{\"added\": {}}]',33,1),(54,'2017-06-01 06:52:23.069228','10','洪山',1,'[{\"added\": {}}]',33,1),(55,'2017-06-01 06:52:30.635972','11','汉阳',1,'[{\"added\": {}}]',33,1),(56,'2017-06-01 06:52:39.551377','12','东湖高新',1,'[{\"added\": {}}]',33,1),(57,'2017-06-01 06:52:46.028019','13','江厦',1,'[{\"added\": {}}]',33,1),(58,'2017-06-01 06:58:29.952619','1','百步亭',1,'[{\"added\": {}}]',27,1),(59,'2017-06-01 06:58:41.108269','2','大智路',1,'[{\"added\": {}}]',27,1),(60,'2017-06-01 06:58:55.148822','3','堤角',1,'[{\"added\": {}}]',27,1),(61,'2017-06-01 06:59:14.619725','4','二七',1,'[{\"added\": {}}]',27,1),(62,'2017-06-01 06:59:33.499883','5','黄埔永清',1,'[{\"added\": {}}]',27,1),(63,'2017-06-01 06:59:50.573030','6','后湖',1,'[{\"added\": {}}]',27,1),(64,'2017-06-01 07:00:03.839681','7','前进江汉',1,'[{\"added\": {}}]',27,1),(65,'2017-06-01 07:00:48.095185','8','三阳路',1,'[{\"added\": {}}]',27,1),(66,'2017-06-01 07:01:01.785625','9','塔子湖',1,'[{\"added\": {}}]',27,1),(67,'2017-06-01 07:01:19.679617','10','台北香港路',1,'[{\"added\": {}}]',27,1),(68,'2017-06-01 07:02:12.866168','11','竹叶山花桥',1,'[{\"added\": {}}]',27,1),(69,'2017-06-01 07:03:33.032296','12','宝丰崇仁',1,'[{\"added\": {}}]',27,1),(70,'2017-06-01 07:03:49.660282','13','常青路',1,'[{\"added\": {}}]',27,1),(71,'2017-06-01 07:04:09.298606','14','长丰常码头',1,'[{\"added\": {}}]',27,1),(72,'2017-06-01 07:04:29.928851','15','CBD西北湖',1,'[{\"added\": {}}]',27,1),(73,'2017-06-01 07:04:55.867948','16','长港路',1,'[{\"added\": {}}]',27,1),(74,'2017-06-01 07:05:12.951283','17','前进江汉',1,'[{\"added\": {}}]',27,1),(75,'2017-06-01 07:05:33.213307','18','塔子湖',1,'[{\"added\": {}}]',27,1),(76,'2017-06-01 07:05:48.161284','19','台北香港路',1,'[{\"added\": {}}]',27,1),(77,'2017-06-01 07:06:00.460060','20','唐家墩',1,'[{\"added\": {}}]',27,1),(78,'2017-06-01 07:06:26.178124','21','武广万松园',1,'[{\"added\": {}}]',27,1),(79,'2017-06-01 07:06:40.480903','22','杨汊湖',1,'[{\"added\": {}}]',27,1),(80,'2017-06-01 07:07:26.414621','23','宝丰崇仁',1,'[{\"added\": {}}]',27,1),(81,'2017-06-01 07:07:38.323649','24','长丰常码头',1,'[{\"added\": {}}]',27,1),(82,'2017-06-01 07:07:53.004314','25','CBD西北湖',1,'[{\"added\": {}}]',27,1),(83,'2017-06-01 07:08:05.951081','26','古田',1,'[{\"added\": {}}]',27,1),(84,'2017-06-01 07:08:20.183644','27','汉正街',1,'[{\"added\": {}}]',27,1),(85,'2017-06-01 07:08:35.283089','28','集贤',1,'[{\"added\": {}}]',27,1),(86,'2017-06-01 07:08:47.605891','29','吴家山',1,'[{\"added\": {}}]',27,1),(87,'2017-06-01 07:09:02.454351','30','宗关',1,'[{\"added\": {}}]',27,1),(88,'2017-06-01 07:12:37.964517','31','常青花园',1,'[{\"added\": {}}]',27,1),(89,'2017-06-01 07:12:52.340672','32','东西湖其它',1,'[{\"added\": {}}]',27,1),(90,'2017-06-01 07:13:04.457499','33','金银湖',1,'[{\"added\": {}}]',27,1),(91,'2017-06-01 07:13:15.872572','34','将军路',1,'[{\"added\": {}}]',27,1),(92,'2017-06-01 07:13:26.633592','35','吴家山',1,'[{\"added\": {}}]',27,1),(93,'2017-06-01 07:14:19.824333','36','白沙洲',1,'[{\"added\": {}}]',27,1),(94,'2017-06-01 07:14:31.630224','37','楚河汉街',1,'[{\"added\": {}}]',27,1),(95,'2017-06-01 07:14:45.555205','38','东湖东亭',1,'[{\"added\": {}}]',27,1),(96,'2017-06-01 07:14:58.392418','39','街道口',1,'[{\"added\": {}}]',27,1),(97,'2017-06-01 07:15:14.128529','40','积玉桥',1,'[{\"added\": {}}]',27,1),(98,'2017-06-01 07:15:38.080700','41','水果湖',1,'[{\"added\": {}}]',27,1),(99,'2017-06-01 07:15:52.327845','42','首义',1,'[{\"added\": {}}]',27,1),(100,'2017-06-01 07:16:17.945993','43','沙湖',1,'[{\"added\": {}}]',27,1),(101,'2017-06-01 07:16:29.840903','44','团结大道',1,'[{\"added\": {}}]',27,1),(102,'2017-06-01 07:16:42.374822','45','武昌火车站',1,'[{\"added\": {}}]',27,1),(103,'2017-06-01 07:16:50.869296','46','徐东',1,'[{\"added\": {}}]',27,1),(104,'2017-06-01 07:17:03.213508','47','杨园',1,'[{\"added\": {}}]',27,1),(105,'2017-06-01 07:17:18.014358','48','中北路',1,'[{\"added\": {}}]',27,1),(106,'2017-06-01 07:17:31.432304','49','中南丁字桥',1,'[{\"added\": {}}]',27,1),(107,'2017-06-01 07:18:05.754487','50','洪山其它',1,'[{\"added\": {}}]',27,1),(108,'2017-06-01 07:18:16.352547','51','青山',1,'[{\"added\": {}}]',27,1),(109,'2017-06-01 07:21:12.303099','52','白沙洲',1,'[{\"added\": {}}]',27,1),(110,'2017-06-01 07:21:21.452816','53','楚河汉街',1,'[{\"added\": {}}]',27,1),(111,'2017-06-01 07:21:34.017427','54','东湖东亭',1,'[{\"added\": {}}]',27,1),(112,'2017-06-01 07:21:45.532592','55','洪山其它',1,'[{\"added\": {}}]',27,1),(113,'2017-06-01 07:21:58.110328','56','虎泉杨家弯',1,'[{\"added\": {}}]',27,1),(114,'2017-06-01 07:22:09.287426','57','街道口',1,'[{\"added\": {}}]',27,1),(115,'2017-06-01 07:24:10.049132','58','珞狮南路',1,'[{\"added\": {}}]',27,1),(116,'2017-06-01 07:25:37.387421','59','老南湖',1,'[{\"added\": {}}]',27,1),(117,'2017-06-01 07:25:56.324698','60','南湖沃尔玛',1,'[{\"added\": {}}]',27,1),(118,'2017-06-01 07:26:06.274119','61','青山',1,'[{\"added\": {}}]',27,1),(119,'2017-06-01 07:26:57.537100','62','沙湖',1,'[{\"added\": {}}]',27,1),(120,'2017-06-01 07:27:12.249166','63','团结大道',1,'[{\"added\": {}}]',27,1),(121,'2017-06-01 07:27:24.592329','64','武昌火车站',1,'[{\"added\": {}}]',27,1),(122,'2017-06-01 07:27:36.045164','65','徐东',1,'[{\"added\": {}}]',27,1),(123,'2017-06-01 07:27:47.409133','66','新南湖',1,'[{\"added\": {}}]',27,1),(124,'2017-06-01 07:28:02.331047','67','中南丁字桥',1,'[{\"added\": {}}]',27,1),(125,'2017-06-01 07:28:19.272057','68','卓刀泉',1,'[{\"added\": {}}]',27,1),(126,'2017-06-01 07:30:20.549634','69','七里庙',1,'[{\"added\": {}}]',27,1),(127,'2017-06-01 07:30:30.606000','70','四新',1,'[{\"added\": {}}]',27,1),(128,'2017-06-01 07:30:47.064546','71','王家湾',1,'[{\"added\": {}}]',27,1),(129,'2017-06-01 07:31:00.957846','72','钟家村',1,'[{\"added\": {}}]',27,1),(130,'2017-06-01 07:31:33.420646','73','关西长职',1,'[{\"added\": {}}]',27,1),(131,'2017-06-01 07:31:45.118280','74','光谷广场',1,'[{\"added\": {}}]',27,1),(132,'2017-06-01 07:31:58.406518','75','关山大道',1,'[{\"added\": {}}]',27,1),(133,'2017-06-01 07:32:09.994964','76','光谷南',1,'[{\"added\": {}}]',27,1),(134,'2017-06-01 07:32:23.223605','77','光谷东',1,'[{\"added\": {}}]',27,1),(135,'2017-06-01 07:32:38.382669','78','洪山其它',1,'[{\"added\": {}}]',27,1),(136,'2017-06-01 07:32:50.055956','79','华科大',1,'[{\"added\": {}}]',27,1),(137,'2017-06-01 07:33:03.441083','80','江厦其它',1,'[{\"added\": {}}]',27,1),(138,'2017-06-01 07:33:27.025884','81','金融港',1,'[{\"added\": {}}]',27,1),(139,'2017-06-01 07:33:52.208449','82','民族大道',1,'[{\"added\": {}}]',27,1),(140,'2017-06-01 07:34:08.568219','83','三环南',1,'[{\"added\": {}}]',27,1),(141,'2017-06-01 07:34:28.481957','84','汤逊湖藏龙岛',1,'[{\"added\": {}}]',27,1),(142,'2017-06-01 07:35:06.396202','85','江厦其它',1,'[{\"added\": {}}]',27,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(33,'commonData','area'),(32,'commonData','decoratedegree'),(27,'commonData','district'),(29,'commonData','newtype'),(26,'commonData','sex'),(30,'commonData','sourcetype'),(31,'commonData','status'),(28,'commonData','subway'),(25,'commonData','usetype'),(5,'contenttypes','contenttype'),(20,'frontsite','account'),(9,'frontsite','cmsstatus'),(18,'frontsite','corporation'),(8,'frontsite','country'),(21,'frontsite','houserequirement'),(19,'frontsite','housesource'),(17,'frontsite','messages'),(7,'frontsite','officebuilding'),(15,'frontsite','order'),(10,'frontsite','rent'),(13,'frontsite','roomdirection'),(12,'frontsite','roomtype'),(16,'frontsite','servicerequirement'),(11,'frontsite','subway'),(14,'frontsite','user'),(23,'publish','news'),(22,'publish','officebuildinglist'),(24,'publish','officelist'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-05-09 09:48:51.787410'),(2,'auth','0001_initial','2017-05-09 09:48:52.133826'),(3,'admin','0001_initial','2017-05-09 09:48:52.224231'),(4,'admin','0002_logentry_remove_auto_add','2017-05-09 09:48:52.264224'),(5,'contenttypes','0002_remove_content_type_name','2017-05-09 09:48:52.376405'),(6,'auth','0002_alter_permission_name_max_length','2017-05-09 09:48:52.422969'),(7,'auth','0003_alter_user_email_max_length','2017-05-09 09:48:52.464585'),(8,'auth','0004_alter_user_username_opts','2017-05-09 09:48:52.483946'),(9,'auth','0005_alter_user_last_login_null','2017-05-09 09:48:52.518915'),(10,'auth','0006_require_contenttypes_0002','2017-05-09 09:48:52.521712'),(11,'auth','0007_alter_validators_add_error_messages','2017-05-09 09:48:52.538310'),(12,'auth','0008_alter_user_username_max_length','2017-05-09 09:48:52.576000'),(13,'sessions','0001_initial','2017-05-09 09:48:52.609352'),(18,'commonData','0001_initial','2017-05-27 09:28:38.166144'),(19,'publish','0001_initial','2017-05-27 09:28:38.705418'),(20,'frontsite','0001_initial','2017-05-27 09:28:39.812280'),(21,'commonData','0002_district_area_type','2017-06-01 06:57:46.352465');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('68oiqlqnysws09sx0ds5oqaqkqgpwl0n','NGI2MTlmMzlhY2Y1Zjc0YmJmMTMzMzY0OTExNTBjYzM0YWM0MWQ3ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjYzODZjYTU1NmVmMjI2NTRhOGY0NGVkNzJlZjJmOTU3NTZiOTA5YmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-31 07:27:13.951942'),('ejr2k0pr3ebv6ox2a4w8stwarryt8q0t','NGI2MTlmMzlhY2Y1Zjc0YmJmMTMzMzY0OTExNTBjYzM0YWM0MWQ3ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjYzODZjYTU1NmVmMjI2NTRhOGY0NGVkNzJlZjJmOTU3NTZiOTA5YmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-31 05:38:07.942002'),('pbi0tv81a733snvp7uqnlc5qpbxyv6th','NGI2MTlmMzlhY2Y1Zjc0YmJmMTMzMzY0OTExNTBjYzM0YWM0MWQ3ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjYzODZjYTU1NmVmMjI2NTRhOGY0NGVkNzJlZjJmOTU3NTZiOTA5YmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-06-14 09:32:31.526463'),('qrme3n8q6udc06r6b3125if2f5dwgcf4','NGI2MTlmMzlhY2Y1Zjc0YmJmMTMzMzY0OTExNTBjYzM0YWM0MWQ3ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjYzODZjYTU1NmVmMjI2NTRhOGY0NGVkNzJlZjJmOTU3NTZiOTA5YmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-25 05:52:10.225350');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_account`
--

DROP TABLE IF EXISTS `frontsite_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telephone` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `nickname` varchar(200) NOT NULL,
  `realname` varchar(200) NOT NULL,
  `IDNum` varchar(200) NOT NULL,
  `age` int(11) NOT NULL,
  `card` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `sex_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_account_sex_id_b2367e4b_fk_commonData_sex_id` (`sex_id`),
  KEY `frontsite_account_status_id_0970e1da_fk_commonData_status_id` (`status_id`),
  CONSTRAINT `frontsite_account_sex_id_b2367e4b_fk_commonData_sex_id` FOREIGN KEY (`sex_id`) REFERENCES `commonData_sex` (`id`),
  CONSTRAINT `frontsite_account_status_id_0970e1da_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_account`
--

LOCK TABLES `frontsite_account` WRITE;
/*!40000 ALTER TABLE `frontsite_account` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_corporation`
--

DROP TABLE IF EXISTS `frontsite_corporation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_corporation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `businessLicence` varchar(100) NOT NULL,
  `corporateCharter` varchar(100) NOT NULL,
  `telephone` varchar(200) NOT NULL,
  `serviceContent` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_corporation_userid_id_b3032d3e_fk_frontsite_account_id` (`userid_id`),
  CONSTRAINT `frontsite_corporation_userid_id_b3032d3e_fk_frontsite_account_id` FOREIGN KEY (`userid_id`) REFERENCES `frontsite_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_corporation`
--

LOCK TABLES `frontsite_corporation` WRITE;
/*!40000 ALTER TABLE `frontsite_corporation` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_corporation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_houserequirement`
--

DROP TABLE IF EXISTS `frontsite_houserequirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_houserequirement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `telephone` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `status_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_houserequi_status_id_f64a20bd_fk_commonDat` (`status_id`),
  KEY `frontsite_houserequi_userid_id_9baf4695_fk_frontsite` (`userid_id`),
  CONSTRAINT `frontsite_houserequi_status_id_f64a20bd_fk_commonDat` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`),
  CONSTRAINT `frontsite_houserequi_userid_id_9baf4695_fk_frontsite` FOREIGN KEY (`userid_id`) REFERENCES `frontsite_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_houserequirement`
--

LOCK TABLES `frontsite_houserequirement` WRITE;
/*!40000 ALTER TABLE `frontsite_houserequirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_houserequirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_housesource`
--

DROP TABLE IF EXISTS `frontsite_housesource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_housesource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `areaNum` int(11) NOT NULL,
  `rent_all_type` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `corporationList` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `image5` varchar(100) NOT NULL,
  `image6` varchar(100) NOT NULL,
  `area_type_id` int(11) NOT NULL,
  `decorate_type_id` int(11) NOT NULL,
  `district_type_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `use_type_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_housesourc_area_type_id_6d028077_fk_commonDat` (`area_type_id`),
  KEY `frontsite_housesourc_decorate_type_id_69c90aba_fk_commonDat` (`decorate_type_id`),
  KEY `frontsite_housesourc_district_type_id_af3bc599_fk_commonDat` (`district_type_id`),
  KEY `frontsite_housesource_status_id_23dd5afa_fk_commonData_status_id` (`status_id`),
  KEY `frontsite_housesourc_use_type_id_25b3468d_fk_commonDat` (`use_type_id`),
  KEY `frontsite_housesource_userid_id_14fbee4d_fk_frontsite_account_id` (`userid_id`),
  CONSTRAINT `frontsite_housesourc_area_type_id_6d028077_fk_commonDat` FOREIGN KEY (`area_type_id`) REFERENCES `commonData_area` (`id`),
  CONSTRAINT `frontsite_housesourc_decorate_type_id_69c90aba_fk_commonDat` FOREIGN KEY (`decorate_type_id`) REFERENCES `commonData_decoratedegree` (`id`),
  CONSTRAINT `frontsite_housesourc_district_type_id_af3bc599_fk_commonDat` FOREIGN KEY (`district_type_id`) REFERENCES `commonData_district` (`id`),
  CONSTRAINT `frontsite_housesourc_use_type_id_25b3468d_fk_commonDat` FOREIGN KEY (`use_type_id`) REFERENCES `commonData_usetype` (`id`),
  CONSTRAINT `frontsite_housesource_status_id_23dd5afa_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`),
  CONSTRAINT `frontsite_housesource_userid_id_14fbee4d_fk_frontsite_account_id` FOREIGN KEY (`userid_id`) REFERENCES `frontsite_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_housesource`
--

LOCK TABLES `frontsite_housesource` WRITE;
/*!40000 ALTER TABLE `frontsite_housesource` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_housesource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_messages`
--

DROP TABLE IF EXISTS `frontsite_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(2000) NOT NULL,
  `body` varchar(2000) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `fromUser_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `toUser_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_messages_fromUser_id_9a7413e6_fk_frontsite_account_id` (`fromUser_id`),
  KEY `frontsite_messages_status_id_5c675997_fk_commonData_status_id` (`status_id`),
  KEY `frontsite_messages_toUser_id_5efd4e41_fk_frontsite_account_id` (`toUser_id`),
  KEY `frontsite_messages_userid_id_7dd01d01_fk_frontsite_account_id` (`userid_id`),
  CONSTRAINT `frontsite_messages_fromUser_id_9a7413e6_fk_frontsite_account_id` FOREIGN KEY (`fromUser_id`) REFERENCES `frontsite_account` (`id`),
  CONSTRAINT `frontsite_messages_status_id_5c675997_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`),
  CONSTRAINT `frontsite_messages_toUser_id_5efd4e41_fk_frontsite_account_id` FOREIGN KEY (`toUser_id`) REFERENCES `frontsite_account` (`id`),
  CONSTRAINT `frontsite_messages_userid_id_7dd01d01_fk_frontsite_account_id` FOREIGN KEY (`userid_id`) REFERENCES `frontsite_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_messages`
--

LOCK TABLES `frontsite_messages` WRITE;
/*!40000 ALTER TABLE `frontsite_messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_order`
--

DROP TABLE IF EXISTS `frontsite_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date published` datetime(6) NOT NULL,
  `officeBuilding_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_order_officeBuilding_id_28fdc379_fk_publish_o` (`officeBuilding_id`),
  KEY `frontsite_order_status_id_206f0e5f_fk_commonData_status_id` (`status_id`),
  KEY `frontsite_order_userid_id_8dbd425e_fk_frontsite_account_id` (`userid_id`),
  CONSTRAINT `frontsite_order_officeBuilding_id_28fdc379_fk_publish_o` FOREIGN KEY (`officeBuilding_id`) REFERENCES `publish_officebuildinglist` (`id`),
  CONSTRAINT `frontsite_order_status_id_206f0e5f_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`),
  CONSTRAINT `frontsite_order_userid_id_8dbd425e_fk_frontsite_account_id` FOREIGN KEY (`userid_id`) REFERENCES `frontsite_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_order`
--

LOCK TABLES `frontsite_order` WRITE;
/*!40000 ALTER TABLE `frontsite_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontsite_servicerequirement`
--

DROP TABLE IF EXISTS `frontsite_servicerequirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontsite_servicerequirement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `telephone` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontsite_servicereq_status_id_087f3b7f_fk_commonDat` (`status_id`),
  CONSTRAINT `frontsite_servicereq_status_id_087f3b7f_fk_commonDat` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontsite_servicerequirement`
--

LOCK TABLES `frontsite_servicerequirement` WRITE;
/*!40000 ALTER TABLE `frontsite_servicerequirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontsite_servicerequirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publish_news`
--

DROP TABLE IF EXISTS `publish_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publish_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `htmlContent` varchar(200) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `image5` varchar(100) NOT NULL,
  `new_type_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `publish_news_new_type_id_6730de2c_fk_commonData_newtype_id` (`new_type_id`),
  KEY `publish_news_status_id_5727942e_fk_commonData_status_id` (`status_id`),
  CONSTRAINT `publish_news_new_type_id_6730de2c_fk_commonData_newtype_id` FOREIGN KEY (`new_type_id`) REFERENCES `commonData_newtype` (`id`),
  CONSTRAINT `publish_news_status_id_5727942e_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publish_news`
--

LOCK TABLES `publish_news` WRITE;
/*!40000 ALTER TABLE `publish_news` DISABLE KEYS */;
/*!40000 ALTER TABLE `publish_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publish_officebuildinglist`
--

DROP TABLE IF EXISTS `publish_officebuildinglist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publish_officebuildinglist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `title_des` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `rent_max_price` int(11) NOT NULL,
  `rent_min_price` int(11) NOT NULL,
  `areaNum` int(11) NOT NULL,
  `floorNum` int(11) NOT NULL,
  `transport` varchar(200) NOT NULL,
  `information` varchar(2000) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `buildTime` datetime(6) NOT NULL,
  `createTime` datetime(6) NOT NULL,
  `location` varchar(200) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `image5` varchar(100) NOT NULL,
  `image6` varchar(100) NOT NULL,
  `area_type_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  `subway_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `publish_officebuildi_area_type_id_b9b606e7_fk_commonDat` (`area_type_id`),
  KEY `publish_officebuildi_status_id_889f9a2c_fk_commonDat` (`status_id`),
  KEY `publish_officebuildi_subway_id_220c51f9_fk_commonDat` (`subway_id`),
  CONSTRAINT `publish_officebuildi_area_type_id_b9b606e7_fk_commonDat` FOREIGN KEY (`area_type_id`) REFERENCES `commonData_area` (`id`),
  CONSTRAINT `publish_officebuildi_status_id_889f9a2c_fk_commonDat` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`),
  CONSTRAINT `publish_officebuildi_subway_id_220c51f9_fk_commonDat` FOREIGN KEY (`subway_id`) REFERENCES `commonData_subway` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publish_officebuildinglist`
--

LOCK TABLES `publish_officebuildinglist` WRITE;
/*!40000 ALTER TABLE `publish_officebuildinglist` DISABLE KEYS */;
/*!40000 ALTER TABLE `publish_officebuildinglist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publish_officelist`
--

DROP TABLE IF EXISTS `publish_officelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publish_officelist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `rent_price` int(11) NOT NULL,
  `areaNum` int(11) NOT NULL,
  `floorNum` int(11) NOT NULL,
  `information` varchar(2000) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `date published` datetime(6) NOT NULL,
  `image1` varchar(100) NOT NULL,
  `image2` varchar(100) NOT NULL,
  `image3` varchar(100) NOT NULL,
  `image4` varchar(100) NOT NULL,
  `image5` varchar(100) NOT NULL,
  `image6` varchar(100) NOT NULL,
  `officeBuilding_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `publish_officelist_officeBuilding_id_bbb7889e_fk_publish_o` (`officeBuilding_id`),
  KEY `publish_officelist_status_id_8fee0fc4_fk_commonData_status_id` (`status_id`),
  CONSTRAINT `publish_officelist_officeBuilding_id_bbb7889e_fk_publish_o` FOREIGN KEY (`officeBuilding_id`) REFERENCES `publish_officebuildinglist` (`id`),
  CONSTRAINT `publish_officelist_status_id_8fee0fc4_fk_commonData_status_id` FOREIGN KEY (`status_id`) REFERENCES `commonData_status` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publish_officelist`
--

LOCK TABLES `publish_officelist` WRITE;
/*!40000 ALTER TABLE `publish_officelist` DISABLE KEYS */;
/*!40000 ALTER TABLE `publish_officelist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-01 15:39:27
