-- converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- converts first_table and 'name' file in the table to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert first_table
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert name field
USE hbtn_0c_0;
ALTER TABLE first_table
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
