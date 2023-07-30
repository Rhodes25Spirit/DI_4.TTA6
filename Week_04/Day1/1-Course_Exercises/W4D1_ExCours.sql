-- create table house_expenses (
-- id serial primary key, 
-- date_paid date, 
-- electricity float,
-- water float, 
-- paid_by varchar(50)
-- );

-- insert into house_expenses (date_paid, electricity, water, paid_by) 
-- values 
-- ('2005-02-11', 56.5, 20.2, 'Adam'),
-- ('2005-03-12', 60.5, 18.2, 'Yossi'),
-- ('2005-04-13', 70.5, 28.2, 'Yossi'),
-- ('2005-05-14', 65.5, 26.2, 'Adam'),
-- ('2005-06-15', 40.5, 10.2, 'Yossi'); 

-- select * from house_expenses;
-- select electricity from house_expenses;
-- select electricity, water from house_expenses;


-- select * from house_expenses where id = 1 or id = 2;
-- select * from house_expenses where id < 3;
-- select * from house_expenses where id in (1, 2);

-- select count(paid_by) from
-- house_expenses where paid_by = 'Yossi'

-- select max(water) from
-- house_expenses where paid_by = 'Yossi'

-- select min(electricity) from
-- house_expenses

-- select avg(electricity+water) as average_sum from
-- house_expenses where paid_by = 'Yossi'

-- select sum(electricity+water) from
-- house_expenses where paid_by = 'Yossi'


-- select paid_by, sum (electricity) from house_expenses
-- group by paid_by;

-- select paid_by, count(paid_by) from house_expenses
-- group by paid_by;

-- select paid_by, sum(electricity + water), max(electricity + water)
-- from house_expenses where electricity > 60
-- group by paid_by;

select water,electricity from house_expenses;
update house_expenses

set electricity = 33, water = 25 where id = 2;
-- update house_expenses
-- set paid_by = 'Lena' where id = 1;
-- update house_expenses
-- set electricity = 0 where paid_by = 'Lena'
-- delete from house_expenses where electricity < 70
-- delete from house_expenses where date_paid < '2005-01-01'