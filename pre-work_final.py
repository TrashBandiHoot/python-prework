
# QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

# First thought was to do something like this

"""
user_name = input("What is your name?: ")

def hello_name(user_name):
    print(f"Hello, {user_name}")

hello_name(user_name)
"""

# After thinking about it for a moment I figured this was probably a better solution.

def hello_name(user_name):
    print(f"Hello, {user_name}")

hello_name(input("What is your name?: "))


# QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for x in range(1, 100):
        if x % 2 == 1:
            print(x)
    return

first_odds()


# QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.


nums = [1, 2, 94, 42, 82, 12, 21, 77, 101, 65, -1, 999]

#* With max()

"""
def max_num_in_list(a_list):
    result = max(a_list)
    print(result)

max_num_in_list(nums)
"""

#* Without max()

def max_num_in_list(a_list):
    big_num = 0
    for num in nums:
        if num > big_num:
            big_num = num

    print(big_num)

max_num_in_list(list)


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


# QUESTION 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
list3 = [1, 3, 5, 7, 9]
list4 = [2, 3, 4, 5, 6]

def in_order(a_list):
    """Checks whether the numbers are ascending/descending"""
    if a_list == sorted(a_list) or a_list == sorted(a_list, reverse=True):
        return sorted(a_list)
    else:
        return False


def is_consecutive(ordered_list):
    new_list = []
    index = 0
    int_a = ordered_list[index]
    int_b = ordered_list[index + 1]
    count = 1
    while index < len(ordered_list):
        for num in ordered_list:
            index += 1
            count += 1
            if int_b == int_a + 1:
                new_list.append(num)
    if new_list == ordered_list:
        return True
    else:
        return False
        

print(is_consecutive(in_order(list1)))