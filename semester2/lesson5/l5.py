import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rxb508',
    database='CRM'
)
mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE CRM")
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS Campaign(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(40),
#         objective VARCHAR(40),
#         sponsor VARCHAR(40),
#         start_date DATE,
#         end_date DATE,
#         other_details VARCHAR(40)
#     )
# """)
# key='INSERT INTO Campaign(name,objective,sponsor,start_date,end_date,other_details) VALUES(%s,%s,%s,%s,%s,%s)'
# val=[('Bekzod','Goodboy','Usmonov','2003-03-15','2008-09-25','Music'),
#     ('Sabina','Welldone','Husband','2006-08-11','2023-07-15','Dance'),
#     ('Doni','Goodboy','Usmonov','2003-03-15','2008-09-25','Music'),
#     ('Sancho','Welldone','Wife','2006-08-11','2023-07-15','Dance')
 # ]
# mycursor.executemany(key,val)
# mydb.commit()
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS Leads(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         firstname VARCHAR(40),
#         surname VARCHAR(40),
#         other_details VARCHAR(40)
#     )
# """)
# key='INSERT INTO Leads(firstname,surname,other_details) VALUES(%s,%s,%s)'
# val=[('Bekzod','Rashidov','Music'),
#     ('Sabina','Husbandova','Dance'),
#     ('Doni','Usmonov','Music'),
#     ('Sancho','Komilov','Dance')
# ]
# mycursor.executemany(key,val)
# mydb.commit()
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS CampaignMember(
#         Campaign_id INT,
#         Leads_id INT,
#         PRIMARY KEY(Campaign_id,Leads_id),
#         FOREIGN KEY(Campaign_id) REFERENCES Campaign(id),
#         FOREIGN KEY(Leads_id) REFERENCES Leads(id)
#     )
# """)
# key='INSERT INTO CampaignMember(Campaign_id,Leads_id) VALUES(%s,%s)'
# val=[(1,2),
# (3,2),
# (2,1)
# ]
# mycursor.executemany(key,val)
# mydb.commit()

# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS Account(
#         id INT,
#         name VARCHAR(40),

#     )
# """)
