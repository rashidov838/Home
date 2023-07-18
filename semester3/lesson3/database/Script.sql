--create table if not exists friends(
--	id integer primary key,
--	name  text not NULL ,
--	birthday date not null,
--	email text
--);

--insert  into friends (id,name,birthday,email)
--values 
--	(2,'Xusan','2003-10-01','Xusan@gmail.com'),
--	(3,'Jony','2003-10-01','Jony@gmail.com');

update friends set name='Kom' where name='Jony'; 
select * from friends;
