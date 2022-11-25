alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def get_data():
    word = input("Enter your message: ")  # apple
    word = word.lower()
    num = int(input("Enter your number: "))  # 2
    # 알파벳 이외의 것을 입력했을 때
    if num > 26 or num == 0:
        while num > 26 or num == 0:
            num = int(input("Out of range, please enter a number again: "))
    # 데이터를 리턴해야 할 때는 변경되면 안되므로 tuple을 이용하기
    data = (word, num)  # (apple, 2)
    return data


def make_code(word, num):
    new_word = ""

    for i in word:
        index = alphabet.index(i)
        index += num
        if index >= 27:
            index -= 27
        char = alphabet[index]
        new_word = new_word + char

    print(new_word)  # bcd


def decode(word, num):  # bcd, 1
    new_word = ""
    for i in word:
        index = alphabet.index(i)
        index -= num
        if index < 0:
            index += 27

        char = alphabet[index]
        new_word = new_word + char


def main():
    try_again = True
    while try_again:
        print("------------< Menu >------------\n")
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit \n")
        print("---------------------------------")
        answer = input("Enter your selection: ")

        if answer == "1":
            (word, num) = get_data()
            make_code(word, num)
        elif answer == "2":
            (word, num) = get_data()
            decode(word, num)
        elif answer == "3":
            try_again = False
        else:
            print("Please try to select correct answer.")
