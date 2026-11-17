sudo apt update
sudo apt upgrade

sudo apt install mariadb-server mariadb-client

sudo apt install python3-pip
sudo apt install python3-mysqldb

sudo mysql_secure_installation
sudo mysql -u root -p

CREATE DATABASE exampledb;
CREATE USER 'exampleuser'@'localhost' IDENTIFIED BY 'pimylifeup';
USE exampledb;
CREATE TABLE Sensorstats (date_time VARCHAR(50), irsensorstat FLOAT);
GRANT ALL PRIVILEGES ON exampledb.* TO 'exampleuser'@'localhost';
FLUSH PRIVILEGES;
quit;

python3 ir_sensor.py

sudo mysql -u root -p
USE exampledb;
SELECT * FROM Sensorstats;