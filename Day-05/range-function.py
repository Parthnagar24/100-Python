# 🔢 Range Function in Python

# The range() function generates a sequence of numbers.
# Syntax: range(start, stop, step)
# Note: 'stop' value is *exclusive* (not included)

# Example 1: Just printing the range object
print(range(1, 11))   # Output: range(1, 11) → not the actual numbers

# Example 2: Looping through numbers 1 to 10
for number in range(1, 11):
    print(number)

# Example 3: Using step value (here it jumps by 3)
for number in range(1, 11, 3):
    print(number)

# Example 4: Sum of numbers from 1 to 100 using a for loop
total = 0
for number in range(1, 101):
    total += number
print("Sum from 1 to 100:", total)
