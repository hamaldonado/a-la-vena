import time
import playsound

CLEAR_SCREEN = "\033c"
REVERSE_RED = "\033[31;7m"
NORMAL = "\033[0m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

def start_bomb(seconds):

    color = NORMAL

    # Ocultar Cursor
    print(HIDE_CURSOR)  

    while seconds >= 0:

        min = seconds // 60
        sec = seconds % 60

        display = f"{min}:{sec:02}"

        if seconds <= 5:
            color = REVERSE_RED
        
        playsound.playsound(u"src/sounds/tick_01.wav", block=False)

        print(f"\r{color}La bomba detonará en {display}", end="", flush=True)

        seconds -= 1

        time.sleep(1)
    
    # Reset de color y muestra cursor
    print(NORMAL, SHOW_CURSOR)  

    # Estalla la bomba
    print("\nBOOM!")
    playsound.playsound(u"src/sounds/explosion_01.mp3")


def main():

    # Limpiar pantalla
    print(CLEAR_SCREEN)

    duration = input("Ingresa la duracion en formato mm:ss -> ")

    s_min, s_sec = duration.split(":")

    seconds = int(s_min) * 60 + int(s_sec)

    start_bomb(seconds)
   

if __name__ == "__main__":
    main()

    