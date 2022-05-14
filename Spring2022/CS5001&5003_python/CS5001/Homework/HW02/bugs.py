"""
    CS5001 Spring 2022
    Assignment HW # 2
    Jason(Haozhe) Zhang
"""


def bug1():
    #The function is interrupted due to the undefined
    #variable is assigned to another variable.
    a = 'abc'
    b = 123
    c = avc
    print(a)
    print(b)
    print(c)

def bug2():
    #List out of range. The indice starts at 0 for created
    #list. Only two elements exist in the list.
    a = [1, 3]
    print(a[2])
          
def bug3():
    #variable is referenced before assignment.
    print(x)
    x = 5

def bug4():
    #Unsupported perand types. Vairable type mismatch,
    #cannot concatenate a string to a integer.
    a = 1
    b = 'ad'
    print(a + b)

def main():
   bug1()
   bug2()
   bug3()
   bug4()


if __name__ == '__main__':
    main()
