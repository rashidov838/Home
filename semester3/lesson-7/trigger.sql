
--create schema cc_user;
--set search_path = cc_user;
--
--create table customers(
--	customer_id integer generated always as identity primary key,
--	first_name varchar(100) not null,
--	last_name varchar(100) not null,
--	email_address varchar(300) not null,
--	home_phone varchar(50) not null,
--	city varchar(100) not null,
--	state_name varchar(50),
--	years_old integer null
--	);
	


--copy customers(
--	first_name,
--    last_name,
--    email_address,
--    home_phone,
--    city,
--    state_name,
--    years_old
--)from 'C:\Users\WINDOWS 10\Documents\Githome\semester3\lesson-7\customer.csv' DELIMITER ',' CSV HEADER;



--
--create  or replace function insert_function() returns trigger as 
--$$ begin
--	new.last_name :='UNKNOWN';
--	return new;
--end; $$ 
--language PLPGSQL;
 

--create trigger insert_function before update on customers for each row 
--execute  procedure  insert_function();

 
--select * from customers;

update customers set years_old = 42 where last_name = 'Hall';

select * from customers;   


