#
# AL OESTE DE TOBRUK
#   ____
# _| °|__
# \OOOOO/
# ^^^^^^^^^^^^^^^^^^
#

import time
import random
import math
from termio import cls, locate

TANK = [
        "  ____ ",
        "_| °|__",
        "\OOOOO/"
    ]

EXPLOSION = [
    "       ",
    " \ | / ",
    "  -+-  "
    ]

TOBRUK = [
    "   \\  ",
    " _\\ \\_ ",
    "/TOBRUK\\"
]

def draw_scenery():
    cls()
    
    # Titulo
    locate(1, 1); print("AL OESTE DE TOBRUK".center(120))
    
    # Terreno
    locate(24, 1); print("^"*120)

    # Tobruk
    locate(21, 113); print(TOBRUK[0])
    locate(22, 113); print(TOBRUK[1])
    locate(23, 113); print(TOBRUK[2])


def draw_tank(column):
    locate(21, column); print(TANK[0])
    locate(22, column); print(TANK[1])
    locate(23, column); print(TANK[2])


def erase_tank(column):
    s = " "*7

    locate(21, column); print(s)
    locate(22, column); print(s)
    locate(23, column); print(s)


def explode_tank(column):

    locate(21, column); print(EXPLOSION[0])
    locate(22, column); print(EXPLOSION[1])
    locate(23, column); print(EXPLOSION[2])


def end_game(msg):
    locate (12, 55)
    print(msg)


def set_tank(available_tanks):
    draw_tank(1)
    
    locate(25, 1); print(f"TANQUES RESTANTES: {available_tanks:02}")
    

def advance_tank(current_position):
    
    steps = random.randint(3, 7)
    new_position = current_position + steps
    
    erase_tank(current_position)
    draw_tank(new_position)
    
    return new_position


def load_bullet(available_bullets):
    locate(22, 116); print("°")
    locate(25, 102); print(f"BALAS RESTANTES: {available_bullets - 1:02}")
    
    return available_bullets - 1
    

def ask_parameters():
    s = " " * 15
    locate(2,1); print(s)
    locate(3,1); print(s)
    
    locate(2,1); angle = float(input("Angulo:"))
    locate(3,1); velocity = float(input("Velocidad:"))

    return angle, velocity


def fire(velocity: float, angle: float):

    radians = angle * ( math.pi / 180.0 )
    v_x = velocity * math.cos(radians)
    v_y = velocity * math.sin(radians)

    # posicion inicial de la bala
    start_x = pos_x = 116
    start_y = pos_y = 22

    t = 0

    while True: 
        # Borramos la bala de la posicion anterior
        locate(pos_y, pos_x)
        print(" ")

        # Calculamos la nueva posición de la bala
        h = int(v_y * t - 0.5*(9.8)*(t**2))
        d = int(v_x * t)

        pos_y = start_y - h
        pos_x = start_x - d 
        
        locate(pos_y, pos_x)
        print("°")
        
        time.sleep(0.1)

        t+=0.1

        # Si la saca del estadio, la cortamos
        if pos_x <= 0 or pos_y <= 0:
            return -1

        # Si llegó a tierra, devolvemos la posicion en la que cayó 
        if pos_y >= 23:
            return pos_x


def main():

    available_bullets = 10
    available_tanks = 3
    tank_current_position = 1
   
    draw_scenery()
    
    # Ponemos el primer tanque en posicion
    set_tank(available_tanks)

    while True:
            
        # Le quedan balas? 
        if available_bullets > 0:
            
            # Tobruk dispara
            available_bullets = load_bullet(available_bullets)
            angle, velocity = ask_parameters()
            bullet_position = fire(velocity, angle)
        
            # Mata al tanque?
            if tank_current_position < bullet_position < tank_current_position + 7:

                # Explota el tanque y desaparece
                explode_tank(tank_current_position)
                time.sleep(0.5)
                erase_tank(tank_current_position)
                available_tanks -= 1 

                # Quedan tanques disponibles?
                if available_tanks == 0:
                    end_game(" GANASTE!")
                    locate(26,1)
                    return
                
                # Instalamos un nuevo tanque en la posicion inicial y volvemos a empezar
                set_tank(available_tanks)
                tank_current_position = 1
                continue

        # Avanza el tanque hacia Tobruk
        tank_current_position = advance_tank(tank_current_position)
        time.sleep(0.2)

        # Llegó el tanque a Tobruk?
        if tank_current_position >= 112:
            end_game("GAME OVER!")
            locate(26,1)
            return

        # Fin del turno



"""
Por cada turno:
- Le quedan balas a TOBRUK?
    - NO:
        - Tanque avanza hasta TOBRUK
        - PIERDE EL JUEGO
- Tobruk Dispara
- Mata al tanque?
    - SI:
        - Hay mas tanques?
            - NO:
                GANA EL JUEGO
            - SI:
                Borra el tanque destruido
                Saca un Tanque nuevo y ponlo al inicio
    - NO:
        Avanza el Tanque
- El Tanque llego a TOBRUK?
    - SI:
        PIERDE EL JUEGO
    - NO:
        Fin del Turno


"""
main()



