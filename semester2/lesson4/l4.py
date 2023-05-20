import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rxb508',
    database='TABLE_USERS'
)
mycursor=mydb.cursor()
mycursor.execute("""
    CREATE DATABASE TABLE_USERS
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS info_about_users(
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        Name   VARCHAR(255) NOT NULL,
        Surname   VARCHAR(255) NOT NULL,
        Score INT NOT NULL
    )
""")
key="INSERT INTO info_about_users(Name,Surname,Score) VALUES(%s,%s,%s) "
val=[('Bekzod','Rashidov',6),
    ('KOMIL','Vohidova',4),
    ('SHAX','Dos',10),
    ('LOLA','Kolikova',8)

]
mycursor.executemany(key,val)
mydb.commit()
mycursor.execute("DROP TABLE info_about_products ")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        Name   VARCHAR(255) NOT NULL
    
    )
# """)
key='INSERT INTO products(Name) VALUE(%s)'
val=[('Meat',),
    ('Kola',),
    ('Sok',),
    ('Pepsi',)
]
mycursor.executemany(key,val)

mydb.commit()



mycursor.execute("""
    SELECT *  FROM info_about_users LEFT JOIN products ON products.product_id=info_about_users.score;
""")
result=mycursor.fetchall()
for x in result:
    print(x)