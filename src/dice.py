import random
import time

dice = {
    1: [
        "+-------+",
        "|       |",
        "|   O   |",
        "|       |",
        "+-------+" 
    ],
    2: [
        "+-------+",
        "|     O |",
        "|       |",
        "| O     |",
        "+-------+" 
    ],
    3: [
        "+-------+",
        "|     O |",
        "|   O   |",
        "| O     |",
        "+-------+" 
    ],
    4: [
        "+-------+",
        "| O   O |",
        "|       |",
        "| O   O |",
        "+-------+" 
    ],
    5: [
        "+-------+",
        "| O   O |",
        "|   O   |",
        "| O   O |",
        "+-------+" 
    ],
    6: [
        "+-------+",
        "| O O O |",
        "|       |",
        "| O O O |",
        "+-------+" 
    ]
}

def print_dice(args: list):

    for row in range(5):
        for arg in args:
            print(dice[arg][row], end=" ")
        print("")


def roll_dice(count):

    result = []

    for _ in range(count):
        n = random.randint(1,6)
        result.append(n)
    
    return result

def print_results(juego):

    print("\nResultados:\n")

    for player, results in juego.items():
        if results["caparazon"]:
            print(f"El jugador #{player} consiguio 1 caparazon y {results['patas']} patas.")
        else:
            print(f"El jugador #{player} no consiguo formar nada.")



def play():
    players = int(input("Cuantos jugadores? "))

    juego = {}
        
    for player in range(1, players + 1):

        cont = input(f"\nVamos a jugar ahora con el jugador #{player}. Continuar (S/n)? ")
        if cont == "n":
            print("Juego abortado.")
            return

        turnos = 3
        caparazon = False
        patas = 0

        for turno in range(1, turnos + 1):
            time.sleep(0.5)

            print(f"\nJugador #{player}, turno #{turno}:")
            r = roll_dice(5)
            print_dice(r)

            # Consiguio caparazon?
            if 6 in r:
                caparazon = True
            
            # Solo si ya consiguio caparazon, podemos contabilizar las patas (max 4)
            if caparazon and patas < 4:
                patas += r.count(1)

        juego[player] = {
            "caparazon": caparazon,
            "patas": patas
        }

    print_results(juego)


if __name__ == "__main__":
    play()


