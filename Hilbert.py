import turtle

def hilbert(tortoise, reverse, depth):
        
    if depth < 0:
        return

    if reverse == True:
        tortoise.rt(90)
        hilbert(tortoise, False, depth - 1)
        tortoise.fd(10)
        tortoise.lt(90)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.fd(10)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.lt(90)
        tortoise.fd(10)
        hilbert(tortoise, False, depth - 1)
        tortoise.rt(90)
        
    else:
        tortoise.lt(90)
        hilbert(tortoise, True, depth - 1)
        tortoise.fd(10)
        tortoise.rt(90)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.fd(10)
        hilbert(tortoise, reverse, depth - 1)
        tortoise.rt(90)
        tortoise.fd(10)
        hilbert(tortoise, True, depth - 1)
        tortoise.lt(90)
        
    


def main():
    reverse = True
    myTurtle = turtle.Turtle()
    myTurtle.lt(90)
    hilbert(myTurtle, reverse, 5)
    screen = myTurtle.getscreen()
    screen.exitonclick()

main()

