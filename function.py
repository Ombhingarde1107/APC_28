# 1.Write a function factorial(n) that accepts an integer and returns its factorial.
# def factorial(a):
#     fact = 1
#     for i in range(1, a + 1):
#         fact = fact * i
#         return fact
#     a = int(input("Enter number: "))
# print("factorial =", factorial(a))

#2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# n = int(input("Enter number: "))
# print(check_even_odd(n))

# 3.Define a function that accepts two numbers and returns the greater number.
# def greater(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Greater =", greater(a, b))

# 4.	Create a function simple_interest(p, r, t) to calculate simple interest.

# def simple_interest(p, r, t):
#     si = (p * r * t) / 100
#     return si
# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# print("Simple Interest =", simple_interest(p, r, t))

#5.	Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
# def isprime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
        # if n % i == 0:
#             return False
#     return True
# n = int(input("Enter number: "))
# print(isprime(n))


#6.	Define a function to calculate the area of a circle using its radius.
# def area_of_circle(radius):
#     pi = 3.14159
#     area = pi * radius ** 2
#     return area
# radius = float(input("Enter radius: "))
# print("Area of Circle =", area_of_circle(radius))

#7.Write a function that accepts n and returns the sum of the first n natural numbers.
# def sum_of_natural_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# total = int(input("Enter a number: "))
# print("Sum of first", total, "natural numbers =", sum_of_natural_numbers(total))

#8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.
# def power(base, exponent):
#     return base ** exponent
# base = int(input("Enter base: "))
# exponent = int(input("Enter exponent: "))
# print("Answer =", power(base, exponent))

#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
# def largest(numbers):
#     big = numbers[0]
#     for n in numbers:
#         if n > big:
#             big = n

#     return big
# numbers = [10, 25, 5, 40, 15]
# print("Largest =", largest(numbers))

#10.	Define a function that accepts a string and returns the number of vowels present in it.
# def count_vowels(string):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# string = input("Enter a string: ")
# print("Number of vowels =", count_vowels(string))

#11.	Write a function that accepts a string and returns the reverse of the string.
# def reverse_string(s):
#     return s[::-1]


# s = input("Enter string: ")

# print("Reverse =", reverse_string(s))

#12.	Create a function that checks whether a given string or number is a palindrome.

# def palindrome(value):
#     value = str(value)

#     if value == value[::-1]:
#         return True
#     else:
#         return False


# value = input("Enter string or number: ")

# print(palindrome(value))

# 13.	Write a function that accepts a list of numbers and returns their average.
# def average(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n

#     return total / len(numbers)
# numbers = [10, 20, 30, 40, 50]
# print("Average =", average(numbers))

#14.	Define a function that accepts a list and an element and returns the number of times that element occurs.
# def count_element(numbers, element):
#     count = 0

#     for n in numbers:
#         if n == element:
#             count = count + 1

#     return count


# numbers = [1, 2, 2, 3, 2, 4]
# element = int(input("Enter element: "))
# print("Occurrences =", count_element(numbers, element))

# 33.
# square = lambda x: x * x
# n = int(input("Enter number: "))
# print("Square =", square(n))

# 34
# cube = lambda n: n ** 3

# n = int(input("Enter a number: "))

# print("Cube =", cube(n))

# 35
# maximum = lambda a, b: a if a > b else b

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Maximum =", maximum(a, b))


# 36
# simple_interest = lambda p, r, t: (p * r * t) / 100

# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))

# print("Simple Interest =", simple_interest(p, r, t))

# 37
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))

print("Numbers =", numbers)
print("Squares =", squares)

# 38numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda n: n ** 3, numbers))

print("Numbers =", numbers)
print("Cubes =", cubes)