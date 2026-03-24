# OOP Basics in Python

# Creating a class
class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
s1 = Student("Divya", 21)
s2 = Student("Rahul", 22)

# Calling method
s1.display()
print("------")
s2.display()
