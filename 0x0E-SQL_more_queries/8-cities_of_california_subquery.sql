-- lists all cities of California in the database
-- sort in ascending order by cities.id
-- DO NOT use JOIN
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
GROUP BY id
ORDER BY id ASC;
