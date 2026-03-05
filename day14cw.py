import random
import math

# Ask user to enter names
names_input = input("Enter the names of invited guests (comma-separated): ")

# Convert input into list
names_list = names_input.split(",")

# Remove extra spaces and duplicates
unique_names = list(set(name.strip() for name in names_list))

# Randomly choose one name
chosen_name = random.choice(unique_names)

# Reverse the chosen name
reversed_name = chosen_name[::-1]

# Total number of unique names
total_unique = len(unique_names)

# Square root rounded to nearest whole number
sqrt_value = round(math.sqrt(total_unique))

# Display results
print("Unique names:", unique_names)
print("Selected name:", chosen_name)
print("Reversed name:", reversed_name)
print("Total unique names:", total_unique)
print("Rounded square root of total:", sqrt_value)