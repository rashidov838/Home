create table restorant(
	id integer primary key,
	title varchar(100),
	content_restorant varchar(50),
	address text,
	nickname text,
	code text,
	number_code integer
);

create table information(
	id integer references restorant(id),
	telephone integer unique,
	hour_from date,
	hour_to date,
	rating integer,
	google_map text
);



create table menu(
	id integer references restorant(id),
	type_food varchar(50) primary key
);
--

create table food(
	title_food varchar(50),
	category varchar(100) primary key,
	price_food float,
	content_food text
);


create table food_category(
	type_food varchar(50) references menu(type_food),
	food_category varchar(20) references food(category),
	primary key (type_food, food_category)
)