Day 8 – Python Array Inbuilt Functions
Introduction
Today I learned about Python array (list) inbuilt functions.
These functions help us easily manipulate and manage elements inside an array.
Python arrays are usually implemented using lists, which provide many built-in methods to modify data.
Python Code Example
# Python Array (List) Inbuilt Functions Practice

# Creating an array
arr = [10, 20, 30, 40]

print("Original Array:", arr)

# append() – Add element at the end
arr.append(50)
print("After append:", arr)

# insert() – Insert element at specific position
arr.insert(2, 25)
print("After insert:", arr)

# remove() – Remove specific value
arr.remove(30)
print("After remove:", arr)

# pop() – Remove element using index
arr.pop(1)
print("After pop:", arr)

# sort() – Sort the array
arr.sort()
print("After sort:", arr)

# reverse() – Reverse the array
arr.reverse()
print("After reverse:", arr)

# count() – Count occurrences of a value
print("Count of 40:", arr.count(40))

# index() – Find index of an element
print("Index of 40:", arr.index(40))
Output
Original Array: [10, 20, 30, 40]
After append: [10, 20, 30, 40, 50]
After insert: [10, 20, 25, 30, 40, 50]
After remove: [10, 20, 25, 40, 50]
After pop: [10, 25, 40, 50]
After sort: [10, 25, 40, 50]
After reverse: [50, 40, 25, 10]
Count of 40: 1
Index of 40: 1
Functions Used
Function
Description
append()
Adds an element at the end of the array
insert()
Inserts an element at a specific position
remove()
Removes a specific value
pop()
Removes element using index
sort()
Sorts the array
reverse()
Reverses the array
count()
Counts occurrences of an element
index()
Returns index of an element
Conclusion
Python provides powerful built-in functions for arrays (lists) that make data manipulation easy and efficient.
