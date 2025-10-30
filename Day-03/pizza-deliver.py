print("Welcome to Pizza Delivery !")

pizza_size = input("What size of pizza do ypu want? S,M,l:")
pizza_pepperoni  = input("Do you want pepperoni ? in the pizza Y or N:")
pizza_cheese = input("Do you want extra cheese? y or N:")


if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25
else:
    print("Invalid size selected")
    bill = 0


if pizza_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    elif pizza_size == "M" or pizza_size == "L":
        bill += 3

        
if pizza_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your final bill is : ${bill}")