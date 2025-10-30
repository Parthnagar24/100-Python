# Understanding All Common List Methods in Python

fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)

# 1️⃣ append() - Adds an item at the end
fruits.append('orange')
print("After append:", fruits)

# 2️⃣ insert() - Adds an item at a specific index
fruits.insert(1, 'mango')  # insert mango at index 1
print("After insert:", fruits)

# 3️⃣ extend() - Adds elements from another list
tropical = ['pineapple', 'papaya']
fruits.extend(tropical)
print("After extend:", fruits)

# 4️⃣ remove() - Removes the first matching value
fruits.remove('banana')
print("After remove:", fruits)

# 5️⃣ pop() - Removes and returns an item by index (default: last item)
popped = fruits.pop()  # removes last element
print("Popped item:", popped)
print("After pop:", fruits)

# 6️⃣ index() - Returns index of first matching value
print("Index of 'apple':", fruits.index('apple'))

# 7️⃣ count() - Counts how many times a value appears
fruits.append('apple')
print("After adding another apple:", fruits)
print("Count of 'apple':", fruits.count('apple'))

# 8️⃣ sort() - Sorts the list in ascending order
fruits.sort()
print("After sort:", fruits)

# 9️⃣ reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse:", fruits)

# 🔟 copy() - Returns a shallow copy of the list
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 11️⃣ clear() - Removes all items from the list
fruits.clear()
print("After clear:", fruits)
