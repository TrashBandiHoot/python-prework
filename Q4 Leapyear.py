# QUESTION 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).


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


