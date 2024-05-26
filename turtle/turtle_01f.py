import turtle

def draw_polygon(size=50, sides=4):
    for _ in range(sides):
        turtle.fd(size)
        turtle.rt(360 // sides)

def draw_triangle(size=50):
    draw_polygon(size, 3)

def draw_square(size=50):
    draw_polygon(size, 4)

def draw_pentagon(size=50):
    draw_polygon(size, 5)

def draw_hexagon(size=50):
    draw_polygon(size, 6)

if __name__ == '__main__':
    turtle.pu()
    turtle.goto(-50, 100)
    turtle.pd()
    draw_triangle(25)
    draw_square()
    draw_pentagon(75)
    draw_hexagon(100)
    draw_polygon(80, 12)
    
