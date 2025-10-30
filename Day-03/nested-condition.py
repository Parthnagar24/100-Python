height = int(input("Enter your height in cm: "))

if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("Ticket cost: $5")
    else:
        print("Ticket cost: $10")
else:
    print("Sorry, you can't ride.")
