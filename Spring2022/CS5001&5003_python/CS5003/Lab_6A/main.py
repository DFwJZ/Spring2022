"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


filenames = ["multiples", "count_down", "count_vowels",
             "average", "count_negatives", "add_ten",
             "filter_evens", "compare_lists", "positional_elements",
             "count_words"]
for file in filenames:
    globals()[file] = __import__(file)


def main():
    # add_ten.add_ten([])
    # print(count_vowels.count_vowels("HelloaABIOd"))
    # print(compare_lists.compare_lists([1, 2, 3, 4, 5], [1, 2, 3, 4]))
    # print(compare_lists.compare_lists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    # print(compare_lists.compare_lists([1, 2, 3, 4, 5], [1, 2, 5, 3, 4]))
    # print(add_ten.add_ten([]))
    # print(add_ten.add_ten([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    main()
