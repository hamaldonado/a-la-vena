import time
import termio as t
from termio import Color
import kbhit
import random

SCREEN_HEIGHT = 20
SCREEN_WIDTH = 60

# Condicion inicial
snake_dir = "R"   # U:up  D:Down L:Left R:Right
snake = [(10, 6), (10, 5), (10, 4), (10, 3)]
snake_size = 4
fruits = []

speed = 0.5


def draw_scenery():
    t.cls()

    print(Color.F_BRIGHT_YELLOW)

    t.locate(1,1); print("#" * SCREEN_WIDTH)

    for line in range(2, SCREEN_HEIGHT):
        t.locate(line, 1); print("#")
        t.locate(line, SCREEN_WIDTH); print("#")

    t.locate(SCREEN_HEIGHT,1); print("#" * SCREEN_WIDTH)

    print(Color.F_DEFAULT)


def draw_fruits():
    
    global fruits

    for _ in range(20):
        line = random.randint(2, SCREEN_HEIGHT - 1)
        col = random.randint(2, SCREEN_WIDTH - 1)

        fruits.append((line,col))    

        t.locate(line, col); print(f"{Color.F_BRIGHT_RED}&{Color.F_DEFAULT}")


def update_snake():

    global snake, snake_size, fruits, speed

    head_line, head_col = snake[0]
    tail_line, tail_col = snake[snake_size - 1]

    match snake_dir:

        case "U":
            head_line -= 1

        case "R":
            head_col += 1

        case "D":
            head_line += 1

        case "L":
            head_col -= 1


    # Nueva posicion de la cabeza
    snake.insert(0, (head_line, head_col))
    
    # Colisiona con pared?
    if head_line in (1, SCREEN_HEIGHT) or head_col in (1, SCREEN_WIDTH):
        return False
    
    # Colisiona consigo misma?
    if (head_line, head_col) in snake[1:]:
        return False
    
    # Se come una fruta?
    if (head_line, head_col) in fruits:
        # No borramos la cola, aumentamos el tamano de la serpiente y la velocidad
        snake_size += 1
        speed /= 1.1

        fruits.remove((head_line, head_col))
    
    else:
        # Borramos la cola
        t.locate(tail_line, tail_col); print(" ")
        snake.pop(len(snake) - 1)

    
    # Dibujamos la serpiente
    for pos in snake:
        line, col = pos
        t.locate(line, col); print(f"{Color.F_BRIGHT_GREEN}@{Color.F_DEFAULT}") 

    return True


def main():
    global snake_dir, speed
    
    draw_scenery()
    draw_fruits()
    
    kb = kbhit.KBHit()

    while True:

        if kb.kbhit():

            c = kb.getarrow()

            match c:
                case 0: # UP
                    if snake_dir in ("R", "L"):
                        snake_dir = "U"
                case 1: # RIGHT
                    if snake_dir in ("U", "D"):
                        snake_dir = "R"
                case 2: # DOWN
                    if snake_dir in ("R", "L"):
                        snake_dir = "D"
                case 3: # LEFT
                    if snake_dir in ("U", "D"):
                        snake_dir = "L"

        if not update_snake():

            # Se choco, perdio el juego
            t.locate(SCREEN_HEIGHT // 2, 1)
            print("GAME OVER!".center(SCREEN_WIDTH))
            break
        
        # Gana?
        if len(fruits) == 0:
            t.locate(SCREEN_HEIGHT // 2, 1)
            print("GANASTE!".center(SCREEN_WIDTH))
            break

        time.sleep(speed)


t.hide_cursor()
main()
t.show_cursor()
t.locate(SCREEN_HEIGHT + 1, 1)