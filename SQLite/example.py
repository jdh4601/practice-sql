import sqlite3
# 데이터 파일 생성 후 db에 데이터 연결
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
# Names라는 테이블 생성 -> 필드, 데이터 타입, 기본키 지정
cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
  id integer PRIMARY KEY,
  firstname text,
  surname text,
  phonenumber text); """)

# 데이터 생성 후 Names 테이블에 삽입
# cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#                VALUES("5", "Simon", "Howels", "01223 324434")""")
# db.commit()

# newID = int(input("enter ID name: "))
# newfirst = input("enter firstname: ")
# newSur = input("enter surname: ")
# newPhone = input("enter phonenumber: ")

# # 입력값을 받아서 insert추가
# cursor.execute("""INSERT INTO Names (id, firstname, surname, phonenumber)
#                VALUES(?,?,?,?)""", (newID, newfirst, newSur, newPhone))
# db.commit()

# # 테이블의 모든 데이터 한번에 출력
# cursor.execute("SELECT * FROM Names")
# print(cursor.fetchall())

cursor.execute("SELECT * FROM Names ORDER BY firstname")
for i in cursor.fetchall():
    print(i)

# 테이블에서 id가 1인 행row 삭제
# cursor.execute("DELETE Names WHERE id=12")

# 가장 마지막에 db를 닫아준다
db.close()
