# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='rxb508',
#     database='Prospects'
# )
# mycursor=mydb.cursor()
# # mycursor.execute("""
# #     CREATE DATABASE Prospects  
# # """)
# # mycursor.execute("""
# #     CREATE TABLE IF NOT EXISTS Prospects(
# #         id INT AUTO_INCREMENT PRIMARY KEY,
# #         name VARCHAR(255) NOT NULL,
# #         address_number INT NOT NULL,
# #         address_street VARCHAR(255) NOT NULL,
# #         phone_number INT NOT NULL
 
# #     )
# # """)
# key="INSERT INTO Prospects(name,address_number,address_street,phone_number) VALUES(%s,%s,%s,%s)"
# val=[('Bekzod',3889,'Chilanzar',1234),
# ('Komil',5688,'Kokand',1759),
# ('Badir',1289,'Fergana',1524)]
# mycursor.executemany(key,val)
# mydb.commit()
# # ----------------------------------------------------------------
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS Employees(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         department VARCHAR(255) NOT NULL,
#         phone_number INT NOT NULL

#         )
# """)
# key="INSERT INTO Employees(name,department,phone_number) VALUES(%s,%s,%s)"
# val=[('Salih','HR',7700),
#     ('Rashid','Accounting',7868),
#     ('Doni','Tourism',9968)
#     ]
# mycursor.executemany(key,val)
# mydb.commit()

# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS ProspectEmployee(
#         prospect_id INT,
#         employee_id INT,
#         FOREIGN KEY(prospect_id) REFERENCES Prospects(id),
#         FOREIGN KEY(employee_id) REFERENCES Employees(id)
         
#     )
# """)

# key='INSERT INTO ProspectEmployee(prospect_id,employee_id) VALUES(%s,%s)'
# val=[(1,1),
# (3,3),
# (2,2)]
# mycursor.executemany(key,val)
# mydb.commit()

# mycursor.execute("""
#     SELECT * FROM Prospects LEFT JOIN Employees ON Prospects.phone_number=Employees.DEPARTMENT;
# """)
# result=mycursor.fetchall()
# for x in result:
#     print(x)

# mycursor.execute("""
#     select * from ProspectEmployee;
# """)
# result=mycursor.fetchall()
# for x in result:
#     print(x)
# ------------------------------------------------------------
# mycursor.execute("""
#     CREATE TABLE Customer(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         address_number INT NOT NULL,
#         address_street VARCHAR(255) NOT NULL,
#         phone_number INT NOT NULL

#     )
# """)
# key='INSERT INTO Customer(name,address_number,add  ress_street,phone_number) VALUES(%s,%s,%s,%s)'
# val=[('Shaxri',9999,'Pekin',6666),
#     ('Lalimi',2131,'Pekin',7777),
#     ('Moxri',5379,'Pekin',9999)
    
#     ]
# mycursor.executemany(key,val)
# mydb.commit()
# mycursor.execute("""
#     CREATE TABLE CustomerEmployee(
#         customer_id INT,
#         employee_id INT,
#         FOREIGN  KEY(customer_id) REFERENCES Customer(id),
#         FOREIGN KEY(employee_id) REFERENCES Employees(id)
#     )
# """)