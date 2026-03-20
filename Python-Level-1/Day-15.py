# 📅 Day 15: Python Data Structures Revision Program

print("----- LIST -----")
# List
numbers = [5, 2, 8, 1, 3]

# Add element
numbers.append(10)

# Sort list
numbers.sort()

print("List after operations:", numbers)


print("\n----- TUPLE -----")
# Tuple
t = (10, 20, 30, 40)

print("Tuple elements:")
for i in t:
    print(i)

# Access element
print("First element:", t[0])


print("\n----- DICTIONARY -----")
# Dictionary
student = {
    "name": "Divya",
    "age": 21,
    "branch": "IoT"
}

# Access value
print("Name:", student["name"])

# Update value
student["age"] = 22

# Add new key
student["college"] = "MITS"

print("Updated Dictionary:", student)

# Loop through dictionary
print("Dictionary items:")
for key, value in student.items():
    print(key, ":", value)


print("\n----- SET -----")
# Set
s = {1, 2, 3, 3, 4}

print("Set (duplicates removed):", s)

# Add element
s.add(5)

# Remove element
s.remove(2)

print("Updated Set:", s)


print("\n----- COMBINED OUTPUT -----")
print("List:", numbers)
print("Tuple:", t)
print("Dictionary:", student)
print("Set:", s)
