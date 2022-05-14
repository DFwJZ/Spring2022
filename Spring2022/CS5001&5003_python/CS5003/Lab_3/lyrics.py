"""
    CS5003 Spring 2022
    Lab 3
    Jason(haozhe) Zhang / Hui Hu
"""


def verse(string, animal, sound):

    x = string.replace('cow', animal).replace('moo', sound)

    return x


def main():
    a = "Old MacDonald had a farm, ee-igh, ee-igh, oh!\n"
    b = "And on that farm he had a cow, ee-igh, ee-igh, oh!\n"
    c = "With a moo, moo here and a moo, moo there.\n"
    d = "Here a moo, there a moo, everywhere a moo, moo.\n"
    e = "Old MacDonald had a farm, ee-igh, ee-igh, oh!\n"
    string = a + b + c + d + e

    print(string)
    print(verse(string, 'pig', 'oink'))
    print(verse(string, 'duck', 'quack'))
    print(verse(string, 'sheep', 'bah'))
    print(verse(string, 'horse', 'neigh'))


if __name__ == "__main__":
    main()
