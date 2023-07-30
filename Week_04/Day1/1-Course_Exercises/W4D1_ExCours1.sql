-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Jane','Berquine','15/09/1916', 8);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Scarlet','Johanson','25/07/1964', 4);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Eddie ','Redmayne','06/01/1982', 0),
-- ('Jude ','Law','29/12/1972', 3),
-- ('Mads ','Mikkelsen','22/11/1965', 1);

-- *************************************************************

-- SELECT
--    first_name
-- FROM
--    actors;

-- SELECT * FROM actors WHERE first_name = 'Matt';

-- SELECT * FROM actors WHERE number_oscars >= 3;

-- SELECT last_name FROM actors WHERE first_name != 'Matt' ;

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Damon' ;
-- -- 1 row is retrieved, with the field last_name and first_name

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  AND 
-- last_name = 'Clooney' ;
-- -- 0 row is retrieved, because there is not an existing actor in the table, with the first_name "Matt" and the last_name "Clooney"

-- SELECT first_name, last_name FROM actors WHERE first_name = 'Matt'  OR  
-- number_oscars = 2 ;
-- -- 2 rows are retrieved. 

-- ALTER TABLE actors
-- ADD gender varchar(6);               Ajouté à chaque acteur manuellement

-- SELECT * FROM actors WHERE (age > '1983-07-30' OR number_oscars >= 4) AND NOT (gender = 'Female');

-- SELECT * FROM actors WHERE gender IS NOT NULL;

-- SELECT * FROM actors WHERE gender IS NULL;

-- SELECT * FROM actors WHERE last_name LIKE '%on%';  #La place du % defini la position de la recherche#

-- -- If we want to skip the first two actors and display the next three actors.
-- SELECT * FROM actors WHERE age < '2083-07-30' LIMIT 3 OFFSET 2;

-- SELECT * FROM actors WHERE age > '1966-01-01' ORDER BY first_name ASC

-- SELECT * FROM actors LIMIT 4;

-- SELECT * FROM actors ORDER BY last_name DESC

-- SELECT * FROM actors WHERE first_name LIKE '%e%';

-- SELECT * FROM actors WHERE number_oscars >= 5;

-- *************************************************************

-- UPDATE actors SET age='1970-01-01' WHERE first_name='Matt' AND last_name='Damon'
-- RETURNING
-- 	actor_id,
-- 	first_name,
-- 	last_name,
-- 	age, 
-- 	gender;

-- Delete the 6 record in the table and return it
-- DELETE FROM actors WHERE actor_id=6
-- RETURNING actor_id, first_name, last_name, number_oscars;
-- -- Peut-on annuler la suppression precedente?? Avec un BackUP(BU) Fait préalablement.

INSERT INTO actors (actor_id, first_name, last_name, age, number_oscars, gender)
VALUES(8, 'Jude','Law','29/12/1972', 3,);