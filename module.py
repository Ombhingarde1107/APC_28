##1. Create a Python module calculator.py containing functions for addition, subtraction,
##multiplication, and division. Create another program that imports the module and
##performs calculations based on user input.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))

if b != 0:
    print("Division:", calculator.divide(a, b))
else:
    print("Division not possible"S)

##2. Create a module student.py containing functions to calculate total marks, percentage, and
##grade. Import the module into another Python program and generate a student's result.

##3. Create a module number_utils.py containing functions to check whether a number is
##prime, palindrome, Armstrong, or perfect. Import the required functions into a main
##program.

##4. Create a module string_utils.py containing functions to count vowels, reverse a string,
##check palindrome, count words, and remove spaces.

##5. Create a module containing functions to calculate gross salary, deductions, and net salary
##for an employee.

##6. Create a module containing recursive functions for factorial, Fibonacci series, sum of
##digits, and binary conversion. Import and use these functions from another program.

##7. Create a package named mathutils containing:
##a) basic.py – arithmetic operations
##b) number.py – prime, Armstrong, palindrome functions
##c) statistics.py – mean, maximum, minimum
##Create a main program that imports functions from each module.

##8. Create a package student containing:
##a) marks.py – total and percentage
##b) grade.py – grade calculation
##c) attendance.py – attendance eligibility
##Write a main program that uses all three modules to generate a student report.

9. Develop a package banking containing:
a) account.py – account creation and balance
b) transaction.py – deposit and withdrawal
c) loan.py – loan calculation
Create a main program to use the package.
10. Create a package texttools containing:
a) cleaning.py – remove punctuation and extra spaces
b) tokenization.py – tokenize text
c) frequency.py – word-frequency analysis
