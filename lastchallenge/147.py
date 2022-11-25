import random

colors = ['red', 'blue', 'yellow', 'pink', 'green', 'black', 'white']


def select_random_color():
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    col3 = random.choice(colors)
    col4 = random.choice(colors)

    random_colors = [col1, col2, col3, col4]
    print(random_colors)

    random_idx = [colors.index(col1), colors.index(
        col2), colors.index(col3), colors.index(col4)]
    return random_idx


def select_user_color():
    for i in colors:
        print(f'{colors.index(i)} : {i}')
    print("\n Please select your 4 colors")

    select1 = int(input("Enter first color index: "))
    select2 = int(input("Enter second color index: "))
    select3 = int(input("Enter third color index: "))
    select4 = int(input("Enter fourth color index: "))

    user_colors = [colors[select1], colors[select2],
                   colors[select3], colors[select4]]
    print(f"You selected {user_colors}")

    user_idx = [select1, select2, select3, select4]
    return user_idx


def check(random_idx, user_idx):
    right_place_num = 0
    wrong_place_num = 0

    for i in random_idx:
        for j in user_idx:
            if colors[j] == colors[j]:
                wrong_place_num += 1
                if i == j:
                    right_place_num += 1

    print(f"Correct color but in the wrong place: {wrong_place_num}")
    print(f"Correct color in the correct place: {right_place_num}")


def main():
    random_idx = select_random_color()
    user_idx = select_user_color()
    check(random_idx, user_idx)


main()
