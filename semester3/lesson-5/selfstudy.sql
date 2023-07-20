<?xml version="1.0" encoding="UTF-8"?><sqlb_project><db path="C:/Users/WINDOWS 10/Documents/Githome/semester3/lesson3/database/quizdata.db" readonly="0" foreign_keys="1" case_sensitive_like="0" temp_store="0" wal_autocheckpoint="1000" synchronous="2"/><attached/><window><main_tabs open="structure query browser pragmas" current="1"/></window><tab_structure><column_width id="0" width="300"/><column_width id="1" width="0"/><column_width id="2" width="110"/><column_width id="3" width="2023"/><column_width id="4" width="0"/><expanded_item id="0" parent="1"/><expanded_item id="1" parent="1"/><expanded_item id="2" parent="1"/><expanded_item id="3" parent="1"/></tab_structure><tab_browse><current_table name="4,6:mainpeople"/><default_encoding codec=""/><browse_table_settings><table schema="main" name="people" show_row_id="0" encoding="" plot_x_axis="" unlock_view_pk="_rowid_"><sort/><column_widths><column index="1" value="88"/><column index="2" value="90"/><column index="3" value="90"/><column index="4" value="122"/><column index="5" value="91"/><column index="6" value="103"/><column index="7" value="95"/><column index="9" value="81"/><column index="10" value="45"/><column index="11" value="251"/></column_widths><filter_values/><conditional_formats/><row_id_formats/><display_formats/><hidden_columns/><plot_y_axes/><global_filter/></table></browse_table_settings></tab_browse><tab_sql><sql name="SQL 1">-- SELECT sum(first_name) from people;

-- SELECT sum(age) from people;

-- SELECT avg(age) from people;

-- SELECT avg(quiz_points) from people where company is NULL;

-- SELECT min(age) from people;

-- SELECT max(age) from people;

-- SELECT max(first_name) from people;L

-- SELECT first_name,round(age,2) as 'Средний возраст' from people WHERE age BETWEEN 30 and 40
--  from  people;



-- SELECT city ,state_code,avg(age) from people WHERE city like 'B%' GROUP By 1  ORDER by 1 LIMIT 10 ;


-- SELECT city ,state_code,avg(age) from people WHERE city like 'B%' GROUP By 1 HAVING state_code like 'C%' ORDER by 1 LIMIT 10 ;


SELECT city,upper(state_code) , avg(age) as 'Avg_age' from people WHERE city like 'B%' GROUP By 1 HAVING sum(quiz_points)&gt;33 ORDER by age  limit 10;</sql><current_tab id="0"/></tab_sql></sqlb_project>
