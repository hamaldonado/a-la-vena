import turtle

def draw_square(size):
    for _ in range(4):
        turtle.fd(size)
        turtle.rt(90)

if __name__ == '__main__': 
    draw_square(100)
    draw_square(75)
    draw_square(50)
    draw_square(25)
