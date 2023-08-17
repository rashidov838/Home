<?xml version="1.0" encoding="UTF-8"?><sqlb_project><db path="C:/Users/WINDOWS 10/Documents/Githome/semester3/lesson3/database/quizdata.db" readonly="0" foreign_keys="1" case_sensitive_like="0" temp_store="0" wal_autocheckpoint="1000" synchronous="2"/><attached/><window><main_tabs open="structure browser query pragmas" current="2"/></window><tab_structure><column_width id="0" width="300"/><column_width id="1" width="0"/><column_width id="2" width="110"/><column_width id="3" width="2023"/><column_width id="4" width="0"/><expanded_item id="0" parent="1"/><expanded_item id="1" parent="1"/><expanded_item id="2" parent="1"/><expanded_item id="3" parent="1"/></tab_structure><tab_browse><current_table name="4,6:mainpeople"/><default_encoding codec=""/><browse_table_settings><table schema="main" name="people" show_row_id="0" encoding="" plot_x_axis="" unlock_view_pk="_rowid_"><sort/><column_widths><column index="1" value="88"/><column index="2" value="90"/><column index="3" value="90"/><column index="4" value="122"/><column index="5" value="91"/><column index="6" value="103"/><column index="7" value="95"/><column index="9" value="81"/><column index="10" value="45"/><column index="11" value="251"/></column_widths><filter_values/><conditional_formats/><row_id_formats/><display_formats/><hidden_columns/><plot_y_axes/><global_filter/></table></browse_table_settings></tab_browse><tab_sql><sql name="SQL 1">-- SELECT  * from people;
-- SELECT first_name 'Имя' from people;
-- SELECT upper(city) Городок FROM people;
-- SELECT DISTINCT state_code from people;
-- SELECT state_code from people;
-- SELECT first_name,last_name ,city,state_code from people where state_code != 'CA' ;

-- SELECT first_name,last_name ,city,state_code from people where state_code &lt;&gt; 'CA' ;


-- SELECT first_name from people WHERE first_name like 'Ja%';

-- SELECT first_name from people WHERE first_name like '%an%';

-- SELECT first_name from people WHERE first_name like '%an';

-- SELECT first_name from people WHERE first_name like '%an%e_';

-- SELECT first_name,company from people WHERE company is NOT NULL;

-- SELECT first_name,quiz_points from people WHERE quiz_points  BETWEEN 50 and 100;


-- SELECT first_name,quiz_points from people WHERE first_name  BETWEEN 'A' and 'K';


-- SELECT first_name,quiz_points from people 
-- WHERE quiz_points &gt;90 and quiz_points &lt;=100

-- WHERE (first_name like 'A%' and last_name like 'W%') and (quiz_points =92 or quiz_points=96)

-- ;
-- SELECT first_name,last_name,city,quiz_points from people WHERE city='Los Angeles' LIMIT 5; 

-- SELECT first_name,last_name,age,
-- CASE 
-- 	WHEN age&gt;40 then 55555
-- 	WHEN age&lt;30 then 'Bye'
-- 	ELSE 'nothing'
-- END as add_info
-- FROM people;



-- SELECT first_name,last_name,quiz_points from people 
-- ORDER by quiz_points DESC;




</sql><current_tab id="0"/></tab_sql></sqlb_project>
