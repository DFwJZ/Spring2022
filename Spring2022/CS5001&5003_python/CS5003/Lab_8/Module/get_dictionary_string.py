"""
    CS5003 Spring 2022
    Assignment Lab 8 Module 11
    Jason(Haozhe) Zhang and Manu Singh and Yuan wang
"""


def get_dictionary_string(x):
    ret_list_keys = []
    ret_list_values = []
    ret_string = ""
    for key in x:
        ret_list_keys.append(str(key))
        ret_list_values.append(str(x[key]))
        print(ret_string)
    for i in range(len(ret_list_keys)):
        ret_string += ret_list_keys[i] + " - " + ret_list_values[i] + "\n"
    ret_string = ret_string[:-1]
    return ret_string
