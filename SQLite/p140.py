import sqlite3

# connect database
with sqlite3.connect("people.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS People(
  id integer PRIMARY KEY,
  firstname text,
  surname text,
  country text);""")

cursor.execute(
    """INSERT INTO People (id, firstname, surname, country)VALUES("1", "Jayden", "Jung", "Korea")""")
db.commit()

db.close()


def viewpeople():
    cursor.execute("SELECT * FROM People")
    for x in cursor.fetchall():
        print(x)


def addnewpeople():
    new_id = int(input("Enter id: "))
    new_firstname = input("Enter firstname: ")
    new_surname = input("Enter surname: ")
    new_country = input("Enter country: ")

    cursor.execute("""INSERT INTO People(id, firstname, surname, country) VALUES(?, ?, ?, ?)"""), (
        new_id, new_firstname, new_surname, new_country)

    db.commit()


def selectname():
    input_surname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM People WHERE surname=?", [input_surname])
    for x in cursor.fetchall():
        print(x)


def deleteperson():
    input_id = int(input("Enter id: "))
    cursor.execute("DELETE People WHERE id=?", [input_id])
    cursor.execute("SELECT * FROM People")
    for x in cursor.fetchall():
        print(x)
    db.commit()


with sqlite3.connect("people.db") as db:
    cursor = db.cursor()


def main():
    try_again = True

    while try_again:
        print("<Main Menu> \n\n 1) View people list. \n 2) Add to people list. \n 3) Search for surname. \n 4) Delete person from people list. \n 5) Quit this program. \n")
        selection = input("Enter a selection (1~5) : ")

        if selection == "1":
            viewpeople()
        elif selection == "2":
            addnewpeople()
        elif selection == "3":
            selectname()
        elif selection == "4":
            deleteperson()
        elif selection == "5":
            try_again = False
        else:
            print("Please enter a right selection.")


main()
db.close()
