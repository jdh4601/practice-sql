import sqlite3

with sqlite3.connect("bookinfo2.db") as db:
    cursor = db.cursor()

# <Authors 데이터>
cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
  Name text PRIMARY KEY,
  place text);""")

# <Books 데이터>
cursor.execute(""" CREATE TABLE IF NOT EXISTS Books(
  id integer PRIMARY KEY,
  title text,
  author text,
  datePublished text
); """)

cursor.execute("SELECT * FROM Books")
for x in cursor.fetchall():
    print(x)

print('')
# 142
print()
location = input("Enter place: ")
print()

cursor.execute(
    """SELECT Books.title, Books.author, Books.datePublished FROM Books, Authors WHERE Authors.Name = Books.author AND Authors.place =? """, [location])
for x in cursor.fetchall():
    print(x)

db.close()

# 143
date = int(input("Enter a published year: "))
print()

cursor.execute(
    """SELECT Books.title, Books.author, Books.datePublished FROM Books WHERE datePublished > ? ORDER BY datePublished""", [date])

for i in cursor.fetchall():
    print(i)


db.close()

# 144
file = open("bookinfo.txt", "w")

author_name = input("Enter author's name: ")
cursor.execute(
    """SELECT * FROM Books WHERE author = ? """, [author_name])

for x in cursor.fetchall():
    new_record = f"{x[0]} - {x[1]} - {x[2]} - {x[3]}\n"
    file.write(new_record)

file = open("bookinfo.txt", "r")
print(file.read())
file.close()
