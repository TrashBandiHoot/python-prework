
#! QUESTION 1

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


#! QUESTION 2

def first_odds():
    for x in range(1, 100):
        if x % 2 == 1:
            print(x)
    return

first_odds()


#! QUESTION 3


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


#! QUESTION 4

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


#! QUESTION 5

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
list3 = [1, 3, 5, 7, 9]


#! This doesn't work, remember to save your work and stop doing homework when you are sleep deprived.

def is_consectutive(a_list):
    check_ascending = a_list[0]
    check_descending = a_list[0]
    for x in a_list:
        if x == check_ascending:
            check_ascending += 1
            # print("works")
            order = "ascending"
        if x == check_descending:
            check_descending -= 1
            # print("works")
            order = "descending"
        else:
            return "This list is not consecutive"
            
    return order



print(is_consectutive(list2))