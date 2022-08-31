# QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for x in range(1, 100):
        if x % 2 == 1:
            print(x)
    

first_odds()