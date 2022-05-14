"""
    CS5003 Spring 2022
    Lab #4
    02/16/2022
    Jason(Haozhe) Zhang / Juan Yu
"""


def read_word():
    is_stop = False
    string = ''

    while not is_stop:
        word = str(input("Enter a word: \n"))
        if word != 'stop':
            string += word + ' '
        else:
            is_stop = True
            print(string)


def main():
    read_word()


if __name__ == '__main__':
    main()
