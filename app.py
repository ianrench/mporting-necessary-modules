# Importing necessary modules
import random  # 'import' keyword
from datetime import datetime  # 'from' keyword

# Class definition using 'class'
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self' is used to refer to the instance
        self.age = age

    # 'def' keyword to define a method
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # 'yield' is used in a generator function
    def birthday(self):
        while True:
            yield f"Happy birthday, {self.name}! You are now {self.age + 1} years old!"
            self.age += 1

# Function using 'def', 'if', 'elif', 'else', 'try', 'except', 'raise'
def check_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative!")  # 'raise' keyword
        elif age < 18:
            return "You are a minor."
        elif age >= 18 and age < 60:
            return "You are an adult."
        else:
            return "You are a senior citizen."
    except ValueError as e:  # 'except' and 'as' keywords
        return f"Error: {e}"

# Lambda function using 'lambda' and 'return'
square = lambda x: x ** 2  # 'lambda' keyword for anonymous function

# 'global' keyword to define a global variable
global_counter = 0

def increment_counter():
    global global_counter  # 'global' keyword to modify global variable
    global_counter += 1
    return global_counter

# 'nonlocal' keyword example
def outer_function():
    outer_var = 10
    def inner_function():
        nonlocal outer_var  # 'nonlocal' keyword
        outer_var += 5
        return outer_var
    return inner_function()

# 'with' keyword for handling resources (file handling)
def write_to_file():
    with open("output.txt", "w") as file:  # 'with' keyword
        file.write("Python keywords demonstration.\n")
        file.write(f"Global counter value: {global_counter}\n")

# 'for' and 'in' keywords for looping
def print_numbers(n):
    for i in range(n):  # 'for' and 'in' keywords
        print(i, end=" ")

# 'while' keyword for a loop
def countdown(start):
    while start > 0:  # 'while' keyword
        print(start)
        start -= 1
    else:
        print("Countdown finished.")

# 'assert' keyword for debugging
def assert_check(value):
    assert value >= 0, "Value cannot be negative!"  # 'assert' keyword
    print(f"Value is: {value}")

# 'continue' and 'break' in a loop
def loop_example():
    for i in range(10):
        if i == 3:
            continue  # 'continue' keyword
        if i == 7:
            break  # 'break' keyword
        print(i, end=" ")

# Main program to use the functions above
def main():
    print("Program Started")

    # 'and', 'or', 'not' for logical operators
    if (True and False):  # 'and' keyword
        print("This will never print.")
    if not False:  # 'not' keyword
        print("This will print because 'not False' is True.")
    if True or False:  # 'or' keyword
        print("This will also print.")

    # Creating an object of the Person class
    person = Person("Alice", 25)
    person.introduce()

    # Testing the check_age function
    age_status = check_age(17)
    print(age_status)

    # Using lambda function to square a number
    print(f"Square of 4 is: {square(4)}")

    # Testing global and nonlocal keywords
    incremented_value = increment_counter()
    print(f"Global counter after increment: {incremented_value}")
    print(f"Value from outer function: {outer_function()}")

    # Writing to a file
    write_to_file()

    # Testing loops and assertions
    print_numbers(5)
    countdown(5)
    assert_check(10)
    loop_example()

    print("Program Ended")

# Using 'if _name_ == "_main_":' to execute the main function
if _name_ == "_main_":  # 'if' keyword
    main()