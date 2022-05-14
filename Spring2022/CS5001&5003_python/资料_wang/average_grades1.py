"""
    CS5001-5003 Spring 2022
    Module 8
    Hui Hu / Xinwan Wang
"""
import re


def average_grades(file):
    try:
        numRegex = re.compile(r'(-)?(\d+.\d+|\d+)')
        with open(file) as content:
            grades = content.readlines()

        sums = 0
        for i in grades:
            num = numRegex.search(i)
            if num:
                sums += float(num.group())
        num = len(grades)
        return sums / num
    except FileNotFoundError:
        print(f"File {file} was not found")
    except PermissionError:
        print("Permission denied for {file}")
    except InterruptedError:
        print("Error occurred while reading {file}")
