from datetime import datetime
import time

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
    print("\033[6A")


def main():

    # Limpiar pantalla
    print("\033c")

    print("\033[?25l")  # Ocultar Cursor
    #print("\033[?25h")  # Mostrar Cursor

    while True:
        hora = datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")

        print_clock(hora)

        time.sleep(1)


if __name__ == "__main__":
    main()

    