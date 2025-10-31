# 06-Conditional_Statements

# ----------------------------------------------
# IF STATEMENT
# ----------------------------------------------
# The 'if' statement tests whether a condition is True.
# If the condition evaluates to True, the indented block of code will execute.
# Otherwise, it will be skipped.

n = 5
if n > 2:
    print("Larger than 2")
# Output: Larger than 2


# ----------------------------------------------
# IF-ELSE STATEMENT
# ----------------------------------------------
# The 'else' block runs only when the 'if' condition is False.

age = 18
if age > 16:
    print("Can drive")
else:
    print("Don't drive")
# Output: Can drive


# ----------------------------------------------
# IF - ELIF - ELSE STATEMENT
# ----------------------------------------------
# 'elif' (else if) allows you to check multiple conditions in sequence.
# Once a True condition is found, the rest of the conditions are skipped.

weather = "sunny"
if weather == "rain":
    print("Bring an umbrella")
elif weather == "sunny":
    print("Bring sunglasses")
elif weather == "snow":
    print("Bring gloves")
else:
    print("Stay prepared for any weather!")
# Output: Bring sunglasses


# ----------------------------------------------
# NESTED IF STATEMENT
# ----------------------------------------------
# You can place an 'if' inside another 'if' block — this is called a nested if.
# It helps to test multiple levels of conditions.

score = 85
if score >= 50:
    print("You passed the exam!")
    if score >= 90:
        print("Excellent! Grade: A+")
    elif score >= 75:
        print("Great job! Grade: A")
    else:
        print("Good effort! Grade: B")
else:
    print("You failed. Better luck next time!")
# Output:
# You passed the exam!
# Great job! Grade: A
