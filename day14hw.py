import random
import math

# Ask user to enter customer names
names = input("Enter customer names (comma-separated): ")

# Convert input into list
name_list = names.split(",")

# Remove spaces and duplicates
unique_names = list(set(name.strip() for name in name_list))

# Shuffle the names
random.shuffle(unique_names)

# Pick 2 winners
winners = random.sample(unique_names, 2)

# Reverse winner names
winner1 = winners[0][::-1]
winner2 = winners[1][::-1]

# Total participants
total = len(unique_names)

# Square root rounded
sqrt_value = round(math.sqrt(total))

# Display results
print("Winner 1 (reversed):", winner1)
print("Winner 2 (reversed):", winner2)
print("Total unique participants:", total)
print("Rounded square root of participants:", sqrt_value)