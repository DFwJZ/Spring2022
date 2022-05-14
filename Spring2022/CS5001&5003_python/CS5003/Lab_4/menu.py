"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def menu():
    zero = '0 -- Quit\n'
    one = '1 -- Add "O"\n'
    two = '2 -- Add "oo"\n'
    three = '3 -- Add "xXx"'
    prompt = zero + one + two + three

    string = ''
    while True:
        print(prompt)
        num = input("Option: ")
        if (num == '0'):
            break
        elif (num == '1'):
            string += 'O'
        elif (num == '2'):
            string += 'oo'
        elif (num == '3'):
            string += 'xXx'
        else:
            print("Invalid option")
    print("Result:", string)


def main():
    menu()


if __name__ == '__main__':
    main()
