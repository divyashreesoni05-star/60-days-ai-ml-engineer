# Day 7 - Python Functions Practice

# 1. Function to add two numbers
def add(a, b):
    return a + b

print("Addition:", add(5, 3))


# 2. Function to find square of a number
def square(n):
    return n * n

print("Square:", square(4))


# 3. Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", check_even_odd(7))


# 4. Function to find largest number
def largest(a, b, c):
    return max(a, b, c)

print("Largest number:", largest(10, 25, 15))


# 5. Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))
