📘 Python Lists – Complete Notes

🔹 Introduction

Python me List ek built-in data structure hai jo multiple values ko ek single variable me store karne ke liye use hota hai.

Ordered collection hoti hai

Mutable (change ho sakti hai)

Different data types store kar sakti hai


my_list = [1, 2, 3, "hello", 4.5]


---

🔹 Creating a List

# Empty list
list1 = []

# With elements
list2 = [10, 20, 30]

# Mixed data types
list3 = [1, "Python", 3.5]


---

🔹 Accessing Elements

my_list = [10, 20, 30, 40]

print(my_list[0])   # 10
print(my_list[2])   # 30
print(my_list[-1])  # 40


---

🔹 Updating Elements

my_list[1] = 100
print(my_list)


---

🔹 List Functions / Methods

1. append()

Element ko end me add karta hai

my_list.append(50)

2. insert()

Specific index par element add karta hai

my_list.insert(1, 200)

3. remove()

Value ko remove karta hai

my_list.remove(20)

4. pop()

Index ke through element remove karta hai

my_list.pop(0)

5. clear()

List ko empty karta hai

my_list.clear()


---

🔹 Other Useful Functions

Length

len(my_list)

Sort

my_list.sort()

Reverse

my_list.reverse()


---

🔹 Looping Through List

for item in my_list:
    print(item)


---

🔹 List Slicing

my_list = [1, 2, 3, 4, 5]

print(my_list[1:4])  # [2, 3, 4]
print(my_list[:3])   # [1, 2, 3]
print(my_list[2:])   # [3, 4, 5]


---

🔹 List Comprehension (Important)

squares = [x*x for x in range(5)]
print(squares)


---

🔹 Nested List

matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # 2


---

🔹 Example Program

numbers = [5, 2, 9, 1]

numbers.append(7)
numbers.sort()

for num in numbers:
    print(num)


---

🔹 Advantages of List

Easy to use

Flexible data structure

Dynamic size



---

🔹 Conclusion

Python list ek powerful aur flexible data structure hai jo real-world programming me bahut use hota hai. Data ko store, update aur process karne ke liye list bahut important concept hai.


---

🚀 Practice Questions

1. List me se duplicate elements remove karo


2. List ko reverse karo


3. Largest element find karo


4. Even numbers print karo


5. Do lists ko merge karo




---

💡 Tip: Roz practice karoge to list aur strong ho jayegi 👍
