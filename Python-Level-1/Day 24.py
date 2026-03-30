📦 Day 24 – Python Packages

🚀 What I Learned Today

Today I learned about Packages in Python, which help organize code in a structured way and make large projects manageable.

---

📌 What is a Package?

A Package in Python is a directory (folder) that contains multiple Python modules (files).

👉 In simple terms:

- Module = Single ".py" file
- Package = Collection of modules

---

📂 Structure of a Package

mypackage/
   __init__.py
   module1.py
   module2.py

- "__init__.py" makes Python treat the folder as a package
- It can be empty

---

🔁 Module vs Package

Feature| Module| Package
Definition| Single Python file| Folder of modules
Extension| .py| Directory
Usage| Small programs| Large projects

---

📥 Importing Packages

Method 1

import mypackage.module1

Method 2

from mypackage import module1

Method 3

from mypackage.module1 import function_name

---

🧪 Example

Folder Structure

calc/
   __init__.py
   add.py

add.py

def add(a, b):
    return a + b

main.py

from calc.add import add

print(add(2, 3))

👉 Output:

5

---

📦 Built-in Packages

Python provides many built-in packages:

- "math"
- "random"
- "datetime"

Example:

import math
print(math.sqrt(16))

---

🎯 Why Use Packages?

✅ Better code organization
✅ Easy to manage large projects
✅ Code reusability
✅ Helpful in team projects

---

🧠 Key Points

- Package = Folder + "__init__.py"
- Contains multiple modules
- Uses dot (".") notation for import
- Important for real-world applications

---

📌 Conclusion

Packages are essential in Python for organizing code and building scalable applications. Understanding packages is important for both development and interviews.

---

✨ Consistency is the key to success. Keep learning!
