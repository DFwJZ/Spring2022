"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def average_grades(x):
    try:
        f = open(x, 'r')
        line = f.read()
        line = line.split('\n')
        count, total = 0, 0
        for i in range(len(line)):
            count += 1
            total += float(line[i])
        return total / count
    except FileNotFoundError:
        print(f"File {x} was not found")
    except PermissionError:
        print(f"Permission denied for {x}")
    except ValueError:
        print(f"Error occurred while reading {x}")
        return 0.0
