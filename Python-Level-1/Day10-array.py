Day X - Python Array Practice

Remove duplicate numbers and reverse the array

def remove_duplicates(arr):
unique = []
for num in arr:
if num not in unique:
unique.append(num)
return unique

def reverse_array(arr):
return arr[::-1]

def main():
# Original array
arr = [1, 2, 3, 2, 4, 5, 3, 6]

print("Original Array:", arr)

# Remove duplicates
unique_arr = remove_duplicates(arr)
print("Array after removing duplicates:", unique_arr)

# Reverse array
reversed_arr = reverse_array(unique_arr)
print("Reversed Array:", reversed_arr)

if name == "main":
main()
