

-- SELECT first_name+''+last_name as full_name from people;



-- SELECT 13+13 from people;





-- SELECT first_name || ' ' ||last_name as full_name from people;



-- SELECT abs(19999);



-- SELECT square(5);





-- SELECT POWER(4, 2);



-- select pi();





-- SELECT first_name, round(avg(age/2)) as  age from people limit 5;







-- SELECT first_name || ' ' || last_name as fullname, city,state_code,shirt_or_hat, quiz_points-age as new  from people GROUP BY 3 ORDER BY 3 ASC  ;





-- 

-- SELECT first_name, age,

-- CASE

-- 	WHEN age=18 THEN &quot;Young boy&quot;

-- 	WHEN age &lt;=30 THEN &quot;Medium&quot;

-- 	when age &gt;40 THEN &quot;Old boy&quot;

-- 	ELSE &quot;Nothing&quot;

-- END as &quot;Category&quot;

-- from people GROUP By &quot;Category&quot;;





-- Логические операторы  and or not 



-- SELECT first_name,last_name,age from people where not age = 22 ORDER By age DESC;





-- SELECT first_name,last_name,age from people where age = 35 or  age=32;







-- SELECT first_name,last_name,age from people where state_code=&quot;AL5&quot; and age=60;







-- SELECT first_name,last_name,age from people where  age in (23,45,67);



-- SELECT * from people where not(age=27 or age=29 or age=31) ORDER By age ASC;








