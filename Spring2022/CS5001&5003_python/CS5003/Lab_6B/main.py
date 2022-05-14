"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


filenames = ["formula", "factorial", "upper_triangle",
             "lower_triangle", "sum_values", "to_squares",
             "find_max", "find_value", "in_english",
             "choose", "try123"]
for file in filenames:
    globals()[file] = __import__(file)


def main():
    # print(formula.formula(5))
    # print(factorial.factorial(5))
    # upper_triangle.upper_triangle(5)
    # lower_triangle.lower_triangle(5)
    # print(sum_values.sum_values([1,2,3,4,5,6,6], 5))
    # print(to_squares.to_squares([1,-2,3,-4,5,-6,7,-8,9], 0))
    # print(to_squares.to_squares([-99], 0))
    # print(find_max.find_max([1,3,65,8]))
    # print(find_value.find_value([1,2,4,5,6,7,8,8], 9))
    # print(in_english.in_english(7))
    # print(in_english.in_english(59))
    # print(in_english.in_english(6341297850))
    print(choose.choose(2, 6)) #15

    print(choose.choose(8, 20)) #125970




if __name__ == '__main__':
    main()
