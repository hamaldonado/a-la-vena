from datetime import datetime
import time
import msvcrt               # Esto sólo funciona en Windows
import termio as t

numeros = {
    "0": [
        " ### ",
        "#  ##",
        "# # #",
        "##  #",
        " ### " 
    ],
    "1": [
        "   # ",
        " # # ",
        "   # ",
        "   # ",
        "   # "
    ],
    "2": [
        "#### ", 
        "    #",
        " ### ",
        "#    ", 
        "#####"
    ],
    "3": [
        "#### ",
        "    #",
        " ### ",
        "    #",
        "#### "
    ],
    "4": [
        " #  #",
        "#   #",
        "#####",
        "    #",
        "    #"
    ],
    "5": [
        "#####",
        "#    ",
        "#### ",
        "    #",
        "#### "
    ],
    "6": [
        " ### ",
        "#    ",
        "#### ",
        "#   #",
        " ### "
    ],
    "7": [
        "#####",
        "    #",   
        "  #  ",
        "  #  ",
        "  #  "
    ],
    "8": [
        " ### ",
        "#   #",
        " ### ",
        "#   #",
        " ### "
    ],
    "9": [
        " ### ",
        "#   #",
        " ####",
        "    #",
        " ### "
    ],
    ":": [
        "    ",
        " ## ",
        "    ",
        " ## ",
        "    "
    ],
    "/": [
        "     ",
        "   # ",
        "  #  ",
        " #   ",
        "     "
    ],
    " ": [
        "    ",
        "    ",
        "    ",
        "    ",
        "    "
    ]
}


def print_clock(value: str):

    for linea in range(0, 5):
        for number in value:
            print(numeros[number][linea], end="", flush=True)
            print("  ", end="", flush=True)
        print("")

    # Mover cursor 6 lineas hacia arriba
    t.move_up(6)


def main():

    # Limpiar pantalla
    t.cls()

    t.hide_cursor()  # Ocultar Cursor
   
    while True:
        hora = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")
        print_clock(hora)

        time.sleep(1)

        if msvcrt.kbhit():         # Esto solo funciona en windows
            t.cls()
            t.show_cursor()
            break

    t.show_cursor()

if __name__ == "__main__":
    main()

    