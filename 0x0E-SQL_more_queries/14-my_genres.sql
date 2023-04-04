-- lists all genres of the show Dexter
-- displats tv_genres.name
-- ordered by genre name in ASC
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_show.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name ASC;
