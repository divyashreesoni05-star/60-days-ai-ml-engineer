Python Learning Journey – Day 8

📅 Topics: Strings and For Loop in Python

Today I learned about Strings and For Loop in Python.

---

🔹 Strings in Python

A String is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

Example

name = "Divya"
print(name)

Output

Divya

---

🔹 String Operations

1️⃣ Length of a String

The "len()" function is used to find the length of a string.

text = "Hello"
print(len(text))

Output

5

---

2️⃣ String Indexing

Indexing is used to access characters of a string.

word = "Python"

print(word[0])  
print(word[1])  
print(word[2])  

Output

P
y
t

---

3️⃣ String Concatenation

Concatenation means joining two strings.

first = "Hello"
second = "World"

print(first + " " + second)

Output

Hello World

---

4️⃣ String Methods

Uppercase

text = "python"
print(text.upper())

Capitalize

text = "python"
print(text.capitalize())

Replace

text = "python"
print(text.replace("p", "j"))

---

🔹 For Loop in Python

A for loop is used to repeat a block of code multiple times.

Example

for i in range(5):
    print(i)

Output

0
1
2
3
4

---

🔹 For Loop with String

We can also use a for loop to iterate through characters of a string.

name = "Python"

for letter in name:
    print(letter)

Output

P
y
t
h
o
n

---

🔹 For Loop Example

Print numbers from 1 to 5

for i in range(1,6):
    print(i)

Output

1
2
3
4
5

---

🧠 Practice Questions

Question 1

Write a Python program to print the length of a string.

text = "Programming"
print(len(text))

---

Question 2

Write a program to print each character of a string using a for loop.

word = "Python"

for i in word:
    print(i)

---

Question 3

Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

---

🎯 What I Learned Today

- What is a String
- Length of String
- String Indexing
- String Methods
- For Loop
- For Loop with String

---

💻 This is part of my Python learning journey and daily coding practice.
