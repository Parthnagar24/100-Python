# 08-Comparison_Operators

# ----------------------------------------------
# COMPARISON OPERATORS
# ----------------------------------------------
# Comparison operators are used to compare two values.
# They always return a Boolean value — either True or False.

# 1️⃣ Greater than (>)
x = 10
y = 5
print(x > y)   # True → because 10 is greater than 5

# 2️⃣ Less than (<)
print(x < y)   # False → because 10 is not less than 5

# 3️⃣ Greater than or equal to (>=)
a = 7
b = 7
print(a >= b)  # True → because 7 is equal to 7

# 4️⃣ Less than or equal to (<=)
m = 4
n = 9
print(m <= n)  # True → because 4 is less than 9

# 5️⃣ Equal to (==)
age = 18
print(age == 18)  # True → both sides are equal

# 6️⃣ Not equal to (!=)
color = "red"
print(color != "blue")  # True → because 'red' is not 'blue'

# ----------------------------------------------
# COMPARISON OPERATORS IN CONDITIONS
# ----------------------------------------------
# You can use these operators inside 'if' statements for decision making.

score = 85
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")
# Output: Grade B
