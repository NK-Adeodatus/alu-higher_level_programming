-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
