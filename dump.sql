CREATE USER 'pledgx_user'@'%' IDENTIFIED BY '';

GRANT ALL PRIVILEGES ON *.* TO 'pledgx_user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS pledgx;

USE pledgx;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `job_title` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`id`, `firstName`, `lastName`, `phoneNumber`, `jobTitle`, `country`) VALUES
(0, '', '', '', '', '');

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);
COMMIT;
