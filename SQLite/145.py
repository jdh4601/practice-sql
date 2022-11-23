from tkinter import *
import sqlite3


def add_data():
    # 입력값 가져옴 -> 튜플
    new_name = name_txtbox.get()
    new_grade = int(grade_txtbox.get())
    score_tup = (new_name, new_grade)
    print(score_tup + "\n")

    # SQL 데이터 베이스에 입력값을 저장
    cursor.execute(
        """INSERT INTO TestScores (sname, grade) VALUES (?, ?)""", score_tup)

    # 데이터 베이스의 모든 데이터 출력
    cursor.execute("SELECT * FROM TestScores")
    for x in cursor.fetchall():
        print(x)

    db.commit()
    name_txtbox.delete(0, END)
    grade_txtbox.delete(0, END)
    name_txtbox.focus()


def clear_data():
    name_txtbox.delete(0, END)
    grade_txtbox.delete(0, END)
    name_txtbox.focus()


with sqlite3.connect("score.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS TestScores(
  id integer PRIMARY KEY,
  sname text,
  grade integer);""")


window = Tk()
window.title("Student Scores")
window.geometry("500x400")
# 이름 입력칸
name_label = Label(text="Enter student's name: ")
name_label.place(x=30, y=20)

name_txtbox = Entry(text="")
name_txtbox.place(x=200, y=20, width=100, height=20)
name_txtbox["fg"] = "white"
name_txtbox["justify"] = "center"
name_txtbox.focus()
# 성적 입력칸
grade_label = Label(text="Enter student's grade: ")
grade_label.place(x=30, y=50)

grade_txtbox = Entry(text="")
grade_txtbox.place(x=200, y=50, width=100, height=20)
grade_txtbox["justify"] = "center"
grade_txtbox["fg"] = "white"
# 추가 버튼
add_btn = Button(text="Add", command=add_data)
add_btn.place(x=140, y=100, width=80, height=30)
# 삭제 버튼
clear_btn = Button(text="Clear", command=clear_data)
clear_btn.place(x=250, y=100, width=80, height=30)

window.mainloop()
db.close()
