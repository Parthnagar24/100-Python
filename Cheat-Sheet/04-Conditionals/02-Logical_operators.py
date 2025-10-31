# 07-Logical_Operators

# ----------------------------------------------
# AND OPERATOR
# ----------------------------------------------
# The 'and' operator expects BOTH conditions to be True.
# If either condition is False, the entire expression becomes False.

s = 58
if s < 60 and s > 50:
    print("Your grade is C")
# Explanation:
# s < 60 → True
# s > 50 → True
# Both True → condition is True → prints "Your grade is C"
# Output: Your grade is C


# ----------------------------------------------
# OR OPERATOR
# ----------------------------------------------
# The 'or' operator expects AT LEAST ONE condition to be True.
# If both conditions are False, then only it returns False.

age = 12
if age < 16 or age > 200:
    print("Can't drive")
# Explanation:
# age < 16 → True
# age > 200 → False
# Since one condition is True → prints "Can't drive"
# Output: Can't drive


# ----------------------------------------------
# NOT OPERATOR
# ----------------------------------------------
# The 'not' operator reverses the result of a condition.
# If a condition is True, 'not' makes it False — and vice versa.

if not 3 > 1:
    print("something")
# Explanation:
# 3 > 1 → True
# not True → False
# So the code inside if will NOT run.
# Output: (nothing printed)


# ----------------------------------------------
# COMBINED EXAMPLE
# ----------------------------------------------
# You can combine 'and', 'or', and 'not' in one condition.

marks = 75
if marks >= 60 and not marks > 90:
    print("You passed, but not with distinction.")
# Explanation:
# marks >= 60 → True
# marks > 90 → False → not False → True
# Both True → condition True → prints message
# Output: You passed, but not with distinction.
