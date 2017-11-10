import turtle

def hilbert(tortoise, reverse, depth):

    if depth == :
        tortoise.fd(10)

    else:
        tortoise.rt(90)
        hilbert(tortoise, reverse / 3, depth - 1)
        tortoise.fd(10)
        tortoise.lt(90)
        hilbert(tortoise, reverse / 3, depth - 1)
        tortoise.fd(10)
        hilbert(tortoise, reverse / 3, depth - 1)
        tortoise.lt(90)
        tortoise.fd(10)
        hilbert(tortoise, reverse / 3, depth - 1)
        tortoise.rt(90)


def main():
    myTurtle = turtle.Turtle()
    hilbert(myTurtle, 9, 0)
    screen = myTurtle.getscreen()
    screen.exitonclick()

main()
