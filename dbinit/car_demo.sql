CREATE DATABASE IF NOT EXISTS car_demo DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'carlot'@'%' IDENTIFIED BY 'I@mR00t';
GRANT SELECT, DELETE, INSERT, UPDATE ON car_demo.* TO 'carlot'@'%' IDENTIFIED By 'I@mR00t';
--
-- Table structure for table `car_demo`
--

DROP TABLE IF EXISTS `car_demo`;

CREATE TABLE `car_demo` (
  `car_id` int(11) NOT NULL AUTO_INCREMENT,
  `car_make` varchar(100) NOT NULL,
  `car_model` varchar(40) NOT NULL,
  `car_year` int(11) NOT NULL,
  `car_color` varchar(40) NOT NULL,
  `car_hp` int(11) NOT NULL,
  PRIMARY KEY (`car_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `car_demo`
--

LOCK TABLES `car_demo` WRITE;
/*!40000 ALTER TABLE `car_demo` DISABLE KEYS */;
INSERT INTO `car_demo` VALUES (1,'Chevrolet','Camaro SS',2018, 'Black',500),
(2,'Chevrolet','Corvette ZR1',2016,'Red',400),
(3,'Cadallac','CTS-V',2020,'Black',300),
(4,'Mercedes-Benz','C63 AMG',2021,'White',350),
(5,'Nissan','GT-R',2021,'Silver',324),
(6,'Ford','GT',2021,'Red',280),
(7,'Ford','Pinto',1971,'Brown',80),
(8,'Ferrari','458 Italia',2015,'Red',500),
(9,'Lamborghini','Diablo SV',1999,'Black',550),
(10,'Chevrolet','Camaro SS',1969,'Blue',305);

UNLOCK TABLES;

