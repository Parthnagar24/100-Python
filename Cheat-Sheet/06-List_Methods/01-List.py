# 09-All_List_Methods_and_Slicing

# ------------------------------------------------------------
# 🧾 Understanding All Common List Methods in Python
# ------------------------------------------------------------

# Creating a sample list
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)

# 1️⃣ append() → Adds an item at the end of the list
fruits.append('orange')
print("After append:", fruits)

# 2️⃣ insert() → Inserts an item at a specific index
fruits.insert(1, 'mango')  # insert 'mango' at index 1
print("After insert:", fruits)

# 3️⃣ extend() → Adds elements from another list (concatenates lists)
tropical = ['pineapple', 'papaya']
fruits.extend(tropical)
print("After extend:", fruits)

# 4️⃣ remove() → Removes the first occurrence of a specified value
fruits.remove('banana')
print("After remove:", fruits)

# 5️⃣ pop() → Removes and returns an item by index (default is last item)
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)

# 6️⃣ index() → Returns the index of the first matching element
print("Index of 'apple':", fruits.index('apple'))

# 7️⃣ count() → Counts how many times an element appears in the list
fruits.append('apple')
print("After adding another apple:", fruits)
print("Count of 'apple':", fruits.count('apple'))

# 8️⃣ sort() → Sorts the list in ascending order (alphabetically or numerically)
fruits.sort()
print("After sort:", fruits)

# 9️⃣ reverse() → Reverses the order of the list
fruits.reverse()
print("After reverse:", fruits)

# 🔟 copy() → Returns a shallow copy of the list (creates a duplicate)
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 11️⃣ clear() → Removes all elements from the list (makes it empty)
fruits.clear()
print("After clear:", fruits)

# ------------------------------------------------------------
# ✂️ LIST SLICING
# ------------------------------------------------------------
# Slicing allows you to access parts (subsets) of a list.
# Syntax: list[start:end:step]
# start → index to begin (inclusive)
# end → index to stop (exclusive)
# step → optional, defines skipping interval

numbers = [10, 20, 30, 40, 50, 60, 70]
print("\nOriginal numbers list:", numbers)

# Slice from index 1 to 4 (excluding 4)
print("numbers[1:4]:", numbers[1:4])  # [20, 30, 40]

# Slice from start to index 2
print("numbers[:3]:", numbers[:3])    # [10, 20, 30]

# Slice from index 4 to end
print("numbers[4:]:", numbers[4:])    # [50, 60, 70]

# Slice last 3 elements using negative index
print("numbers[-3:]:", numbers[-3:])  # [50, 60, 70]

# Slice every second element
print("numbers[::2]:", numbers[::2])  # [10, 30, 50, 70]

# Reverse the list using slicing
print("numbers[::-1]:", numbers[::-1])  # [70, 60, 50, 40, 30, 20, 10]

# ------------------------------------------------------------
# 🧠 QUICK SUMMARY OF LIST METHODS
# ------------------------------------------------------------
# append()   → Add one item at end
# insert()   → Insert at a specific position
# extend()   → Add all elements from another list
# remove()   → Remove first occurrence of an item
# pop()      → Remove and return item by index
# index()    → Find index of first occurrence
# count()    → Count occurrences of an item
# sort()     → Sort list in ascending order
# reverse()  → Reverse list order
# copy()     → Return shallow copy
# clear()    → Remove all items
# slicing    → Extract parts of a list (using [start:end:step])
