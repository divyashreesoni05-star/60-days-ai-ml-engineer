# Day 6 - Python Functions
# Author: Divya Shree Soni

# ---------------------------------
# 1. Simple Function
# ---------------------------------
def greet():
    print("Hello Divya, welcome to Python Functions!")

greet()


# ---------------------------------
# 2. Function with Parameter
# ---------------------------------
def greet_user(name):
    print("Hello", name)

greet_user("Divya")


# ---------------------------------
# 3. Function with Return Value
# ---------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Addition Result:", result)


# ---------------------------------
# 4. Function with Default Parameter
# ---------------------------------
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Divya")


# ---------------------------------
# 5. Function to Find Square of Number
# ---------------------------------
def square(num):
    return num * num

number = int(input("Enter a number: "))
print("Square is:", square(number))


# ---------------------------------
# 6. Function to Check Even or Odd
# ---------------------------------
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check_even_odd(7)


# ---------------------------------
# 7. Function to Find Maximum Number
# ---------------------------------
def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum number is:", find_max(10, 20))
