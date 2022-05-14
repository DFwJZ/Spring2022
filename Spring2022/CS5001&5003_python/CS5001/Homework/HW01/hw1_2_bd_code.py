"""
    CS5001 Spring 2022
    Assignment: hw01
    Name:Jason(Haozhe Zhang)
"""


def main():
    current_year = 2022

    user_name = input("Welcome! What is your name: \n")

    print("Hi, " + user_name)

    age = input("How old are you?\n")

    user_age = int(age)

    user_birth = current_year - user_age

    print("Your were born in ", user_birth, '.', sep='')


if __name__ == "__main__":
    main()
