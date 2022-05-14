"""
    CS5003 Spring 2022
    01/26/2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    10.Three-letter months
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa
"""


def main():
    month = input("Enter month: ")
    # determine the number of days
    if month == "Jan" or "January" or "1":
        days = 31
    elif month == "Feb" or "February" or "2":
        days = 28
    elif month == "Mar" or "March" or "3":
        days = 31
    elif month == "Apr" or "April" or "4":
        days = 30
    elif month == "May" or "May" or "5":
        days = 31
    elif month == "Jun" or "June" or "6":
        days = 30
    elif month == "Jul" or "July" or "7":
        days = 31
    elif month == "Aug" or "August" or "8":
        days = 31
    elif month == "Sep" or "September" or "9":
        days = 30
    elif month == "Oct" or "October" or "10":
        days = 31
    elif month == "Nov" or "November" or "11":
        days = 30
    elif month == "Dec" or "December" or "12":
        days = 31
    else:
        days = "Unknown"
    print(month, "has", days, "days")


if __name__ == '__main__':
    main()
