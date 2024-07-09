import time
import playsound
import termio as t
from termio import Color

def start_bomb(seconds):

    color = Color.NORMAL

    # Ocultar Cursor
    t.hide_cursor()

    while seconds >= 0:

        min = seconds // 60
        sec = seconds % 60

        display = f"{min}:{sec:02}"

        if seconds <= 5:
            color = Color.B_RED + Color.F_BRIGHT_WHITE
        
        playsound.playsound(u"src/sounds/tick_01.wav", block=False)

        print(f"\r{color}La bomba detonará en {display}", end="", flush=True)

        seconds -= 1

        time.sleep(1)
    
    # Reset de color y muestra cursor
    print(Color.NORMAL)
    t.show_cursor()  

    # Estalla la bomba
    print("\nBOOM!")
    playsound.playsound(u"src/sounds/explosion_01.mp3")


def main():

    # Limpiar pantalla
    t.cls()

    duration = input("Ingresa la duracion en formato mm:ss -> ")

    s_min, s_sec = duration.split(":")

    seconds = int(s_min) * 60 + int(s_sec)

    start_bomb(seconds)
   

if __name__ == "__main__":
    main()

    