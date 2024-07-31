CREATE USER 'pledgx_user'@'%' IDENTIFIED BY '';

GRANT ALL PRIVILEGES ON *.* TO 'pledgx_user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS pledgx;

USE pledgx;

CREATE TABLE `users` (
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `phoneNumber` varchar(20) NOT NULL,
  `jobTitle` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;
