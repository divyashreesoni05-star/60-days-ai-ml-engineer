📘 Python OOP Concepts

🚀 Day 20 - Learning Journey

Today, I learned the basics of Object-Oriented Programming (OOP) in Python.

---

📌 Topics Covered

1. Classes & Objects

- A class is a blueprint for creating objects
- An object is an instance of a class

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Divya")
print(s1.name)

---

2. Four Pillars of OOP

🔹 Encapsulation

- Wrapping data and methods into a single unit (class)

class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

---

🔹 Abstraction

- Hiding internal implementation and showing only essential details

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

---

🔹 Inheritance

- One class can inherit properties of another class

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

---

🔹 Polymorphism

- Same function name, different behavior

def add(a, b):
    return a + b

print(add(2, 3))
print(add("Hello ", "World"))

---

💡 Key Learnings

- OOP helps in writing clean and reusable code
- Makes code more structured and modular
- Useful for real-world problem solving

---

🔥 Conclusion

Today was a productive day learning OOP concepts in Python.
I will continue practicing and building projects using these concepts.

---

📌 Tags

"Python" "OOP" "Learning" "Beginner" "Coding Journey"
