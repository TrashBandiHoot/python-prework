
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