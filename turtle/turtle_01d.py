import turtle

def draw_square(size=50):
    for _ in range(4):
        turtle.fd(size)
        turtle.rt(90)

if __name__ == '__main__': 
    draw_square()
    draw_square(150)
