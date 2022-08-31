
#! Figure out if else statement is necessary. Will it return False without it? or would it be null/void/none and is that funionally the same.


def is_leap_year(a_year):
    if a_year % 100 and a_year % 400 == 0:
        print("leapyear")
        return True
    elif a_year % 4 == 0:
        print("leapyear")
        return True
    else:
        print("Not a leapyear")
        return False


year = int(input("Please enter a year: "))
is_leap_year(a_year=year)


