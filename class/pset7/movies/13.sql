SELECT DISTINCT name
FROM people
JOIN stars ON stars.person_id = people.id
--JOIN movies ON stars.movie_id = movies.id
WHERE movie_id IN
(SELECT movie_id
FROM stars
JOIN people ON stars.person_id = people.id
WHERE birth = '1958' AND name ='Kevin Bacon')
AND name != 'Kevin Bacon';
