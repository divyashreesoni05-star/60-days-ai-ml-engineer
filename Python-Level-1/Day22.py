Day 22 - OOPs Four Pillars (Java/Python)

📅 Date:

28 March 2026

📚 Topic Covered:

- Object-Oriented Programming (OOP)
- Four Pillars of OOP

---

🚀 What I Learned Today

Today, I learned about the Four Pillars of Object-Oriented Programming (OOP):

1. Encapsulation

- Wrapping data (variables) and methods into a single unit (class).
- Helps in data hiding.
- Achieved using private variables and public getters/setters.

👉 Example:

class Student:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):
        return self.__name

---

2. Abstraction

- Hiding complex implementation details and showing only essential features.
- Improves code clarity and reduces complexity.

👉 Example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

---

3. Inheritance

- One class acquires properties and methods of another class.
- Promotes code reusability.

👉 Example:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

---

4. Polymorphism

- Same function name behaves differently in different situations.
- Can be achieved using method overriding or overloading.

👉 Example:

class Bird:
    def sound(self):
        print("Bird makes sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

---

💻 Practice Done

- Practiced basic problems based on OOP concepts
- Implemented classes and objects
- Applied inheritance and polymorphism

---

🎯 Key Takeaways

- OOP helps in writing clean and reusable code
- Four pillars are the foundation of OOP
- Understanding these concepts is important for placements

---

🔥 Next Plan

- Practice more OOP problems
- Start Data Structures basics
- Improve problem-solving skills

---

📌 Status:

✅ Completed

---
