"""
    CS5003 Spring 2022
    01/26/2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    9.Truth
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():
    print("+---+---+---+---+---+")
    print("| p | q | r | A | B |")
    print("+---+---+---+---+---+")

    for p in range(0, 2):
        for q in range(0, 2):
            for r in range(0, 2):
                # s1, s2, s3 are set to True
                s1 = bool(str(p) == "1")
                s2 = bool(str(q) == "1")
                s3 = bool(str(r) == "1")
                print("|", ("T" if s1 else "F"),
                      "|", ("T" if s2 else "F"),
                      "|", ("T" if s3 else "F"),
                      "|", ("T" if (s1 and s2) or not s3 else "F"),
                      "|", ("T" if not (s1 and (s2 or not s3)) else "F"),
                      "|")
                print("+---+---+---+---+---+")


if __name__ == '__main__':
    main()
