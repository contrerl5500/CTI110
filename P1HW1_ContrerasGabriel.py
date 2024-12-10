# Gabriel Contreras
# 17SEP2024
# P1HW1
# Input and Output with mathematical expressions

print("----Calculating Exponents----")
print()
print()

# Get base value (as an integer) from the user
base_value = int(input("Enter an integer as the base value: "))

# Get exponent value (as an integer) from the user
exponent = int(input("Enter an integer as the exponent: "))

# Raise the base_value to the exponent
result = base_value ** exponent 
print()
print()

# Display output to the user
print(base_value, "raised to the power of", exponent, "is", result, "!!")

      
print()
print()
print("----Addition and Subtraction----")
print()
print()

start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print()
print()

print(start_num, "+", add_num, "-", sub_num, "is equal to", start_num + add_num - sub_num)
