--CREATE TABLE customers_log (
--    changed_by VARCHAR(100) NOT NULL,
--    time_changed TIMESTAMP NOT NULL
--);
--CREATE OR REPLACE FUNCTION statement_function() RETURNS TRIGGER AS $$ BEGIN
--INSERT INTO
--    customers_log 
--VALUES
--    ( (select first_name from customers limit 1),NOW());
--RETURN NEW;
--END;
--$$ LANGUAGE PLPGSQL;
--
--
--create trigger statement_function_trigger after update on customers
--for each statement 
--execute procedure statement_function();
--
--
--select * from customers;
--
--update customers set years_old = years_old +1 where customer_id =2;
--select * from customers_log;

CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY,
    high_spender INTEGER NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    total_spent INTEGER NULL
);

select * from clients ;


create or replace function set_low_spender() returns trigger as $$
begin 
		new.high_spender=4;
		return new;
end;
$$ language PLPGSQL;


create or replace function set_high_spender() returns trigger as $$
begin 
		new.high_spender=8;
		return new;
end;
$$ language PLPGSQL;


create or replace trigger update_trigger_high 
before insert  on clients 
for each row 
when (new.total_spent >= 1000)
execute procedure set_high_spender();





create or replace trigger update_trigger_low 
before insert on clients 
for each row 
when (new.total_spent < 1000)
execute procedure set_low_spender();



update clients set total_spent = 5000 where last_name = 'Edward';



insert into clients values (4,0,'Bekzod','QWERTYU',100000);
select * from clients ;



