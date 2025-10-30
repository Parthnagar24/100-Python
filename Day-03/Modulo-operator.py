# Even or Odd Number Checker

# Take user input
number_to_check = int(input("Enter a number: "))

# Check if number is even or odd using modulus operator
if number_to_check % 2 == 0:
    print(f"{number_to_check} is an even number.")
else:
    print(f"{number_to_check} is an odd number.")
