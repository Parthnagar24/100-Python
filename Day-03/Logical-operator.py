print("Welcome to Pizza Delivery!")

# Take user inputs
pizza_size = input("What size of pizza do you want? S, M, or L: ").upper()
pizza_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
pizza_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initialize bill
bill = 0

# Base price using logical operators
if (pizza_size == "S") or (pizza_size == "M") or (pizza_size == "L"):
    if pizza_size == "S":
        bill = 15
    elif pizza_size == "M":
        bill = 20
    elif pizza_size == "L":
        bill = 25
else:
    print("Invalid pizza size selected!")

# Pepperoni and cheese additions using logical operators
if (pizza_pepperoni == "Y") and (pizza_size == "S"):
    bill += 2
elif (pizza_pepperoni == "Y") and ((pizza_size == "M") or (pizza_size == "L")):
    bill += 3

if (pizza_cheese == "Y"):
    bill += 1

# Final bill output
if (pizza_size == "S" or pizza_size == "M" or pizza_size == "L") and (bill > 0):
    print(f"Your final bill is: ${bill}")
