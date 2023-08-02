-- COMMENT ON DATABASE "W4D2_ExCours"
-- --     IS 'W4D2_ExCours';

-- CREATE TABLE Acteurs(
--   acteur_id SERIAL PRIMARY KEY,
--   f_name VARCHAR (50) NOT NULL,
--   l_name VARCHAR (100) NOT NULL,
--   dob DATE NOT NULL,
--   number_of_oscars SMALLINT NOT NULL
--  );
 
--  INSERT INTO acteurs (f_name, l_name, dob, number_of_oscars)
--  VALUES
--  ('Matt','Damon','08/10/1970', 5),
--  ('George','Clooney','06/05/1961', 2),
--  ('Brad','Pitt','1980-04-22', 1),
--  ('Maty','Damon','1982-11-22', 2),
--  ('Patrick','Jolie','1980-04-22', 1),
--  ('Marc','Benichou','1998-11-02',0), 
--  ('Yoan','Cohen','2010-12-03',0), 
--  ('Lea','Benichou','1987-07-27',0), 
--  ('Amelia','Dux','1996-04-07',0), 
--  ('David','Grez','2003-06-14',0), 
--  ('Omer','Simpson','1980-10-03',1);

----------------------------------------------------------------- 
--  create table continent (
--  id smallserial primary key, 
--  c_name varchar(50) not null, 
--  continent_code smallint not null check(continent_code < 50)
--  ); 
 
 -- 1 - add a new column
--  alter table acteurs 
--  add column continent_code smallint; 
 
 -- 2 - specify the new column as foreign key
--  alter table acteurs
--  add foreign key (continent_code) references continent(id);
 
--  insert into continent (c_name, continent_code) 
--  values
--  ('USA', 1),
--  ('France', 33),
--  ('Britain', 44);


-- update acteurs set continent_code = 2 where f_name = 'Matt';

--  update acteurs set continent_code = (select id from continent where c_name = 'USA') where f_name in ('George');
 
-- update acteurs 
-- set continent_code = (select continent.id from continent where continent.c_name = 'USA') 
-- where acteurs.acteur_id > 9
-- RETURNING *;

-- update acteurs 
-- set continent_code = (select continent.id from continent where continent.c_name = 'Britain') 
-- where acteurs.acteur_id BETWEEN 4 AND 7
-- RETURNING *;

-- CREATE TABLE films (
--  F_id serial primary key, 
--  titre varchar(50) not null,
--  continent_id smallint references continent(id)
--  );
 
--  insert into films (titre, continent_id)
--  values 
--  ('Will Hunting', (select id from continent where c_name = 'USA')),
--  ('Jason Bourne', (select id from continent where c_name = 'USA')), 
--  ('Ocean Twelve', (select id from continent where c_name = 'Britain')), 
--  ('Oceans Eight', (select id from continent where c_name = 'Britain')),
--  ('Bleu Dragons', (select id from continent where c_name = 'France'))
--  RETURNING *;
 
--  create table acteurs_films (
--  af_id serial primary key,
--  acteur_id int references acteurs(acteur_id),
--  films_id smallint references films(F_id)
--  );
 
 insert into acteurs_films (acteur_id, films_id) values
 ((select acteur_id from acteurs where f_name = 'Matt'), (select f_id from films where titre = 'Good Will Hunting')),
 ((select acteur_id from acteurs where f_name = 'Matt'), (select f_id from films where titre = 'Jason Bourne')),
 ((select acteur_id from acteurs where f_name = 'Matt'), (select f_id from films where titre = 'Oceans Twelve')),
 ((select acteur_id from acteurs where f_name = 'Matt'), (select f_id from films where titre = 'Oceans 8')),
 ((select acteur_id from acteurs where f_name = 'Maty'), (select f_id from films where titre = 'Oceans 8'))
 ((select acteur_id from acteurs where f_name = 'Yoan'), (select f_id from films where titre = 'Bleu Dragons'))
 RETURNING * ;
 






