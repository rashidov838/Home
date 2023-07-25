--create table if not exists restaurant(
--	id integer primary key,
--	name varchar(20) not null,
--	description varchar(100),
--	rating decimal,
--	telephone char(10),
--	hours varchar(100)
--);

--create  table if not exists address(
--	if integer primary key,
--	street_number varchar(10),
--	street_name varchar(20),
--	city varchar(20),
--	state varchar(15),
--	google_map_link varchar(50),
--	restaurant_id integer references restaurant(id) unique
--	);

--create table if not exists category(
--	id varchar(2) primary key,
--	name varchar(20) not null,
--	description varchar(150)
--);


--create table if not exists dish(
--	id integer primary key,
--	name varchar(50),
--	description varchar(200),
--	spicy boolean
--);


--create table if not exists categories_dishes(
--	category_id varchar(2) references category(id),
--	dish_id integer references dish(id),
--	price money,
--	primary key(category_id,dish_id)	
--);
--
--
--create  table if not exists review(
--	id integer primary key,
--	rating decimal ,
--	comment varchar(100),
--	created_at date,
--	restaurant_id integer references restaurant(id)
--	
--);


--insert into restaurant values(1,'Bytes of China',
--        'Delectable Chinese Cuisine',
--        3.9,
--        '6175551212',
--        'Mon - Fri 9:00 am to 9:00 pm, Weekends 10:00 am to 11:00 pm');
--       
--       
--insert  into address values(  1,
--        '2020',
--        'Busy Street',
--        'Chinatown',
--        'MA',
--        'http://bit.ly/BytesOfChina',
--        1);
--       
--       
--insert  into review values( 1,
--        5.0,
--        'Would love to host another birthday party at Bytes of China!',
--        '2020-05-20',
--        1);


insert into category values(
        'LS',
        'Luncheon Specials',
        'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice  between 11:00 am and 3:00 pm from Monday to Friday.'
    );
insert into category values ('C', 'Chicken', null);


insert into category values(
	'HS', 'House Specials', null
);



--insert into dish values (
--        1,
--        'Chicken with Broccoli',
--        'Diced chicken stir-fried with succulent broccoli florets',
--        false
--);


insert into dish values (
        2,
        'Sweet and Sour Chicken',
        'Marinated chicken with tangy sweet and sour sauce together with pineapples and green peppers',
        false
	
);



insert into dish values (
	  3,
        'Chicken Wings',
        'Finger-licking mouth-watering entree to spice up any lunch or dinner',
        true
    );

   
   
--  insert into dish values(
--  4,
--        'Beef with Garlic Sauce',
--        'Sliced beef steak marinated in garlic sauce for that tangy flavor',
--        true
--  );
    

--  insert into dish values(
--  5,
--        'Fresh Mushroom with Snow Peapods and Baby Corns',
--        'Colorful entree perfect for vegetarians and mushroom lovers',
--        false
--  );
--    insert into dish values(
--        6,
--        'Sesame Chicken',
--        'Crispy chunks of chicken flavored with savory sesame sauce',
--        false
--  );
   
--    insert into dish values(7,
--        'Special Minced Chicken',
--        'Marinated chicken breast sauteed with colorful vegetables topped with pine nuts and shredded lettuce.',
--        false
  );
--    insert into dish values(
--        8,
--        'Hunan Special Half & Half',
--        'Shredded beef in Peking sauce and shredded chicken in garlic sauce',
--        true
--  );
  
 
 
 
-- insert into categories_dishes values('C', 1, 6.95);
 

-- insert into categories_dishes values('C', 3, 6.95);



-- insert into categories_dishes values ('LS', 1, 8.95);


-- insert into categories_dishes values ('LS', 4, 8.95);

-- insert into categories_dishes values('LS', 5, 8.95);

-- insert into categories_dishes values('HS', 6, 15.95);

-- insert into categories_dishes values ('HS', 7, 16.95);
--
-- insert into categories_dishes values ('HS', 8, 17.95);
 
 
-- Task-1
-- create table customer(
-- 	customer_id integer generated always as identity primary key,
-- 	first_name varchar(100) not null,
-- 	last_name varchar(100) not null,
-- 	email_address varchar(40) null,
-- 	restaurant_id integer references restaurant(id)
-- );
-- 
-- create table customers_log(
-- 	changed_by varchar(100) not null,
-- 	time_changed timestamp not null
-- );
-- 
 
-- Task-2
 
CREATE OR REPLACE FUNCTION log_customers_change() RETURNS TRIGGER AS $$ BEGIN
INSERT INTO
    customers_log (changed_by, time_changed)
VALUES
    (User, DATE_TRUNC('minute', NOW()));
RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

--Update
create trigger log_customers_change before update on address for each row 
execute procedure log_customers_change();


select * from address;

update address  set street_name ='Bekzod street' where city ='Chinatown';

select * from address;

--for category
create trigger log_customers_change before update on category for each row 
execute procedure log_customers_change();

select * from category ;

update category  set description = 'it is chicken ' where name ='Chicken';

select * from category;
--for dish
create trigger log_customers_change before update on   dish 
for each row execute procedure log_customers_change();

update dish set name = 'New food' where id = 1;


select * from dish ;



--for review

create trigger log_customers_change before update on review for each row 
execute procedure  log_customers_change();

select * from review;

update review set rating = 6 where id =1;





--Task-3 Update
create trigger log_customers_change_for_insert after insert on address for each row 
execute function log_customers_change();

select * from address;

insert into address  values(1,2021,'chilanzar street','Tashkent','AC','http://google.com');

create trigger log_customers_change_for_insert after insert on category for each row 
execute function log_customers_change();

insert  into category  values('RT','Beef','it is beef');
select * from category;


create trigger log_customers_change_for_insert after insert on dish for each row 
execute function log_customers_change();

insert into dish values(9,'Beef and chicken', 'it is mix food', false);

select * from dish;


create trigger log_customers_change_for_insert after insert on review for each row 
execute function log_customers_change();

insert into review values(1,6,'It is the best','2002-01-10',1);

select * from review;


--Task-4 Delete

create trigger log_customers_change_for_delete after delete on review for each row 
execute function log_customers_change();

delete from review where id =1;

select * from review;

create trigger log_customers_change_for_delete after delete on address for each row 
execute function log_customers_change();

delete  from address  where if =2;

select * from address ;

create trigger log_customers_change_for_delete after delete on dish for each row 
execute function log_customers_change();

delete  from dish  where id =2;

select * from dish ;


create trigger log_customers_change_for_delete after delete on category for each row 
execute function log_customers_change();

delete  from category  where name ='Beef';

select * from category;




