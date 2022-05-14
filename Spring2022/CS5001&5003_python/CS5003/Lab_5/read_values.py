"""
    CS5003 Spring 2022
    Lab #5
    02/16/2022
    Jason(Haozhe) Zhang
"""


def read_values():
    my_list = []
    is_done = False
    while(not is_done):
        x = int(input("Enter a number: "))
        if(x > 0):
            my_list.append(x)
        else:
            is_done = True
    return my_list
