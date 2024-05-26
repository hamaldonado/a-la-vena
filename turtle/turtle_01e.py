import turtle

def draw_triangle(size=50):
    for _ in range(3):
        turtle.fd(size)
        turtle.rt(120)

def draw_square(size=50):
    for _ in range(4):
        turtle.fd(size)
        turtle.rt(90)

def draw_pentagon(size=50):
    for _ in range(5):
        turtle.fd(size)
        turtle.rt(72)

def draw_hexagon(size=50):
    for _ in range(6):
        turtle.fd(size)
        turtle.rt(60)

if __name__ == '__main__': 
    draw_triangle(25)
    draw_square(50)
    draw_pentagon(75)
    draw_hexagon(100)    
