--create table  book(
----	id integer primary key,
--	title varchar(100),
--	isbn varchar(50) primary key,
--	pages integer,
--	price money,
--	description varchar(256),
--	publisher varchar(100)
--	);
--
--create  table chapter(
--	id integer primary key,
--	number integer,
--	title varchar(50),
--	content varchar(1024),
--	book_isbn varchar(50) references book(isbn)
--);
--
--create table author(
--	name varchar(50),
--	bio varchar(100),
--	email varchar(20) primary key
--);
--
--create table popular_books(
--	book_title varchar(100),
--	author_name varchar(50),
--	number_sold integer,
--	number_previewed integer,
--	primary key (book_title, author_name)
--);
--
--create table book_details(
--	id integer primary key,
--	rating decimal,
--	language_of_type varchar(10),
--	keywords_of_type text,
--	date_published  date,
--	book_isbn varchar(50) references book(isbn) unique
--);


create table page(
	id integer primary key,
	content_page text,
	header_page varchar(20),
	footer varchar(20)
);

create table books_authors(
	book_isbn varchar(50) references book(isbn),
	author_email varchar(20) references author(email),
	primary key (book_isbn,author_email)
);


--select constraint_name,table_name,column_name from 
--information_schema.key_column_usage
--where table_name= 'popular_books';