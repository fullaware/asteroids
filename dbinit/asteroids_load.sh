#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install mysql-server -y
mysqladmin -u root password 'I@mR00t'
mysql -u root -pI@mR00t -e "CREATE USER 'asteroid'@'%' IDENTIFIED BY 'IamR00t'; GRANT ALL PRIVILEGES ON *.* TO 'asteroid'@'%' WITH GRANT OPTION;"
mysql -u asteroid -pI@mR00t -e "CREATE DATABASE asteroids DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;"
mysql -u asteroid -pI@mR00t < asteroids.sql
