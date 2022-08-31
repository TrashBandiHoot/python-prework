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