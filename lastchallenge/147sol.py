import random


def select_color():
    colors = ['red', 'blue', 'orange', 'yellow', 'pink', 'green', 'white']
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    col3 = random.choice(colors)
    col4 = random.choice(colors)
    data = (col1, col2, col3, col4)
    print(data)
    return data


def check(col1, col2, col3, col4):
    print("colors are : red, blue, orange, yellow, pink, green and white.")
    try_again = True
    # user color 1
    while try_again:
        user_col1 = input("Enter your choice 1: ")
        user_col1 = user_col1.lower()

        if user_col1 != 'red' and user_col1 != 'blue' and user_col1 != 'orange' and user_col1 != 'yellow' and user_col1 != 'pink' and user_col1 != 'green' and user_col1 != 'white':
            print("Incorrect selection")
        else:
            try_again = False
    # user color 2
    try_again = True
    while try_again:
        user_col2 = input("Enter your choice 2: ")
        user_col2 = user_col2.lower()
        if user_col2 != 'red' and user_col2 != 'blue' and user_col2 != 'orange' and user_col2 != 'yellow' and user_col2 != 'pink' and user_col2 != 'green' and user_col2 != 'white':
            print("Incorrect selection")
        else:
            try_again = False
    # user color 3
    try_again = True
    while try_again:
        user_col3 = input("Enter your choice 3: ")
        user_col3 = user_col3.lower()
        if user_col3 != 'red' and user_col3 != 'blue' and user_col3 != 'orange' and user_col3 != 'yellow' and user_col3 != 'pink' and user_col3 != 'green' and user_col3 != 'white':
            print("Incorrect selection")
        else:
            try_again = False
    # user color 4
    try_again = True
    while try_again:
        user_col4 = input("Enter your choice 4: ")
        user_col4 = user_col4.lower()
        if user_col4 != 'red' and user_col4 != 'blue' and user_col4 != 'orange' and user_col4 != 'yellow' and user_col4 != 'pink' and user_col4 != 'green' and user_col4 != 'white':
            print("Incorrect selection")
        else:
            try_again = False

    correct = 0
    wrong_place = 0

    # check color1
    if col1 == user_col1:
        correct += 1
    elif col2 == user_col1 or col3 == user_col1 or col4 == user_col1:
        wrong_place += 1
    # check color2
    if col2 == user_col2:
        correct += 1
    elif col2 == user_col2 or col3 == user_col2 or col4 == user_col2:
        wrong_place += 1
    # ckeck color3
    if col3 == user_col3:
        correct += 1
    elif col1 == user_col3 or col2 == user_col3 or col4 == user_col3:
        wrong_place += 1
    # ckeck color4
    if col4 == user_col4:
        correct += 1
    elif col1 == user_col4 or col2 == user_col4 or col3 == user_col4:
        wrong_place += 1

    print(f"Correct color but in the wrong place: {correct}")
    print(f"Correct color in the correct place: {wrong_place}")

    return (correct, wrong_place)


def main():
    (col1, col2, col3, col4) = select_color()
    score = 0
    play = True
    while play:
        (correct, wrong_place) = check(col1, col2, col3, col4)
        print(correct, wrong_place)
        score += 1
        if correct == 4:
            play = False
    print("You win!")
    print(f"You took {score} times guesses.")


main()
