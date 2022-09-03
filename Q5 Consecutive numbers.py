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