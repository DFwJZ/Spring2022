"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""
import json
from hw6 import *


l1 = [{'a': 'able'}, {'b': 'baker'}, "Ignore", {'b': 'bravo'}, {'b': 'bravodsad'}]
l3 = [[[[[[[[[[[[{'j': 'jason'}]]]]]]], {'j': 'jasmine'}]]], {'j': 'jurassic'}]]
l5 = [{'a': 'alpha', 'b': 'bravo'}, [[{'c': 'charlie'}],
      [{'e': 'echo'}]], {'d': 'delta'}]

dict1 = flatten_to_dict(l1)
dict3 = flatten_to_dict(l3)
dict5 = flatten_to_dict(l5)


def main():
    try:
        with open('hw6_output.txt', "x") as outfile:
            json.dump(dict1, outfile)
        with open('hw6_output1.txt', "x") as outfile:
            json.dump(dict3, outfile)
        with open('hw6_output2.txt', "x") as outfile:
            json.dump(dict5, outfile)
    except OSError:
        print(False, end=': ')
        print(OSError)
        return False
    except KeyError:
        print(False, end=': ')
        print(KeyError)
        return False
    except TypeError:
        print(False, end=': ')
        print(TypeError)
        return False
    print("True")
    return True


if __name__ == '__main__':
    main()
