"""
    CS5003 Spring 2022
    Assignment: HW06
    Jason(Haozhe) Zhang
"""


def flatten_to_dict(lst):
    # if lst is not a list, raise a TypeError
    if not isinstance(lst, list):
        raise TypeError
    my_dict = {}
    for i in range(len(lst)):
        # if the element inside the lst is a dictionary, add it to my_dict
        if isinstance(lst[i], dict):
            for k, v in lst[i].items():
                # if not found key, add the key and its value to my_dict
                if k not in my_dict:
                    my_dict[k] = v
                # if one duplicate key with different a value are found,
                # add the value to the existing key to make a list of values.
                # if duplicate keys with multiple different values ( > 1),
                # append the different value(s) to the existing value list.
                else:
                    if isinstance(my_dict[k], list):
                        my_dict[k].append(v)
                    else:
                        my_dict[k] = [my_dict[k], v]
        # if the element in lst is a nested list,
        # calling flatten_to_dict() recursively until a list is found,
        # and attach the items in the nested list to the outer list
        elif isinstance(lst[i], list):
            my_dict.update(flatten_to_dict(lst[i]))
    return my_dict


def main():
    l1 = [{'a': 'alpha', 'b': 'bravo'}, [[{'c': 'charlie'}],
          [{'e': 'echo'}]], {'d': 'delta'}]
    l2 = [1, ('a' 'b'), {'c': 'charlie'}]
    l3 = [{'a': 'able'}, {'b': 'baker'}, "Ignore", {'b': 'bravo'}, {'b': 'bravodsad'}]
    l4 = [3.14]
    l5 = [[[[[[[[[[[[{'j': 'jason'}]]]]]]], {'j': 'jasmine'}]]], {'j': 'jurassic'}]]
    l6 = [{'CS5001': 'HW06'}]

    dict1 = flatten_to_dict(l1)
    dict2 = flatten_to_dict(l2)
    dict3 = flatten_to_dict(l3)
    dict4 = flatten_to_dict(l4)
    dict5 = flatten_to_dict(l5)
    dict6 = flatten_to_dict(l6)


if __name__ == '__main__':
    main()
