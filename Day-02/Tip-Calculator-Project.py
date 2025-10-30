# Tip Calculator Program

print("Welcome to the tip calculator!")

# Taking user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculating total bill including tip
bill_with_tip = bill + (tip / 100 * bill)

# Calculating amount per person
bill_per_person = bill_with_tip / people

# Rounding final amount to 2 decimal places
final_amount = round(bill_per_person, 2)

# Displaying the result using f-string
print(f"Each person should pay: ${final_amount}")
