-- CREATE TABLE Actors_2(
--  actorid SERIAL PRIMARY KEY,
--  first_n VARCHAR (50) NOT NULL,
--  last_n VARCHAR (100) NOT NULL,
--  ages DATE NOT NULL,
--  number_of_oscars SMALLINT NOT NULL,
--  gender_class character varying(10));

-- INSERT INTO Actors_2(first_n, last_n, ages, number_of_oscars, gender_class)
-- VALUES('Matt','Damon','08/10/1970', 5, 'Male');

-- INSERT INTO Actors_2(first_n, last_n, ages, number_of_oscars, gender_class)
-- VALUES('George','Clooney','06/05/1961', 2, 'Male');

-- INSERT INTO Actors_2(first_n, last_n, ages, number_of_oscars, gender_class)
-- VALUES('Jane','Berquine','15/09/1916', 8, 'Female');

-- INSERT INTO Actors_2(first_n, last_n, ages, number_of_oscars, gender_class)
-- VALUES('Scarlet','Johanson','25/07/1964', 4, 'Female');

-- INSERT INTO Actors_2(first_n, last_n, ages, number_of_oscars, gender_class)
-- VALUES('Eddie ','Redmayne','06/01/1982', 0, 'Male'),
-- ('Jude ','Law','29/12/1972', 3, 'Male'),
-- ('Mads ','Mikkelsen','22/11/1965', 1, 'Male');

-- *************************************************************

-- SELECT
--    first_n
-- FROM
--    Actors_2;

-- SELECT * FROM Actors_2 WHERE first_n = 'Matt';

-- SELECT * FROM Actors_2 WHERE number_of_oscars >= 3;

-- SELECT last_n FROM Actors_2 WHERE first_n != 'Matt' ;

-- SELECT first_n, last_n FROM Actors_2 WHERE first_n = 'Matt'  AND 
-- last_n = 'Damon' ;
-- -- 1 row is retrieved, with the field last_n and first_n

-- SELECT first_n, last_n FROM Actors_2 WHERE first_n = 'Matt'  AND 
-- last_n = 'Clooney' ;
-- -- 0 row is retrieved, because there is not an existing actor in the table, with the first_n "Matt" and the last_n "Clooney"

-- SELECT first_n, last_n FROM Actors_2 WHERE first_n = 'Matt'  OR  
-- number_of_oscars = 2 ;
-- -- 2 rows are retrieved. 

-- SELECT * FROM Actors_2 WHERE (ages > '1983-07-30' OR number_of_oscars >= 4) AND NOT (gender_class = 'Female');

-- SELECT * FROM Actors_2 WHERE gender_class IS NOT NULL;

-- SELECT * FROM Actors_2 WHERE gender_class IS NULL;

-- SELECT * FROM Actors_2 WHERE last_n LIKE '%on%';  
-- #La place du % defini la position de la recherche#

-- -- If we want to skip the first two actors and display the next actors.
-- SELECT * FROM Actors_2 WHERE ages < '2083-07-30' LIMIT 3 OFFSET 2;

-- SELECT * FROM Actors_2 WHERE ages > '1966-01-01' ORDER BY first_n ASC

-- SELECT * FROM Actors_2 LIMIT 4;

-- SELECT * FROM Actors_2 ORDER BY last_n DESC

-- SELECT * FROM Actors_2 WHERE first_n LIKE '%e%';

-- SELECT * FROM Actors_2 WHERE number_of_oscars >= 5;

-- *************************************************************

-- UPDATE Actors_2 SET ages='1970-01-01' WHERE first_n='Matt' AND last_n='Damon'
-- RETURNING
-- 	actorid,
-- 	first_n,
-- 	last_n,
-- 	ages, 
-- 	gender_class;


-- UPDATE Actors_2 SET first_n='Maty' WHERE ages='1970-01-01' AND last_n='Damon'
-- RETURNING
-- 	actorid,
-- 	first_n,
-- 	last_n,
-- 	ages, 
-- 	gender_class;
	

-- UPDATE Actors_2 SET number_of_oscars= 6 WHERE first_n='George' AND last_n='Clooney'
-- RETURNING
-- 	actorid,
-- 	first_n,
-- 	last_n,
-- 	ages, 
-- 	number_of_oscars;


ALTER TABLE actors_2 RENAME COLUMN ages TO birthday;
