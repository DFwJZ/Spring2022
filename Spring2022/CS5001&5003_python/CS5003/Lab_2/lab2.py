"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""

def main():
    A1 = "T" if (False and False) or not False else "F"
    B1 = "T" if not(False and (False or not False)) else "F"

    
    print("|---+---+---+---+---|")
    print("| p + q + r + A + B |")
    print("| F + F + F +" , A1, "+",B1,  "|")
    print("| F + F + F +   +   |")
    print("| F + F + F +   +   |")
    print("| F + F + F +   +   |")
    print("| T + F + F +   +   |")
    print("| T + F + F +   +   |")
    print("| T + F + F +   +   |")
    print("| T + F + F +   +   |")
    print("|---+---+---+---+---|")
    

if __name__ == '__main__':
    main()
