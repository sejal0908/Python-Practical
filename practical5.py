# Exercise 1 - Handling ZeroDivisionError

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero.")
        return None


numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))

result = safe_divide(numerator, denominator)

if result is not None:
    print("Result:", result)


# Exercise 2 - Handling ValueError

import math

def find_square_root(number1):
    try:
        if number1 <= 0:
            raise ValueError
        return math.sqrt(number1)
    except ValueError:
        print("Invalid input! Please enter a positive integer or a float value.")
        return None


number1 = float(input("Enter a number: "))

result = find_square_root(number1)

if result is not None:
    print("Square root:", result)


# Exercise 3 - Handling Generic Exceptions

def calculate(num):
    try:
        result = num / (num - 5)
        print("Result:", result)
    except Exception as e:
        print("An error occurred during calculation.")


num = float(input("Enter a number: "))

calculate(num)