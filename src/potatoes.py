def main():
    print("Vamos a resolver el enigma de las papas..")

    papas = input("Cuantas papas hay que repartir? ")
    personas = input("Entre cuantas personas? ")

    num_papas = int(papas)
    num_personas = int(personas)

    if num_papas % num_personas == 0:
        reparte = int(num_papas / num_personas)
        print(f"Está fácil!  A cada persona le corresponde {reparte} papas.")
    else:
        print("No te compliques!  Haz puré y asunto resuelto.")


if __name__ == "__main__":
    main()