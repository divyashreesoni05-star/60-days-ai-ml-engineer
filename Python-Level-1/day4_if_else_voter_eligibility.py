
# Day 4 - Python If Else Statements
# Author: Divyashree Soni

# ---------------------------------
# What I Learned Today
# ---------------------------------
# 1. If statement
# 2. If-Else statement
# 3. If-Elif-Else statement
# 4. Decision making in Python
# 5. Voter Eligibility Program

# ---------------------------------
# 1. Simple If Example
# ---------------------------------

num = 10

if num > 5:
    print("Number is greater than 5")


# ---------------------------------
# 2. If-Else Example (Even or Odd)
# ---------------------------------

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ---------------------------------
# 3. If-Elif-Else Example (Grade Checker)
# ---------------------------------

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# ---------------------------------
# Project: Voter Eligibility Checker
# ---------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ---------------------------------
# Day 4 Progress
# ---------------------------------
# ✔ Learned If, Else, Elif
# ✔ Built Voter Eligibility Program
