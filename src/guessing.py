import random


def main():
    chosen_one = random.randint(1, 15)
    intentos = 4

    print("Dime un número entre 1 y 15.  Si adivinas, te ganas una Oreo.") 

    while True:

        # Condicion de derrota
        if intentos == 0:
            print(f"Perdiste!  El número era {chosen_one}.")
            break

        n = int(input(f"Te quedan {intentos} intentos -> "))

        # Condicion de victoria
        if n == chosen_one:
            print("Ese es! Ganaste!!")
            break

        if n < chosen_one:
            print("Frío frío.. ese número es muy pequeño")
            intentos -= 1

        elif n > chosen_one:
            print("Frío frío.. ese número es muy grande")
            intentos -= 1


if __name__ == "__main__":
    main()

