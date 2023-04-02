--displays the average temperature by city ordered by temp DESC
SELECT city, AVG(value) as avg_temp FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
