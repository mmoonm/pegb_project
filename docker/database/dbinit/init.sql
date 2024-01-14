# create  users
CREATE USER 'pegb' @'%' IDENTIFIED WITH mysql_native_password BY 'pegb';
CREATE USER 'pegb' @'localhost' IDENTIFIED WITH mysql_native_password BY 'pegb';

FLUSH PRIVILEGES;

# create databases
CREATE DATABASE IF NOT EXISTS `pegb` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# grant super user permission to user
GRANT ALL PRIVILEGES ON *.* TO 'pegb' @'%';
GRANT ALL PRIVILEGES ON *.* TO 'pegb' @'localhost';

FLUSH PRIVILEGES;