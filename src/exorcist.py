import time

#texto = "merrin ayudanos sacanos de aqui merrin tengo miedo no los quiero ver merrin no lo soporto mas merrin"
#print(texto[::-1])

def reveal(text: str):
    fin = len(text) - 1

    for i in range(fin, -1, -1):
        print(text[i], end="", flush=True)
        time.sleep(0.2)

    print()


def main():
    texto = "nirrem sam otropos ol on nirrem rev oreiuq sol on odeim ognet nirrem iuqa ed sonacas sonaduya nirrem"
    reveal(texto)


if __name__ == "__main__":
    main()