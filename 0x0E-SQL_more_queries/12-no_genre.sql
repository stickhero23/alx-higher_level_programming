-- lists all shows in hbtn_0d_tvshows without genre linked
-- displays tv_shows.title - tv_show_genres.genre_id
-- ordered by tv_shows.title and tv_show_genres.genre_id in ASC
-- use select once
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_grenres.genre_id IS NULL
ORDER BY tv-shows.title, tv_show_genres.genre_id ASC;
