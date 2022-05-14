"""
    CS5003 Spring 2022
    Assignment HW # 2
    Jason(Haozhe) Zhang
"""


def is_leap_year(x):
    #step 1
    if(x % 4 == 0):
        #step 2
        if(x % 100 == 0):
            #step 3
            if(x % 400 == 0):
                #step 4
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():

###a = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032,2036, 2040, 2044, 2048, 2050, 2089]
    
###    for item in a:
###        print(is_leap_year(item))      


    year_of_input = int(input("Please enter a year greater than 2000: \n"))

    if(is_leap_year(year_of_input) == True):
        print("The year",year_of_input,"is a leap year")
    else:
        print("The year",year_of_input,"is not a leap year")


if __name__ == '__main__':
    main()
