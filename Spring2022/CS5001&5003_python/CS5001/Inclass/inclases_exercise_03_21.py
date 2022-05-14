#
#Inclass notes for mar 21
#


def r_fact(n):
    if n < 2:
        return 1
    else:
        return n * r_fact(n - 1)



def main():
    
    return r_fact(5)


if __name__ == '__main__':
    main()

