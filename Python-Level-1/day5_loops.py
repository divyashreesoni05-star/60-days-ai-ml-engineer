# Day 5 - Python Loops
# Learning: for loop, while loop, do-while loop concept

# -------------------------
# 1. For Loop
# -------------------------

print("For Loop Example")

for i in range(1, 6):
    print("Number:", i)


# -------------------------
# 2. While Loop
# -------------------------

print("\nWhile Loop Example")

i = 1

while i <= 5:
    print("Value:", i)
    i += 1


# -------------------------
# 3. Do-While Loop (Concept)
# Python me direct do-while loop nahi hota
# Isko while True se simulate karte hain

print("\nDo While Loop Example")

i = 1

while True:
    print("Count:", i)
    i += 1

    if i > 5:
        break


# -------------------------
# 4. Simple Program using Loop
# Print table of a number
# -------------------------

print("\nMultiplication Table")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
