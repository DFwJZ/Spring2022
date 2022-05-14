"""
    CS5002 Spring 2022
    Homework 7
    Hui Hu
"""

def find_numbers(S, n, x, y):
    low = min(S[0], S[-1])
    high = max(S[0], S[-1])

    if x <= low and high <= y:
        return n

    elif y < low or x > high:
        return 0
    else:
        mid = (n-1) // 2
        return find_numbers(S[:mid+1], mid+1, x, y) + find_numbers(S[mid+1:],n-mid-1, x, y)


def main():
    S1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    S2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print("S1 =", S1)
    print("S2 =", S2, "\n")

    # undefines range (x > y)
    test(S1, 3, 2, 0)
    test(S2, 3, 2, 0)
    print()

    # test x < y < low
    test(S1, -2, -1, 0)
    test(S2, -2, -1, 0)
    print()

    # test high < x < y
    test(S1, 10, 12, 0)
    test(S2, 10, 12, 0)
    print()

    # test x < low < y < high
    test(S1, -1, 5, 5)
    test(S2, -1, 5, 5)
    print()

    # test low <= x < y <= high
    test(S1, 2, 8, 7)
    test(S1, 5.1, 5.2, 0)
    test(S2, 2, 8, 7)
    test(S2, 5.1, 5.2, 0)
    print()

    # test x <= high < y
    test(S1, 7, 12, 3)
    test(S2, 7, 12, 3)
    print()

    # test x < low < high < y
    test(S1, -1, 12, 9)
    test(S2, -1, 12, 9)
    print()


def test(S, x, y, expect):
    if S[0] < S[-1]:
        print(f"test: [x,y]=[{x}, {y}], S=S1", end="\t")
    else:
        print(f"test: [x,y]=[{x}, {y}], S=S2", end="\t")
    print("expect:", expect, end="\t")
    print("actual:", find_numbers(S, len(S), x, y))

 
if __name__ == '__main__':
    main()    
