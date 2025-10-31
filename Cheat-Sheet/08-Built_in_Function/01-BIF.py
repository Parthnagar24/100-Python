# 11-Built_in_Functions_and_Randomisation

# ------------------------------------------------------------
# 🧮 B U I L T - I N   F U N C T I O N S
# ------------------------------------------------------------
# Python has several built-in functions that perform useful tasks.
# Below are some commonly used ones: randomisation, range, abs, and round.
# ------------------------------------------------------------


# ============================================================
# 1️⃣ RANDOMISATION
# ============================================================
# The 'random' module allows you to generate random numbers or select random items.
# You must import it before using any random functions.

import random

# Syntax:
# random.randint(start, end)
# → Returns a random integer N such that start <= N <= end

n = random.randint(2, 5)
print("Random number between 2 and 5:", n)
# Example output: Random number between 2 and 5: 4

# You can also generate random floats using random.random()
# random.random() → returns a float between 0.0 and 1.0
print("Random float between 0 and 1:", random.random())

# Or pick a random choice from a list:
colors = ["red", "blue", "green", "yellow"]
print("Random color:", random.choice(colors))


# ============================================================
# 2️⃣ RANGE()
# ============================================================
# The range() function generates a sequence of numbers.
# Syntax: range(start, end, step)
# - start → where the sequence begins (included)
# - end   → where the sequence ends (excluded)
# - step  → how much to increment or decrement by (default = 1)

print("\nRange Example: Counting backwards by 2 from 6 to 0 (exclusive):")
for i in range(6, 0, -2):
    print(i)
# Output: 6, 4, 2
# 0 is not included because the end value is always excluded.


# ============================================================
# 3️⃣ ABSOLUTE VALUE (abs)
# ============================================================
# The abs() function returns the absolute value of a number.
# It removes any negative sign.

print("\nAbsolute Value Examples:")
print("abs(-4.6):", abs(-4.6))   # Output: 4.6
print("abs(10):", abs(10))       # Output: 10


# ============================================================
# 4️⃣ ROUND()
# ============================================================
# The round() function rounds a number to the nearest integer (or to a given number of decimal places).
# Syntax: round(number, ndigits)
# - number → the number to round
# - ndigits → (optional) how many decimals to keep

print("\nRounding Examples:")
print("round(3.1):", round(3.1))    # Output: 3
print("round(4.5):", round(4.5))    # Output: 4 or 5 depending on Python version (banker's rounding)
print("round(5.8):", round(5.8))    # Output: 6
print("round(3.14159, 2):", round(3.14159, 2))  # Output: 3.14


# ============================================================
# 🧠 QUICK SUMMARY
# ============================================================
# import random      → brings in random module
# random.randint(a, b) → random integer between a and b (inclusive)
# random.choice(seq) → random element from a list or sequence
# range(start, end, step) → generates sequence of numbers
# abs(x)             → absolute (non-negative) value of x
# round(x, n)        → rounds x to n decimal places (default: nearest integer)
