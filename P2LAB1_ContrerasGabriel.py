# Name
# 01SEP2024
# P2LAB1
# Using built-in libraries for circle calculations

#Import the math library
import math

# Create a variable to hold pi
pi = math.pi

print(pi)

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate/display the diameter
diam = 2 * radius
print(f"The diameter of the circle is {diam:.1f}\n")

# Calculate/display the circumference
circum = 2 * pi * radius
print(f"The circumferene of the circle is {circum:.2f}\n")

# Calculate/display the area
area = pi * radius ** 2
print(f"The area of the circle is {area:.3f}")
