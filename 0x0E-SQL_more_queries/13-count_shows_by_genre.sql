-- lists all genres and the number of shows linked to each
-- displays tv_show_grenre, number of shows linked to this genre
-- first column is genre
-- second column number_of_shows
-- No NULL entries
-- order byu number of shows in DESC
-- use select once
SELECT tv_genres.name AS genre, COUNT(*) AS 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
