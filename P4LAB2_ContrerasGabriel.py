# Gabriel
# 31OCT2024
# P4LAB2
# Program asks user for integer and displays multiplication table

# Make a while loop to control program running continuously 

run_again = "yes"

while run_again == "yes" or run_again == "y":
    user_int = int(input("Enter an integer: "))
    print()    
    if user_int >= 0:
        # Print multiplication table
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")
    else:
        print("Cannot accept negative values!!")
    print()
    run_again = input("Would you like to run the program again? ").lower()
    valid_inputs = ["yes", "y", "no", "n"]
    # Validate the user's input
    while run_again not in valid_inputs:
        print("INVALID RESPONSE ENTERED!")
        run_again = input("Would you like to run the program again? ").lower()

# Loop breaks
print("Thank you for using this program...")

