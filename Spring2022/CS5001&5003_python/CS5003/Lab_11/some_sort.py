from itertools import count


def some_sort(my_list):
    counter = 0
    swapped = True
    counter += 1
    while swapped is True:
        counter += 1
        swapped = False
        counter += 1
        for i in range(0, len(my_list) - 1):
            print(f"i = {i}", end=' ')
            if my_list[i] > my_list[i + 1]: # conditional statement count ++
                counter += 1
                # print(f"swapping {my_list[i]} with {my_list[i + 1]}")
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                counter += 3
                swapped = True
                counter += 1
        counter += 1
        print(f"for loop complete, count + 1")
    print(f"counttotal: {counter}")

def main():
    ls = [5,4,3,2,1]
    ls2 = [1,2,3,4,5]
    some_sort(ls)
    # some_sort(ls2)




main()