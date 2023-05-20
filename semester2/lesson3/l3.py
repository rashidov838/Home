import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rxb508',
    database='Table_of_employees'
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE Table_of_employees")
# mycursor.execute("""CREATE TABLE IF NOT EXISTS info_about_employees(
#     employee_id INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(255) NOT NULL,
#     Surname CHAR(10) NOT NULL,
#     Gender ENUM('F','M') NOT NULL,
#     Age INT NOT NULL,
#     Salary FLOAT NOT NULL,
#     Work BOOLEAN NOT NULL,
#     Tax DECIMAL(65,30),
#     Start_work DATE,
#     End_work TIMESTAMP
# )""")
# key="INSERT INTO info_about_employees(Name,Surname,Gender,Age,Salary,Work,Tax,Start_work,End_work) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val=[('Bekzod','Rashidovaa','M',20,200000.3694,True,456.159,'2002-10-01','2023-10-09 12:48:00'
# ),
# (
#     'Komilov',"Sanjarovaa",'F',48,520000.3694,False,258.159,'1985-05-21','2023-10-09 12:48:00'
# )]
# mycursor.executemany(key,val)
# mydb.commit()

mycursor.execute("""
    SELECT * FROM info_about_employees;
""")
result=mycursor.fetchall()
for x in result:
    print(x)
# ---------------------------------------------------------------------------------------------------------------------------------------
# mycursor.execute("UPDATE info_about_employees SET Name='Samira' where employee_id=2")
# mydb.commit()
# ---------------------------------------------------------------------------------------------------------------------------------------
# mycursor.execute("""
#     DELETE FROM info_about_employees WHERE Name='Samira';
# """)
# mydb.commit()
# ---------------------------------------------------------------------------------------------------------------------------------------
# mycursor.execute("DELETE FROM info_about_employees WHERE employee_id=3 LIMIT 1")
# mydb.commit()
# ---------------------------------------------------------------------------------------------------------------------------------------
# mycursor.execute("DELETE FROM info_about_employees WHERE employee_id!=6")
# mydb.commit()