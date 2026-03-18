📘 Day 13: Python Lists + Tuples (Complete Notes)


---

🔹 Revision: Python List

What is a List?

Ordered collection

Mutable (change ho sakti hai)

Different data types store kar sakti hai


my_list = [1, 2, 3, "hello", 4.5]


---

🔹 Important List Methods

my_list.append(10)
my_list.insert(1, 100)
my_list.remove(2)
my_list.pop()
my_list.sort()
my_list.reverse()


---

🔹 List Comprehension

squares = [x*x for x in range(5)]


---

🔹 What is a Tuple?

Tuple bhi list jaisa hota hai but:

Immutable hota hai (change nahi kar sakte)

Faster than list

Parentheses () use hota hai


t = (1, 2, 3, "hello")


---

🔹 Accessing Tuple Elements

print(t[0])
print(t[-1])


---

🔹 Tuple Methods

t = (1, 2, 2, 3)

print(t.count(2))
print(t.index(3))


---

🔹 List vs Tuple

Feature	List	Tuple

Mutable	Yes	No
Syntax	[]	()
Speed	Slower	Faster



---

🔹 Practice Questions (List)

1. Reverse List

lst = [1,2,3,4]
lst.reverse()
print(lst)

2. Find Largest Element

lst = [10, 20, 5, 40]
print(max(lst))

3. Remove Duplicates

lst = [1,2,2,3,4,4]
lst = list(set(lst))
print(lst)

4. Even Numbers

lst = [1,2,3,4,5,6]
for i in lst:
    if i % 2 == 0:
        print(i)

5. Merge Two Lists

a = [1,2]
b = [3,4]
print(a + b)


---

🔹 Practice Questions (Tuple)

1. Convert List to Tuple

lst = [1,2,3]
t = tuple(lst)

2. Count Elements

t = (1,2,2,3)
print(t.count(2))

3. Find Index

print(t.index(3))


---

🔹 Example Program

numbers = [5, 2, 9, 1]
numbers.append(7)
numbers.sort()

for num in numbers:
    print(num)

# tuple example

t = (10, 20, 30)
print(t[1])




---

🚀 Day 13 Completed ✅

💡 Kal se aur advanced topics + coding practice start karo 👍
