import random

HORIZONTAL = 0
VERTICAL = 1
BOARD_SIZE = 20

board = []


def initialize_board():
    """
    Inicializa el board con espacios en blanco
    """
    global board
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board():
    for line in board:
        for letter in line:
            print(letter.upper(), end = " ")
        print()


def check_word(word, row, col, direction):
    """ 
    Verifica que la palabra en cuestion pueda ser ingresada en la posicion y direccion 
    indicadas sin entrar en conflicto con otra palanbra existente
    """
    for letter in word:
        if board[row][col] not in (" ", letter):
            return False

        if direction == HORIZONTAL:
            col += 1
        else:
            row += 1

    return True


def put_word(word):
    """
    Agrega una nueva palabra al tablero
    """
    global board

    if len(word) > BOARD_SIZE:
        return

    tries = 0

    while tries < 20:

        direction = random.randint(0, 1)  # 0: Horizontal,  1: Vertical
        row = random.randint(0, BOARD_SIZE - (1 if direction == HORIZONTAL else len(word)))
        col = random.randint(0, BOARD_SIZE - (1 if direction == VERTICAL else len(word)))

        if check_word(word, row, col, direction):
            # Se confirma que si hay espacio, salimos de aqui y continuamos
            break

        tries += 1

    else:
        # Despues de 10 intentos no se logró encontrar sitio para la palabra
        return

    for letter in word:
        board[row][col] = letter
    
        if direction == HORIZONTAL:
            col += 1
        else:
            row += 1 


def complete_board():
    """
    Rellena los espacios en blanco que quedan en el tablaro luego de haber colocado 
    todas las palabras
    """
    global board

    for row in range(0, BOARD_SIZE):
        for col in range(0, BOARD_SIZE):
            if board[row][col] == " ":
                board[row][col] = random.choice("abcdefghijklmnopqrstuvwxyz")


def main():

    initialize_board()

    put_word("arandano")
    put_word("maracuya")
    put_word("granadilla")
    put_word("uva")
    put_word("fresa")
    put_word("papaya")
    put_word("platano")
    put_word("naranja")

    complete_board()

    print_board()


main()