"""
    CS5003 Spring 2022
    Assignment Lab 8 Module 11
    Jason(Haozhe) Zhang and Manu Singh and Yuan wang
"""


def get_key_string(x):
    print(type(x.keys()))
    ret_list = []
    ret_string = ""
    for key in x:
        ret_list.append(str(key))
    for key in ret_list:
        ret_string += key + "\n"
    ret_string = ret_string[:-1]
    return ret_string  
