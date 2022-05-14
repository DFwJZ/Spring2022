
"""
    CS5001-5003 Summer 2022
    Utilities to assist with user input checking before try/except introduced.
    Intended for temporary use during 5001 midterm and while loop module.
    Students should import using "from number_checks import *"
    Mark L. Miller, Ph.D.
"""


def float_ok(str1):
    """ Determines if it is safe to convert a string, str1, to a float. """
    try:
        float(str1)
        return True
    except ValueError:
        return False


def int_ok(str1):
    """ Determines if it is safe to convert a string, str1, to an int. """
    try:
        int(str1)
        return True
    except ValueError:
        return False


def main():
    """ main() provides a few trial 'tests' to verify expected behavior. """
    print(f"float_ok('3.14') returns {float_ok('3.14')}, expected True")
    print(f"float_ok('42') returns {float_ok('42')}, expected True")
    print(f"float_ok('+3.14') returns {float_ok('+3.14')}, expected True")
    print(f"float_ok('-3.14') returns {float_ok('-3.14') }, expected True")
    print()
    print(f"float_ok('Three') returns {float_ok('Three')}, expected False")
    print(f"float_ok('3.14.15') returns {float_ok('3.14.15')}, expected False")
    print(f"float_ok('3-14') returns {float_ok('3-14')}, expected False")
    print(f"float_ok('True') returns {float_ok('True')}, expected False")
    print()
    print(f"int_ok('42') returns {int_ok('42')}, expected True")
    print(f"int_ok('+3') returns {int_ok('+3')}, expected True")
    print(f"int_ok('-3') returns {int_ok('-3') }, expected True")
    print(f"int_ok('999') returns {int_ok('999') }, expected True")
    print()
    print(f"int_ok('3.14') returns {int_ok('3.14')}, expected False")
    print(f"int_ok('Three') returns {int_ok('Three')}, expected False")
    print(f"int_ok('3.14.15') returns {int_ok('3.14.15')}, expected False")
    print(f"int_ok('True') returns {int_ok('True')}, expected False")


if __name__ == '__main__':
    main()
