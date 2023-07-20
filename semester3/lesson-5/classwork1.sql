-- SELECT Name from country
-- GROUP by 1
-- ORDER by 1;


-- SELECT name from Country where Continent = 'Asia';

-- SELECT Name, Continent, IndepYear from Country where IndepYear > 1990 
-- ORDER By IndepYear;


-- SELECT IndepYear,Population from Country where IndepYear is not null and Population BETWEEN 15000 and 24318000 LIMIT 10;



SELECT Name, HeadOfState,
	CASE
		WHEN GovernmentForm ='Republic' THEN 'Республика'
		WHEN GovernmentForm ='Monarchy' THEN 'Монархния'
		WHEN GovernmentForm ='Federal Republic' THEN 'Федерация'
	ELSE 'Иные виды правления'
	END as 'Форма управления'
from Country;
 


SELECT sum(Population) as "сумма населения" from Country;


SELECT avg(LifeExpectancy) as 'среднее количество продолжения' FROM Country;


SELECT max(LifeExpectancy) as 'максимальное продолжения жизни',Continent FROM Country;
SELECT Name ,sum(Population)from City ORDER by  Name DESC;