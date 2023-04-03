-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- displays tv_shows.title - tv_shows_genres.genre_id
-- arranged in ASC by tv_shows.title and tv_show_genres.genre_id
-- uses select only once
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_shows_genres
WHERE tv_shows.id = tv_shows_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
