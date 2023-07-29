import sqlite3
import pprint
connection=sqlite3.connect("hotel_booking.db")
cursor=connection.cursor()



# 1
# print(cursor.execute("select * from booking_summary").fetchall())

# 2
# pprint.pprint(cursor.execute("select * from booking_summary ").fetchmany(10))

# 3
# bra=cursor.execute("select country from booking_summary where country = 'BRA'").fetchall()
# print(bra)

# 4
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS bra_cutomers(
#         num integer,
#         hotel text,
#         is_cancelled integer,
#         lead_time integer,
#         arrival_date_year integer ,
#         arrival_date_month text,
#         arrival_date_day_of_month integer,
#         adults integer,
#         children integer,
#         country text,
#         adr real,
#         special_requests integer
#     )

# """)

# 5
# bra=cursor.execute("select * from booking_summary where country = 'BRA'").fetchall()
# cursor.executemany("""INSERT INTO bra_cutomers VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",bra)
# 6
# pprint.pprint(cursor.execute("select avg(lead_time) from booking_summary where is_cancelled = 1").fetchall())
# 7
# pprint.pprint(cursor.execute("select avg(lead_time) from booking_summary where is_cancelled = 0").fetchall())
# 8
# pprint.pprint(cursor.execute("select sum(special_requests) from booking_summary where is_cancelled=0").fetchall())
# 9
# pprint.pprint(cursor.execute("select sum(special_requests) from booking_summary where is_cancelled=1").fetchall())
connection.commit()
connection.close()








# connection=sqlite3.connect("new_db.db")
# cursor=connection.cursor()



# cursor.execute("""
#     CREATE TABLE if not exists toys(
#         id integer,
#         name text,
#         price REAL

#     )


# """)


# new_toys = [
#     (1, "Shadow", 32),
#     (2, "Miko", 10),
#     (3, "Ork", 21),
#     (4, "Batman", 21),
#     (5, "Spiderman", 21),
# ]

# cursor.executemany("""INSERT INTO toys VALUES(?,?,?)""",new_toys)
# print(cursor.execute("select * from toys").fetchone())
# print(cursor.execute("select * from toys").fetchall())
# print(cursor.execute("select * from toys").fetchmany(2))


# connection.commit()
# connection.close()


