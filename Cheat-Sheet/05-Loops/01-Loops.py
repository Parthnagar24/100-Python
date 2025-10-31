# 10-Loops_in_Python

# ------------------------------------------------------------
# 🔁 L O O P S  (Repetition in Python)
# ------------------------------------------------------------
# Loops allow you to repeat a block of code multiple times.
# Python provides two main types of loops:
#   1️⃣ while loop
#   2️⃣ for loop
# Along with special control statements like:
#   - break
#   - continue
#   - use of underscore (_) in loops
# ------------------------------------------------------------


# ============================================================
# 1️⃣ WHILE LOOP
# ============================================================
# The while loop repeats a block of code as long as the condition is True.
# Syntax:
# while condition:
#     # code to run repeatedly

n = 1
while n <= 5:   # loop runs until n becomes greater than 5
    print("Current number:", n)
    n += 1
print("Loop ended because condition became False.\n")
# Output:
# Current number: 1
# ...
# Current number: 5


# ============================================================
# 2️⃣ FOR LOOP
# ============================================================
# The for loop is used to iterate over a sequence (list, tuple, string, range, etc.).
# Syntax:
# for variable in sequence:
#     # code to run for each item

all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
    print("Fruit:", fruit)
# Output:
# Fruit: apple
# Fruit: banana
# Fruit: orange


# ============================================================
# 3️⃣ RANGE() WITH FOR LOOP
# ============================================================
# The range() function generates a sequence of numbers.
# Syntax: range(start, stop, step)
# start → starting number (default 0)
# stop  → stop before this number
# step  → increment (default 1)

print("\nUsing range():")
for num in range(1, 6):
    print(num, end=" ")  # prints 1 to 5
print("\n")


# ============================================================
# 4️⃣ BREAK STATEMENT
# ============================================================
# 'break' immediately exits the loop — even if the condition is still True.
# Useful when you want to stop looping early.

scores = [34, 67, 99, 105]
for s in scores:
    if s > 100:
        print("\nInvalid score found! Stopping loop.")
        break
    print("Score:", s)
# Output:
# Score: 34
# Score: 67
# Score: 99
# Invalid score found! Stopping loop.


# ============================================================
# 5️⃣ CONTINUE STATEMENT
# ============================================================
# 'continue' skips the current iteration and goes to the next one.
# The loop doesn’t stop — it just skips that particular round.

print("\nOdd numbers between 1 and 10:")
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # skip even numbers
    print(n)
# Output: 1 3 5 7 9


# ============================================================
# 6️⃣ UNDERSCORE (_) IN A FOR LOOP
# ============================================================
# If you don’t need the loop variable, use an underscore (_) as a placeholder.
# This makes your code cleaner and more readable.

print("\nPrinting 'Hello' 5 times using _:")
for _ in range(5):
    print("Hello")
# Output: Hello (5 times)


# ============================================================
# 7️⃣ INFINITE LOOPS
# ============================================================
# A loop that never ends because its condition is always True.
# Be careful — it can freeze your program if not handled correctly.
# Press Ctrl + C to stop it when running manually.

# Example (commented out for safety):
# while 5 > 1:
#     print("I'm a survivor!")  # This will print forever


# ============================================================
# 🧠 SUMMARY
# ============================================================
# while → repeats until condition becomes False
# for → iterates over items in a sequence
# range() → generates a sequence of numbers for looping
# break → exits the loop completely
# continue → skips one iteration and continues
# _ → placeholder when loop variable isn’t needed
# Infinite loop → loop with a condition that never becomes False
