# Python Revision - Day 19
# Topics Covered: Strings, Loops, Conditions, Multi Printing

print("Day 19 Revision Started 🚀")

# 1. Multi Printing Problem
a = input("Enter string: ")
n = int(input("Enter number: "))

print("Output:")
print(a * n)   # Main Logic

# 2. String Reverse
s = input("Enter a string to reverse: ")
print("Reversed:", s[::-1])

# 3. Count Vowels
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total vowels:", count)

# 4. Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5. Factorial
n = int(input("Enter number for factorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial:", fact)

# 6. Pattern Printing
print("Pattern:")
for i in range(1, 6):
    print("*" * i)

print("Day 19 Completed ✅")
