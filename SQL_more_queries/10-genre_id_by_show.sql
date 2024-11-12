-- Script that all tv shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genre ON tv_shows.id = tv_show_genre.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genre_id ASC;
