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