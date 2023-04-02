-- create user_0d_1 with password user_0d_1_pwd
-- Granted all privilege on MySQL server
-- script schould not fail if user_0d_1 alter exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
