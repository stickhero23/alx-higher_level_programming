-- lists all shows contained in the database
-- displays tv_shows.title - tv_show_genres.genre_id
-- NULL where there is no genre
-- sorted in ASC by tv_shows.title and tv_show_genres.genre_id
-- uses SELECT only once
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
