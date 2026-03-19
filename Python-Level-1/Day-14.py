

📘 Day 14: Python Dictionary (Complete Notes)


---

🔹 What is a Dictionary?

Dictionary ek key-value pair data structure hota hai.

Unordered collection

Mutable hota hai

Keys unique hoti hain


dict1 = {
    "name": "Divya",
    "age": 21,
    "branch": "IoT"
}


---

🔹 Accessing Values

print(dict1["name"])
print(dict1.get("age"))


---

🔹 Adding / Updating Values

dict1["city"] = "Gwalior"   # add
dict1["age"] = 22            # update


---

🔹 Removing Elements

dict1.pop("age")
del dict1["branch"]


---

🔹 Important Methods

print(dict1.keys())
print(dict1.values())
print(dict1.items())


---

🔹 Looping Through Dictionary

for key, value in dict1.items():
    print(key, value)


---

🔹 Nested Dictionary

student = {
    "name": "Divya",
    "marks": {"math": 90, "eng": 85}
}

print(student["marks"]["math"])


---

🔹 Practice Questions

1. Count Frequency of Elements

lst = [1,2,2,3,3,3]
freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)

2. Merge Two Dictionaries

d1 = {"a":1}
d2 = {"b":2}

print({**d1, **d2})

3. Check Key Exists

if "name" in dict1:
    print("Exists")

4. Find Maximum Value

print(max(dict1.values()))


---

🔹 Example Program

student = {
    "name": "Divya",
    "age": 21,
    "marks": [90, 85, 88]
}

for key, value in student.items():
    print(key, value)




