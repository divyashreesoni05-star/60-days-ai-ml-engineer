
# 📅 Day 16: Top 10 Python Data Structure Questions
# 👩‍💻 Divyashree Soni

print("----- 1. Reverse a List -----")
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)


print("\n----- 2. Find Maximum Element in List -----")
numbers = [10, 5, 20, 8]
print(max(numbers))


print("\n----- 3. Remove Duplicates from List -----")
numbers = [1, 2, 2, 3, 4, 4]
unique = list(set(numbers))
print(unique)


print("\n----- 4. Count Frequency using Dictionary -----")
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)


print("\n----- 5. Merge Two Dictionaries -----")
d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)


print("\n----- 6. Check if Element Exists in Set -----")
s = {1, 2, 3, 4}
print(2 in s)


print("\n----- 7. Find Common Elements in Two Lists -----")
l1 = [1, 2, 3]
l2 = [2, 3, 4]

common = list(set(l1) & set(l2))
print(common)


print("\n----- 8. Tuple Unpacking -----")
t = (10, 20, 30)
a, b, c = t
print(a, b, c)


print("\n----- 9. Sort Dictionary by Keys -----")
d = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


print("\n----- 10. Find Union of Two Sets -----")
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)


print("\n🚀 All Questions Executed Successfully!")
