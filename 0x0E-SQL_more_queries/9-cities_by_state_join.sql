-- list all cities in hbtn_0d_usa
-- displays cities.id, cities.name, states.name
-- sorted in ASC by cities.id
-- One SELECT statement
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = state_id
ORDER BY cities.id ASC;
