import turtle

def spiral():
    colors = ['red', 'purple', 'blue',
              'green', 'orange', 'yellow']
    #t = turtle.Pen()
    turtle.speed(0)

    turtle.bgcolor('black')
       
    for x in range(360):
        turtle.pencolor(colors[x % 6])
        turtle.width(x // 100 + 1)
        turtle.fd(x)
        turtle.lt(59)

if __name__ == '__main__':
    spiral()
    turtle.exitonclick()
