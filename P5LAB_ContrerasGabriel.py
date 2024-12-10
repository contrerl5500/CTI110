# Gabriel Contreras
# 17NOV2024
# P5LAB
# Simulate customer using self-checkout


import random  

def disperse_change(change):
    """
    Takes the change amount (in dollars) and calculates the number of 
    dollars, quarters, dimes, nickels, and pennies to give as change.
    """
    # Convert change to cents to avoid floating-point issues
    change = round(change * 100)

    # Calculate the amount of dollars
    num_dollars = change // 100
    change %= 100  # Update the remaining change

    # Calculate the amount of quarters
    num_quarters = change // 25
    change %= 25

    # Calculate the amount of dimes
    num_dimes = change // 10
    change %= 10

    # Calculate the amount of nickels
    num_nickels = change // 5
    change %= 5

    # Remaining amount is pennies
    num_pennies = change

    # Print the results with grammatical correctness
    if num_dollars > 0:
        print(f"{num_dollars} dollar{'s' if num_dollars > 1 else ''}")
    if num_quarters > 0:
        print(f"{num_quarters} quarter{'s' if num_quarters > 1 else ''}")
    if num_dimes > 0:
        print(f"{num_dimes} dime{'s' if num_dimes > 1 else ''}")
    if num_nickels > 0:
        print(f"{num_nickels} nickel{'s' if num_nickels > 1 else ''}")
    if num_pennies > 0:
        print(f"{num_pennies} penn{'y' if num_pennies == 1 else 'ies'}")

def main():
    
    # Generate a random total owed by the customer
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed:.2f}")

    # Prompt the user to enter the amount of money they will input
    while True:
        try:
            money_given = float(input("How much cash will you input: $"))
            if money_given < total_owed:
                print("amount you entered is less than the total owed. Try again!")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Calculate change owed
    change = money_given - total_owed
    print(f"Change is: ${change:.2f}")

    # Call the disperse_change function to calculate the breakdown of the change
    disperse_change(change)

# Call the main function to start the program
if __name__ == "__main__":
    main()
