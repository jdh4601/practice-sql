import csv

id_list = ['user1', 'user2', 'user3']


def get_id():
    user_id = input("Enter id: ")
    return user_id


def get_pw():
    user_pw = input("Enter password: ")
    return user_pw


def check_id(user_id):
    again = True

    while again:
        if user_id in id_list or user_id == '':
            print("Try again!")
        else:
            again = False
            checked_id = True
            return checked_id


def check_pw(user_pw):
    score = 0
    if len(user_pw) >= 8:
        score += 1
    if 대문자 포함:
        score += 1
    if 소문자 포함:
        score += 1
    if 숫자 포함:
        score += 1
    if 특수문자 포함:
        score += 1

    return score


def display_pw_message(score):
    if score < 3:
        print("This password could not be")
    elif score >= 3 and score < 5:
        print("This password could be improved")
    elif score == 5:
        print("This password is strong")
        is_strong = True
        return is_strong


# csv 파일 끝에 id,pw 추가하는 함수
def add_to_csv(user_data):
    file = open("users.csv", "a")
    new_record = user_data
    file.write(new_record)
    file.close()


def change_pw():
    # 비밀번호 변경 -> 리스트 이용하기
    # csv 파일에 저장
    return


def display_all_user_data():
    file = open("users.csv", "r")
    for row in file:
        print(row)
    file.close()


def main():
    print("----------< menu >----------")
    print("1) Create a new user")
    print("2) Change a password")
    print("3) Display all user ids")
    print("4) Quit")
    print("")
    selection = input("Enter a selection: ")

    try_again = True

    while try_again:
        if selection == "1":
            user_id = get_id()  # id 받아옴
            checked_id = check_id(user_id)  # id 유효성 검사
            if checked_id:  # 올바른 id일때?
                user_pw = get_pw()  # pw 받아옴
                score = check_pw(user_pw)  # pw 유효성 검사
                is_strong = display_pw_message(
                    score)  # 점수에 따른 메시지 표시
                if is_strong:  # 확실히 강력 pw?
                    add_to_csv(user_id, user_pw)  # csv 파일에 추가

        elif selection == "2":
            if user_id in id_list:
                change_pw()

        elif selection == "3":
            display_all_user_data()

        elif selection == "4":
            try_again = False


main()
