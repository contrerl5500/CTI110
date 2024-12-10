# Gabriel 
# 03SEP2024
# P2LAB2
# Using dictionary with user input

# Create the dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Get the keys only
keys = cars.keys()
# Get values from dictionary
print(keys)
print()

# Prompt user to give on of the keys
user_choice = input("Enter a vehicle to see it's MPG: ")
print()

# Show user mpg for their selected car
print(f"The {user_choice} gets {cars[user_choice]} MPG.")
print()

# Ask user how many miles will you drive
miles_to_drive = float(input(f"How many miles will you drive the {user_choice}? "))

# Calcuate gallons needed to drive selected key
gallons_needed = miles_to_drive/ cars[user_choice]

# Display gallons needed to the user
print(f"{gallons_needed:.2f} of gas are needed to drive the {user_choice} {miles_to_drive} miles.")




