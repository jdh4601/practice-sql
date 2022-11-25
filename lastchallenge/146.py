# shift code
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

# 하나의 함수는 하나의 역할만 하기 -> 데이터 받아오는 함수 분리시켜 재활용하자


def incoding():
    new_message = input("What's your message?: ")  # apple
    num = int(input("Enter a number: "))  # 2

    list_message = list(new_message)  # [a, p, p, l, e]
    incoded_list = list_message[num:] + \
        list_message[:num]  # [p, l, e] + [a, p]
    incoded_message = ''.join(incoded_list).lower()  # [p,l,e,a,p]
    print('')
    print(f'Incoded message is [{incoded_message}].')  # pleap


def decoding():
    incoded_message = input("What's your incoded message?: ")  # pleap
    num = int(input("Enter a number: "))  # 2


def main():
    try_again = True

    while try_again:
        print("------------< Menu >------------\n")
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit \n")
        print("---------------------------------")
        answer = input("Enter your selection between 1 and 3: ")

        if answer == "1":
            incoding()
        elif answer == "2":
            decoding()
        elif answer == "3":
            try_again = False
        else:
            print("Please try to select correct answer.")


main()
