
import turtle     #importing Turtle commands from computer for all programs
import random     #importing Random commands from computer for all programs


def tree(tortoise, length, depth, angle): #defining the tree function, with all desired parameters
'''
    Recursively draw a tree with random branch angles, or 10.1.1
    Parameters:
    tortoise: a Turtle object
    length: the length of the trunk
    depth: the desired depth of recursion
    The tree wont look more natural
    Return value: none
'''
    length = random.uniform(10, 100) # I wanted random lengths bewteen 10 and 100 length, so I used the Uniform command
    angle = random.randint(10, 60)   # I also wanted random angles between 10 and 60 degrees, so I used the randint command

    if depth <= 1:                     #the base case
        tortoise.forward(length) #Lines 20, 21, 24, 25, 28, 31, and 33 are self- explainatory
        tortoise.backward(length)
    else:                              #the recursive case
        tortoise.speed(0)   #Turtle's speed, with 0 being fastest
        tortoise.forward(length)
        tortoise.lt(angle)
        tortoise.setheading(angle) # sets the turtle to follow a variable's angle
        tree(tortoise, length * (2 / 3), depth - 1, angle) # I ran the function, multiplied the length by 2/3, and took 1 form the depth variable.
        tortoise.right(angle)
        tortoise.setheading(angle)
        tree(tortoise, length * (2 / 3), depth - 1, angle) # Refer to Line 27's explaination
        tortoise.left(angle)
        tortoise.setheading(angle) #Refer to line 26.
        tortoise.backward(length)

def main():     # Main function. Allows the previous function to run.
    george = turtle.Turtle() #Constructing the Turtle.
    george.left(90)
    angle = random.randint(10, 60) # Line 17, but repeated
    tree(george, 100, 9, angle) #Running the tree function, with all of our parameters inputted.
    screen = george.getscreen() #Turtle gets the screen functions.
    screen.exitonclick() #Exits program on mouse click

main() #Running the whole program


def quadkoch(tortoise, length, depth): #Defining the function, along with all parmameters
'''
    Recursively draw a  qadratic Koch curve
10.1.2
    Parameters:
    tortoise: a Turtle object
    length: the length of a line segment
    depth: the desired depth of recursion

    Return value: none
'''

    if depth == 0:                  #base case
        tortoise.fd(length) #Self-explainatory, along with lines 63, 65, 67, and 69.
    else:                           #recursive case
        tortoise.speed(0) #Turtle's speed, with 0 being fastest
        quadkoch(tortoise, length / 3, depth - 1) #Running the function, and dividing length by 3, and dividing depth by 1.
        tortoise.lt(90)
        quadkoch(tortoise, length / 3, depth - 1) # Refer to Line 62
        tortoise.rt(90)
        quadkoch(tortoise, length / 3, depth - 1) # Refer to Line 62
        tortoise.rt(90)
        quadkoch(tortoise, length / 3, depth - 1) # Refer to Line 62
        tortoise.lt(90)
        quadkoch(tortoise, length / 3, depth - 1) # Refer to Line 62

def main(): # Main function. Allows the previous function to run.
    george = turtle.Turtle() #Constructing our Turtle.
    quadkoch(george, 400, 3) #Running the previous function
    screen = george.getscreen() #Turtle gets the screen function
    screen.exitonclick() #Exits program on mouse click

main() #runs whole program


def koch(tortoise, length, depth): # Defining the function
'''
Recursively draw a Koch Curve, with added Snowflake functionality
Parameters:
tortoise: a Turtle object
length: the length of the Koch Curve
depth: the desired depth of recursion
Return value: none

'''
    if depth == 0:              #base case
        tortoise.fd(length)
    else:                       #recursive case
        tortoise.speed(0) #Turtle's speed, with 0 being fastest.
        koch(tortoise, length / 3, depth - 1) #Running the function, and dividing length by 3, and dividing depth by 1.
        tortoise.lt(60)
        koch(tortoise, length / 3, depth - 1) #Refer to line 95.
        tortoise.rt(120)
        koch(tortoise, length / 3, depth - 1) #Refer to line 95.
        tortoise.lt(60)
        koch(tortoise, length / 3, depth - 1)  #Refer to line 95. 


def kochSnowFlake(tortoise, length, depth, sides): #Defining the second fuction, with all parameters.
'''
Added Snowflake-making functionality to the Koch curve function. 10.1.4
Parameters:
tortoise: a Turtle object
length: the length of the sides of the snowflake.
depth: the depth of recursion
sides: the number of desired sides
Return value: none
'''
    for side in range(sides): # for loop allowing for a polygon made of Koch curves, or a "snowflake"
        koch(tortoise, length, depth)
        angle = 360 / sides
        tortoise.rt(angle)
        turtle.setheading(angle)

def main(): #Main function allows the previous functions to run.
    sides = input('How many sides do you want the snowflake to have?') #user- decided input. Allows choice of snowflake sides.
    bob = turtle.Turtle() #Constructing Turtle
    kochSnowFlake(bob, 400, 3, int (sides)) #Runs kochSnowFlake function.

main() #runs whole program
