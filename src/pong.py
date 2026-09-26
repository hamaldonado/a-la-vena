from termio import locate, cls, hide_cursor, show_cursor
import keyboard as kb
import math
import time
import random

# Constantes Globales
UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

PADDLE_1 = 1
PADDLE_2 = 2

PADDLE_SPRITE = [
    "█",
    "█",
    "█",
    "█"
]

# Variables Globales
speed = 30

p1_pos = 16
p2_pos = 16

p1_score = 0
p2_score = 0
last_scorer = ""

ball_row_pos = 18
ball_col_pos = 50
ball_direction = RIGHT
ball_angle = 0   # En grados, 0 es horizontal, 90 es vertical


def draw_border():

    # El tablero tiene 33 lineas y 101 columnas.
    # La linea 1 es para el titulo, la linea 2 es para el marcador, la linea 3 es para separar el marcador del area jugable.
    # El area jugable del tablero (por donde la bola se puede mover) inicia en la linea 4, columna 2 y termina en la linea 32, columna 100. 
    # En total hay 29 lineas y 99 columnas jugables.
    # La posicion central donde inicia la bola es la linea 18, columna 50. 
    
    locate(1, 2); print("─"*99)
    locate(3, 2); print("─"*99)
    locate(33, 2); print("─"*99)

    for i in range(1, 34):
        locate(i, 1); print("│")
        locate(i, 101); print("│")

    locate(1, 1); print("┌")
    locate(1, 101); print("┐")
    locate(3, 1); print("├")
    locate(3, 101); print("┤")
    locate(33, 1); print("└")
    locate(33, 101); print("┘")

    locate(2, 2); print("PONG!".center(95))

    # Paddles en posicion inicial
    draw_paddle(PADDLE_1, p1_pos)
    draw_paddle(PADDLE_2, p2_pos)


def draw_score():
    locate(2, 3); print(f"P1: {p1_score}".ljust(10))
    locate(2, 90); print(f"P2: {p2_score}".rjust(10))


def draw_ball():
    locate(int(ball_row_pos), ball_col_pos); print("●")

    #locate(35,1); print(f"Ball pos: {ball_row_pos}, {ball_col_pos} | Angle: {ball_angle} | Direction: {'RIGHT' if ball_direction == RIGHT else 'LEFT'}")


def draw_paddle(paddle: int, pos: int):

    if paddle == PADDLE_1:
        col = 2
        pos = p1_pos
    else:
        col = 100
        pos = p2_pos

    if pos > 4:
        locate(pos - 1, col); print(" ")
    if pos < 29:
        locate(pos + 4, col); print(" ")

    locate(pos, col); print(PADDLE_SPRITE[0])
    locate(pos + 1, col); print(PADDLE_SPRITE[1])
    locate(pos + 2, col); print(PADDLE_SPRITE[2])
    locate(pos + 3, col); print(PADDLE_SPRITE[3])


def move_paddle(paddle: int, direction: int):
    global p1_pos, p2_pos

    if paddle == PADDLE_1:
        if direction == UP and p1_pos > 4:
            p1_pos -= 1
        elif direction == DOWN and p1_pos < 29:
            p1_pos += 1

        draw_paddle(PADDLE_1, p1_pos)

    elif paddle == PADDLE_2:
        if direction == UP and p2_pos > 4:
            p2_pos -= 1
        elif direction == DOWN and p2_pos < 29:
            p2_pos += 1

        draw_paddle(PADDLE_2, p2_pos)


def move_ball():
    global ball_row_pos, ball_col_pos, ball_direction, ball_angle, p1_score, p2_score, last_scorer

    # Borramos la bola de su posicion actual
    locate(int(ball_row_pos), ball_col_pos); print(" ")

    # Calculamos la nueva posicion de la bola segun su direccion y angulo
    ball_col_pos += (2 if ball_direction == RIGHT else -2)
    
    ball_row_pos = ball_row_pos + math.tan(math.radians(ball_angle))

    if ball_row_pos < 4:
        ball_row_pos = 4
        ball_angle = -ball_angle

    if ball_row_pos > 32:
        ball_row_pos = 32
        ball_angle = -ball_angle

    if ball_col_pos < 3:

        # Detectamos si la bola ha chocado con el paddle del jugador 1
        if p1_pos <= int(ball_row_pos) <= p1_pos + 3:
            ball_col_pos = 3
            ball_direction = RIGHT

            # Si golpea el centro del paddle, rebota con el mismo angulo de entrada, pero si golpea en los extremos, 
            # rebota con un angulo mayor (angulo de entrada +/- 15).        
            if int(ball_row_pos) in (p1_pos, p1_pos + 3):
                ball_angle = -ball_angle
            else:
                ball_angle = -ball_angle + (15 if ball_angle < 0 else -15)  

        else:
        
            # La bola ha salido por la izquierda, punto para el jugador 2
            p2_score += 1
            last_scorer = "P2"
            draw_score()
            reset_ball()

    if ball_col_pos > 99:

        # Detectamos si la bola ha chocado con el paddle del jugador 2
        if p2_pos <= int(ball_row_pos) <= p2_pos + 3:
            ball_col_pos = 99
            ball_direction = LEFT

            # Si golpea el centro del paddle, rebota con el mismo angulo de entrada, pero si golpea en los extremos, 
            # rebota con un angulo mayor (angulo de entrada +/- 15).        
            if int(ball_row_pos) in (p2_pos, p2_pos + 3):
                ball_angle = -ball_angle
            else:
                ball_angle = -ball_angle + (15 if ball_angle < 0 else -15)  

        else:
            # La bola ha salido por la derecha, punto para el jugador 1
            p1_score += 1
            last_scorer = "P1"
            draw_score()
            reset_ball()

    # Dibujamos la bola en su nueva posicion
    draw_ball()



def reset_ball():
    global ball_row_pos, ball_col_pos, ball_direction, ball_angle

    ball_angle = random.choice((-15,15,-30,30,-45,45))

    # Definimos de que lado sale la bola en funcion del ultimo anotador
    if last_scorer == "P1":
        ball_col_pos = 99
        ball_row_pos = p2_pos + 1
        ball_direction = LEFT
    else:
        ball_col_pos = 3
        ball_row_pos = p1_pos + 1
        ball_direction = RIGHT
    
    draw_ball()

    # Hacemos una breve pausa
    time.sleep(1)


def there_is_a_winner() -> bool:

    # Si nadie llego a 10, no hay ganador aun
    if p1_score < 10 and p2_score < 10:
        return False

    winner = "1" if p1_score == 10 else "2"    
    locate(18, 40); print(f"Player {winner} Wins!".center(20))

    return True


def main():

    # Hook para capturar eventos de teclado evitar que se muestren en pantalla
    #kb.hook(lambda e: None, suppress=True)  

    hide_cursor()
    cls()

    draw_border()
    draw_score()

    reset_ball()
    
    while True:
        if kb.is_pressed('a'):
            move_paddle(PADDLE_1, UP)

        if kb.is_pressed('z'):
            move_paddle(PADDLE_1, DOWN)

        if kb.is_pressed('k'):
            move_paddle(PADDLE_2, UP)

        if kb.is_pressed('m'):
            move_paddle(PADDLE_2, DOWN)

        if kb.is_pressed('esc'):
            break

        move_ball()

        time.sleep(0.06)

        if there_is_a_winner():
            break

    # Desconectar el hook de teclado
    #kb.unhook_all()  

    locate(35, 1); print("bye!")
    show_cursor()


main()


