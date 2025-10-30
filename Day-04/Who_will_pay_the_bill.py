# 🎯 Banker Roulette Game
# Randomly selects one person who will pay the bill

import random

# List of friends
friends = ['A', 'B', 'C', 'D', 'E']

# Randomly choose one friend to pay the bill
#random.choice() is a built-in method in Python’s random module that selects one random item from a non-empty sequence like a list, tuple, or string.
payer = random.choice(friends)

# Display the result
print(f"{payer} is going to buy the meal today!")





friends = ['A', 'B', 'C', 'D', 'E']
random_index = random.randint(0, 4)
payer = friends[random_index]
print(f"{payer} is going to buy the meal today!")
