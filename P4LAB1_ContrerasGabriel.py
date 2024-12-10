# Gabriel
# 29OCT2024
# P4LAB1
# Use loops and turtle library to draw a house

import turtle

# Set up the window and turtle object
window = turtle.Screen()
tom = turtle.Turtle()

# Change the feautures of the turtle
tom.pensize(10)
tom.pencolor("red")
tom.shape("arrow")

# While loop that runs 4 times

movement = 0
while movement  <= 3:
    movement += 1
    tom.forward(100)
    tom.right(90)

# For loop to run 3 times
for side in range(3):
    tom.forward(100)
    tom.left(120)
    print(side)




