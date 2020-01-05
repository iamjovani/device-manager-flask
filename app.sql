DROP DATABASE IF EXISTS `deviceManager`;
CREATE DATABASE IF NOT EXISTS `deviceManager` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `deviceManager`;

CREATE TABLE IF NOT EXISTS `accounts` 
(
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    `privilege`varchar(20) NOT NULL,
    `location` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `devices`
(
	`name` varchar(12) NOT NULL,
    `serial_number` varchar(13) NOT NULL,
    `installed_by` varchar(13) NOT NULL,
    `operating_sys` varchar(18) NOT NULL,
    `tablet_type`   varchar(18) NOT NULL,
    `model`			varchar(10) NOT NULL,
    `zone`			varchar(10) NOT NULL,
    `condition`     varchar(10) NOT NULL,
    `date_added`	date NOT NULL,
    `date_damaged`  date NOT NULL,
    PRIMARY KEY (`name`, `serial_number`)
    
);

INSERT INTO `devices` (`name`, `serial_number`, `installed_by`, `operating_sys`, `tablet_type`, `model`, `zone`, `condition`, `date_added`, `date_damaged`) 
VALUES('BAP-WKS-A10', '12097885455', 'Grizzle', 'Windows 10', 'Microsoft Surface', 'Pro 4', 'Zone 4', 'Good', '2011-04-25', '2015-06-20');
INSERT INTO `devices`  (`name`, `serial_number`, `installed_by`, `operating_sys`, `tablet_type`, `model`, `zone`, `condition`, `date_added`, `date_damaged`)  
VALUES('BAP-WKS-A15', '14597887685', 'Dwayne', 'Windows 10', 'Microsoft Surface', 'Pro 3', 'Zone 2', 'Good', '2015-04-25', '2019-10-25');
INSERT INTO `devices`  (`name`, `serial_number`, `installed_by`, `operating_sys`, `tablet_type`, `model`, `zone`, `condition`, `date_added`, `date_damaged`)  
VALUES('BAP-WKS-A56', '072832664353', 'Dwayne', 'Windows 10 PRO', 'Microsoft Surface', 'Pro 4', 'Zone 2', 'Good', '2015-11-13', '2019-10-25');

INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `privilege`, `location`) VALUES (1, 'test', 'test', 'test@test.com', 'administrator', 'all');
INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `privilege`, `location`) VALUES (2, 'admin', 'admin', 'admin@admin.com','administrator', 'all');