# colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# def writeTofile(text):
#     with open(text+ '.txt','w') as file:
#         file.write(text)
# for color in colors:
#     writeTofile(color)
# writeTofile("FSPR-4-22")

# try:
#     file=open("semester2\lesson2\doc.txt",'r')
#     print(file.read())
# except:
#     print('Cannot read file')
# finally:
#     file.close()

# name='Bek'
# try:
#     if len(name)<8:
#         print('Welcome ' + name)
# except NameError

import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='rxb508'
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("Create database Fisrtbase")