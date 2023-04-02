-- display max temperature of each state order by state name
SELECT state, max(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
