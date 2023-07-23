# List built-in data structures / Python

# LIST
lst = [1, 2, 3, 4, "a", "b", "c", 38.5, "56.7"]
print(lst)  # Lists are mutable and can store heterogeneous data types.
print(type(lst))
print(type(lst[-1]))

# Append function in list
l1 = [1, 2, 3, 4, 5, 6]
l1.append(3)  # adds an element at the end of the list:
l1.append([7, 8, 9])
l1.extend([6, 7, 8])
print(l1)

# Insert function in a list

l2 = [1, 2, 3, 4, 5, 6]
l2.insert(2, 6)  # inserts an element at the specified element:
print(l2)

# Count function in python
l3 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
s = l3.count(4)  # counts the occurrences of a character/number.
print(s)

# Sort and sorted function in a list
a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print("a after sorted function")
print(a)
print(x)
b = [1, 2, 5, 8, 3]
b.sort()
print(b)
