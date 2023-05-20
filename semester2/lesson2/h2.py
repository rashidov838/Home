# import mysql.connector
# try:
#     connection=mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='rxb508',
#         database='fisrtbase'
#     )
    
#     # mysql_table="""
#     # Create TABLE Laptop(
#     #     id int(11) NOT NULL,
#     #     Name VARCHAR(250) NOT NULL,
#     #     Price float NOT NULL,
#     #     Purchase_date DATE NOT NULL,
#     #     PRIMARY KEY(ID)
#     # )
#     # """
#     mycursor=connection.cursor()
#     # result=cursor.execute(mysql_table)
#     # print("Laptop Table was created succesfully")
#     mycursor.execute("SELECT * FROM Laptop")
#     result=mycursor.fetchall()
#     for x in result:
#         print(x)

# except mysql.connector.Error as error:
#     print("Failed to create Table in Mysql: {}".format(error))
# finally:
#     if connection.is_connected():
#         mycursor.close()
#         connection.close()
#         print("Mysql connection is closed")


# Ex_1_________________________________________________________________________________________________
# import mysql.connector
# mydb=mysql.connector.connect(
#     host="localhost",
#     user='root',
#     password='rxb508'
# )
# print(mydb)
# mycursor=mydb.cursor()
# # # mycursor.execute("CREATE DATABASE Laptop")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     list_mydatabase=[]
#     list_mydatabase.append(*x)
#     print(list_mydatabase)
# for i in list_mydatabase:
#     check_database=input("Check your database: ")
#     if check_database == i:
#         print('True')
#     else:
#         print("False")

# Ex_2_________________________________________________________________________________________________
# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='rxb508',
#     database='Laptop'
# )
# # print(mydb)
# mycursor=mydb.cursor()
# # mycursor.execute("""
# #     CREATE TABLE information(
# #         Laptop_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         Name VARCHAR(255) NOT NULL,
# #         Adress VARCHAR(255) NOT NULL,
# #         Price DECIMAL(12,2) NOT NULL,
# #         Owner VARCHAR(255) NOT NULL
# #     )
# # """)
# # ------------------------------------------------------------------------------------------------------------------------
# # mycursor.execute("""
# #     ALTER TABLE information ADD COLUMN  username_id INT AUTO_INCREMENT PRIMARY KEY
# # """)    
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)


import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="rxb508",
    database="SOFA"
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE SOFA")
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS info(
#         Sofa_id INT AUTO_INCREMENT PRIMARY KEY, 
#         Name VARCHAR(255) NOT NULL,
#         Adress VARCHAR(255) NOT NULL,
#         Price DECIMAL(12,2) NOT NULL,
#         Owner VARCHAR(255) NOT NULL
#     )
# """)
# ----------------------------------------------------------------------------------------------------------------------------
# mycursor.execute("INSERT INTO info(Name,Adress,Price,Owner) VALUES(%s,%s,%s,%s)",('Chair','Nirabad city',100,'Bekzod'))
# mycursor.execute("INSERT INTO info(Name,Adress,Price,Owner) VALUES(%s,%s,%s,%s)",('Mono','Olmazar city',26.45,'Xusan'))
# mycursor.execute("""
#     SELECT * FROM sofa.info
# """)
# result=mycursor.fetchall()
# for x in result:
#     print(x)
# mydb.commit()
# ----------------------------------------------------------------------------------------------------------------------------
# key="INSERT INTO info(Name,Adress,Price,Owner) VALUES(%s,%s,%s,%s)"
# val=[('Kola','Olmazar city',26.45,'xcvbm'),
#     ('Pepsi','Tashkent city',212.45,'Poiuyt'),
#     ('Fanta','China city',2632.45,'TYUI'),
#     ('Simo','Kokand city',456.45,'ASDFG'), 
#     ('Lipo','S1amarkand city',926.45,'ERTY'),
#     ('Rolla','Fergana city',8826.45,'Moioa')]
# mycursor.executemany(key,val)
# mydb.commit()
# mycursor.execute(""" 
#     SELECT sofa_id, Name, Price FROM sofa.info where adress = 'China city' 
# """)
# --------------------------------------------------------------------------------------------------
# mycursor.execute("""
#     select * from info where adress LIKE '%Fergana%'
# """)
# result=mycursor.fetchall()
# for x in result:
#     print(x)
# ------------------------------------------------------------------------------------------------------
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="rxb508",
    database="Table_students"
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE Table_students")
# mycursor.execute("""CREATE TABLE IF NOT EXISTS info_about_students(
#     student_id  INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(255) NOT NULL,
#     Surname VARCHAR(255) NOT NULL,
#     Gender VARCHAR(50) NOT NULL,
#     Type TINYINT(1) NOT NULL,
#     Address VARCHAR(255) NOT NULL,
#     Email VARCHAR(255) NOT NULL,
#     Number INT 
# )""")
# key="INSERT INTO info_about_students(Name,Surname,Gender,Type,Address,Email,Number) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# val=[("Bekzod","Rashidov",'M',0,"Yunusabad district",'bekzod73@gmail.com',9921),
#     ("Sher","Ganiev",'M',1,"Olma district",'qwertyu903@gmail.com',9789)
#     ]
# mycursor.executemany(key,val)
# mydb.commit()
mycursor.execute("""
    select * from info_about_students
""")
result=mycursor.fetchall()
for x in result:
    print(x)
# print(mycursor.rowcount)
# mycursor.execute("""
#     ALTER TABLE info_about_students DROP COLUMN birthday;
# """)
# ---------------------------------------
# mycursor.execute("""
#     ALTER TABLE info_about_students ADD COLUMN birthday datetime;
# """)
# mydb.commit()
# ------------------------------------------
# mycursor.execute("""
#     UPDATE info_about_students SET birthday = '2000-09-11 10:00:00' WHERE student_id=2;
# """) 
# mydb.commit()
