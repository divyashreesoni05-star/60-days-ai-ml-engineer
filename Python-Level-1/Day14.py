# 1 Reverse List
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# 2 Max Element
print(max([10, 5, 20, 8]))

# 3 Remove Duplicates
print(list(set([1, 2, 2, 3, 4, 4])))

# 4 Frequency Count
arr = [1, 2, 2, 3, 3, 3]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print(freq)

# 5 Merge Dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)

# 6 Element in Set
print(2 in {1, 2, 3, 4})

# 7 Common Elements
print(list(set([1, 2, 3]) & set([2, 3, 4])))

# 8 Tuple Unpacking
a, b, c = (10, 20, 30)
print(a, b, c)

# 9 Sort Dictionary
d = {"b": 2, "a": 1, "c": 3}
print(dict(sorted(d.items())))

# 10 Union of Sets
print({1, 2, 3} | {3, 4, 5})
