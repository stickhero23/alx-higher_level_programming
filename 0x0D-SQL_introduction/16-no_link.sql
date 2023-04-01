-- list all records from second_table
-- exclude rows without name value
-- score, name in this order
-- arranged in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
