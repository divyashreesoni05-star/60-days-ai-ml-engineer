# 🚀 Day 17 of 75 Days of Coding

## 📌 Topics Covered:

* Exception Handling in Python
* File Handling in Python

---

## 🧠 What I Learned Today:

### 🔹 Exception Handling

Today I learned how to handle errors in Python so that the program does not crash.

* `try` → used for risky code
* `except` → handles errors
* `else` → runs when no error occurs
* `finally` → always executes
* `raise` → used to create custom errors

I also understood that handling specific exceptions is a good practice.

---

### 🔹 File Handling

I learned how to work with files using Python.

* `open()` function is used to open files

* Different modes:

  * `r` → read
  * `w` → write (overwrites file)
  * `a` → append
  * `r+` → read & write

* `close()` is used to close files

* `with` statement is the best practice as it automatically closes the file

---

## 💻 Practice Code:

```python
# Exception Handling Example
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Success")
finally:
    print("Program Ended")


# File Handling Example
with open("demo.txt", "w") as file:
    file.write("Hello World")

with open("demo.txt", "r") as file:
    print(file.read())
```

---

## 🎯 Key Takeaways:

* Exception handling prevents program crash
* `finally` always runs
* File handling helps in storing data permanently
* `with` statement is safer than manual closing

---

## 🔥 Progress:

Day 17 completed successfully ✅
Learning step by step and building consistency 💪

---

## 📌 Next Plan:

* Practice more problems on Exception Handling
* Work on File Handling questions
* Start small mini project

---

#75DaysOfCode #Python #LearningJourney #Coding #BeginnerToPro 🚀
