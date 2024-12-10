# Contreras
# 26SEP2024
# P1HW2
# Calcualte and Display Expenses

print("This program calculates and displays travel expenses")
print()

# Get travel info from user
bud1 = float(input("Enter Budget: "))
print()
dest1 = input("Enter travel destination: ")
print()
gas1 = float(input(f"How much do you think you will spend on gas to {dest1}? "))
print()
lod1 = float(input(f"Approximately, how much will you need for lodging to {dest1}? "))
print()
eat1 = float(input(f"Last, how much do you need for food on your way to {dest1}? "))
print()
print()

# Calculate Expenses
total_expenses = gas1 + lod1 + eat1

# Calculate Remaining Balance
left_over = bud1 - total_expenses

# Display Results
print("-------Travel Expenses------")
print(f"Location: {dest1}")
print(f"Initial Budget: ${bud1:.2f}\n")
print(f"Fuel Expenses: ${gas1:.2f}")
print(f"Accommodation Expenses: ${lod1:.2f}")
print(f"Food Expenses: ${eat1:.2f}\n\n")

print(f"Remaining Budget: ${left_over:.2f}")










