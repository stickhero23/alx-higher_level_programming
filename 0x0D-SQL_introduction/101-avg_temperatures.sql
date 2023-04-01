--displays the average temperature by city ordered by temp DESC
SELECT city, avg(value) as avg_temp FROM temperature
GROUP BY value
ORDER BY avg_temp DESC;
