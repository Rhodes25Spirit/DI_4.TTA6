-- COMMENT ON DATABASE "Bootcamp"
--     IS 'W4D1 Exercise XP +';
	
-- CREATE TABLE students(
-- stud_id SERIAL PRIMARY KEY,
-- last_name VARCHAR (40) NOT NULL,	
-- first_name VARCHAR (40) NOT NULL,
-- birthdate DATE NOT NULL
-- )
	
-- INSERT INTO students (first_name, last_name, birthdate)
-- VALUES
--  ('Marc', 'Benichou', '02/11/1998'),
--  ('Yoan', 'Cohen', '03/12/2010'),
-- 	('Lea', 'Benichou', 	'27/07/1987'),
-- 	('Amelia', 	'Dux' ,	'07/04/1996'),
-- 	('David' ,	'Grez' ,	'14/06/2003'),
-- 	('Omer' ,	'Simpson' ,	'03/10/1980');
	
-- INSERT INTO students (last_name, first_name, birthdate)
-- VALUES('Levy','Anna','06/03/1987');

-- SELECT * FROM students;

-- SELECT first_name, last_name FROM students;

-- SELECT first_name, last_name FROM students WHERE stud_id = 2;

-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR  = 'Marc';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';

-- SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

-- SELECT first_name  PATINDEX('%a%', first_name) birthdate FROM students;

-- #### Pas la meme logique que Word... Autre soluce à trouver####

-- SELECT first_name, last_name FROM students WHERE stud_id = 1 AND stud_id = 3;

SELECT * FROM students WHERE birthdate >= '01/01/2000';
