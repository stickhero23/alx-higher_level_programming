-- create database hbtn_0d_2 and user user_0d_2
-- Grant SELECT privilege in hbtn_0d_2 to user_0d_2
-- password for user_0d_2 is user_0d_2_pwd
-- Not fail if database exists
-- Not fail if user_0d_2 already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

-- Grant select privilege
GRANT SELECT PRIVILEGE ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

