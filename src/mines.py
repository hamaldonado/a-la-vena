import random
import kbhit
import termio as t
import time
from termio import Color, Attr

SCREEN_HEIGHT = 10
SCREEN_WIDTH = 20
MINES_COUNT = 20

back = []
front = []

def prepare_back():

    global back
    
    # Generamos los espacion
    for _ in range(SCREEN_HEIGHT):
        back.append(list(' ' * SCREEN_WIDTH))


    # Sembramos las bombas
    for _ in range(MINES_COUNT):
        bomb_row = random.randint(0, SCREEN_HEIGHT - 1)
        bomb_col = random.randint(0, SCREEN_WIDTH - 1)
        back[bomb_row][bomb_col] = "x"
    
    # Ponemos las marcas alrededor de las bombas

    # 'x', ' ' ,' '  
    # 'x', '3' ,' '
    # ' ', ' ' ,'x'

    for row in range(SCREEN_HEIGHT):
        for col in range(SCREEN_WIDTH):

            if back[row][col] == ' ':

                near_bombs = 0

                if row > 0 and col > 0 and back[row - 1][col - 1] == 'x':
                    near_bombs += 1

                if row > 0 and back[row - 1][col] == 'x':
                    near_bombs += 1

                if row > 0 and col < SCREEN_WIDTH -1 and back[row - 1][col + 1] == 'x':
                    near_bombs += 1

                if col > 0 and back[row][col - 1] == 'x':
                    near_bombs += 1

                if col < SCREEN_WIDTH -1 and back[row][col + 1] == 'x':
                    near_bombs += 1

                if row < SCREEN_HEIGHT - 1 and col > 0 and back[row + 1][col - 1] == 'x':
                    near_bombs += 1

                if row < SCREEN_HEIGHT - 1 and back[row + 1][col] == 'x':
                    near_bombs += 1

                if row < SCREEN_HEIGHT -1 and col < SCREEN_WIDTH - 1 and back[row + 1][col + 1] == 'x':
                    near_bombs += 1

                if near_bombs > 0:
                    back[row][col] = str(near_bombs)


def prepare_front():

    global front
    
    # Generamos los espacion
    for _ in range(SCREEN_HEIGHT):
        front.append(list('#' * SCREEN_WIDTH))


def draw_front():

    t.locate(1, 1)
    
    print(f"{'+---' * SCREEN_WIDTH}+")

    for row in range(SCREEN_HEIGHT):
        for col in range(SCREEN_WIDTH):

            match front[row][col]:

                case '1':
                    cell_value = f"{Color.F_BLUE}{front[row][col]}{Color.F_DEFAULT}" 
                
                case '2':
                    cell_value = f"{Color.F_GREEN}{front[row][col]}{Color.F_DEFAULT}" 

                case '3':
                    cell_value = f"{Color.F_YELLOW}{front[row][col]}{Color.F_DEFAULT}" 

                case '4':
                    cell_value = f"{Color.F_MAGENTA}{front[row][col]}{Color.F_DEFAULT}" 

                case '5':
                    cell_value = f"{Color.F_RED}{front[row][col]}{Color.F_DEFAULT}" 

                case 'F':
                    cell_value = f"{Color.B_CYAN}{front[row][col]}{Color.NORMAL}" 

                case 'x':
                    cell_value = f"{Color.B_RED}{front[row][col]}{Color.B_DEFAULT}"

                case _:
                    cell_value = f"{front[row][col]}"

            print(f"| {cell_value} ", end="")
        
        print("|")

        print(f"{'+---' * SCREEN_WIDTH}+")


def select(row, col):

    """
    Cols:
    0 -> 3    = 3 + 4 * 0
    1 -> 7    = 3 + 4 * 1
    2 -> 11   = 3 + 4 * 2
    3 -> 15   = 3 + 4 * 3
    
    n -> 3 + 4 * n

    
    Rows:
    0 -> 2   = 2 + 2 * 0  
    1 -> 4   = 2 + 2 * 1
    2 -> 6   = 2 + 2 * 2
    3 -> 8   = 2 + 2 * 3
    
    n -> 2 + 2 * n

    """
    
    r = 2 + 2 * row
    c = 3 + 4 * col

    t.locate(r, c - 1); print(f"{Attr.BOLD}{Color.F_CYAN}[{Color.F_DEFAULT}{Attr.BOLD_OFF}")
    t.locate(r, c + 1); print(f"{Attr.BOLD}{Color.F_CYAN}]{Color.F_DEFAULT}{Attr.BOLD_OFF}")  


def unselect(row, col):

    r = 2 + 2 * row
    c = 3 + 4 * col

    t.locate(r, c - 1); print(f" ")
    t.locate(r, c + 1); print(f" ")  


def flag(row, col):
    
    global front

    # Solo podemos flaguear una celda aun no revelada o previamente flagueda
    if front[row][col] not in ("#", "F"):
        return

    # Verificamos si ya tiene flag.  Si no tiene, le ponemos de lo contraio
    # lo quitamos
    if front[row][col] == "#":
        front[row][col] = "F"
    else:
        front[row][col] = "#"

    draw_front()


def reveal(row, col):
    
    global front

    # Solo podemos revelar una celda aun no revelada
    if front[row][col] != "#":
        return

    # Revelamos la celda, obteniendo el dato de back
    front[row][col] = back[row][col]

    draw_front()

    # Piso mina?
    if front[row][col] == 'x':
        return "lose"

    # Gano? 
    if check_winning_condition():
        return "win"
    
    return "keep_playing"
    

def check_winning_condition():
    # El jugador gana si no hay mas celdas que revelar y todas las F 
    # se corresponden exactamente 1-a-1 con las bombas 

    # Contamos cuantas celdas faltan revelar y cuantas se han flageado
    pending_cells_count = 0
    flags_count = 0

    for row in front:
        pending_cells_count += row.count('#')
        flags_count += row.count('F')

    if pending_cells_count == 0 and flags_count == MINES_COUNT:
        return True
    
    return False

def main():
    global front

    prepare_back()
    prepare_front()
    
    t.cls()
    draw_front()

    kb = kbhit.KBHit()

    selected_row = 0
    selected_col = 0
    select(selected_row, selected_col)

    while True:

        if kb.kbhit():

            c = kb.getarrow()

            match c:
                case 0: # UP
                    if selected_row > 0:
                        unselect(selected_row, selected_col)
                        select(selected_row - 1, selected_col)
                        selected_row = selected_row - 1
                
                case 1: # RIGHT
                    if selected_col < SCREEN_WIDTH - 1:
                        unselect(selected_row, selected_col)
                        select(selected_row, selected_col + 1)
                        selected_col = selected_col + 1

                case 2: # DOWN
                    if selected_row < SCREEN_HEIGHT - 1:
                        unselect(selected_row, selected_col)
                        select(selected_row + 1, selected_col)
                        selected_row = selected_row + 1
                
                case 3: # LEFT
                    if selected_col > 0:
                        unselect(selected_row, selected_col)
                        select(selected_row, selected_col - 1)
                        selected_col = selected_col - 1

                case 102: # F: Flag
                    flag(selected_row, selected_col)
                    select(selected_row, selected_col)
                    

                case 114: # R: Reveal
                    r = reveal(selected_row, selected_col)
                    select(selected_row, selected_col)

                    if r == "win":
                        t.locate(SCREEN_HEIGHT * 2 + 2, 1); print("GANASTE!")
                        break

                    elif r == "lose":
                        t.locate(SCREEN_HEIGHT * 2 + 2, 1); print("PERDISTE!")
                        break

        time.sleep(0.1)

main()

