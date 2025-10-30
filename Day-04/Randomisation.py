# Random Module Demonstration

import random
import my_module  # Custom module (should be in the same folder)

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# What is a Module?
# A module is a Python file that contains functions, variables, or classes
# It helps organize code into reusable components
# Example: random is a built-in module; my_module is a user-defined module

# Accessing a variable from another module
print(my_module.my_favourite_number)

# Generate a random float between 0 and 1
random_number = random.random()
print(random_number)

# Generate a random float between 1 and 10
random_float = random.uniform(1, 10)
print(random_float)

# Simulating a coin toss
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
