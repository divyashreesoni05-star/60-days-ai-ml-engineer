# Day 02 - Data Types and Strings

# 1. Data Types in Python

a = 10          # int
b = 3.14        # float
c = "Python"    # string
d = True        # boolean
e = 2 + 3j      # complex

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# 2. String Example

text = "Python Programming"

print(text)


# 3. String Indexing

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # g


# 4. String Slicing

print(text[0:6])   # Python
print(text[7:18])  # Programming
print(text[:6])    # Python
print(text[7:])    # Programming


# 5. String Methods

name = "divya"

print(name.upper())   # DIVYA
print(name.lower())   # divya
print(len(name))      # length of string
