import turtle

def hilbert(tortoise, reverse, depth):
    if reverse == True:
        angle = 270
        
    else:
        angle = 90
        
    if depth < 0:
        tortoise.fd(0)

    else:
        tortoise.rt(angle)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.fd(10)
        tortoise.lt(angle)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.fd(10)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.lt(angle)
        tortoise.fd(10)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.rt(angle)
    
  

def main():
    reverse = False
    myTurtle = turtle.Turtle()
    myTurtle.lt(90)
    hilbert(myTurtle, reverse, 1)
    screen = myTurtle.getscreen()
    screen.exitonclick()

main()

