-- creates database hbtn_0d_usa and table cities
-- cities has id INT, UNIQUE, AUTO, NOT NULL, PRIMARY KEY
-- state_id NOT NULL, FOREIGN KEY ref id of the state table
-- name VARCHAR(256)
-- should not fail if exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
