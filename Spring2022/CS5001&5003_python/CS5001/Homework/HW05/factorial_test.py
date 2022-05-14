"""
    CS5001 Spring 2022
    Assignment HW 05
    Jason(Haozhe) Zhang
"""

# import all base factorial calculating functions from fact.py
import fact


def fact_while_test(n, expected) -> bool:
    x = fact.fact_while(n)
    if x == expected:
        return True
    return False


def fact_for_test(n, expected) -> bool:
    x = fact.fact_for(n)
    if x == expected:
        return True
    return False


def fact_rec_test(n, expected) -> bool:
    x = fact.fact_for(n)
    if x == expected:
        return True
    return False


def main():
    counter = 0
    success_counter = 0
    my_list = [-1, 0, 1, 2, 3, 4, 5, 10]
    expected = [1, 1, 1, 2, 6, 24, 120, 3628800]
    for i in range(len(my_list)):
        counter += 1
        x = fact.fact_while(my_list[i])
        y = False
        if fact_while_test(my_list[i], expected[i]):
            success_counter += 1
            y = True
        if y:
            print(f"fact_while[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- Passed")
        else:
            print(f"fact_while[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- failed")
    print(f"Result fact_while:  {success_counter} passed, {counter - success_counter} failed. \n")

    counter = 0
    success_counter = 0
    for i in range(len(my_list)):
        counter += 1
        x = fact.fact_for(my_list[i])
        y = False
        if fact_for_test(my_list[i], expected[i]):
            success_counter += 1
            y = True
        if y:
            print(f"fact_for[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- Passed")
        else:
            print(f"fact_for[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- failed")
    print(f"Result fact_for:  {success_counter} passed, {counter - success_counter} failed. \n")

    counter = 0
    success_counter = 0
    for i in range(len(my_list)):
        counter += 1
        x = fact.fact_rec(my_list[i])
        y = False
        if fact_rec_test(my_list[i], expected[i]):
            success_counter += 1
            y = True
        if y:
            print(f"fact_rec[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- Passed")
        else:
            print(f"fact_rec[{my_list[i]}]  expected: {expected[i]}  actual: {x} -- failed")
    print(f"Result fact_rec:  {success_counter} passed, {counter - success_counter} failed. \n")


if __name__ == '__main__':
    main()
