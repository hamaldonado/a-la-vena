import random
import termio

HANG = (
    r"""
    +----+
    |
    |
    |
    |
    |
    """,
    r"""
    +----+
    |    |
    |    
    |   
    |   
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |   
    |   
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |    |
    |   
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |   /|
    |   
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |   /|\
    |   
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |   /|\
    |   / 
    |
    """,
    r"""
    +----+
    |    |
    |    O
    |   /|\
    |   / \
    |
    """
)

def load_words() -> list:
    words = []

    with open("Data/paises_de_america.txt") as f:
        
        while line := f.readline():
            word = line.split(",")[0].strip()

            words.append(word)

    return words            


def reveal(word: str, guessed_letters: set) -> bool:

    """ 
    Revela la palabra letra x letra.  Devuelve True si todas las letras 
    fueron reveladas, False caso contrario 
    """

    all_revealed = True

    for letter in word:
        if letter in guessed_letters:
            print(f"{letter} ", end="")
        else:
            print(f"_ ", end="")
            all_revealed = False

    print("")

    return all_revealed


def main():
    
    words = load_words()
    tries = 0

    word = random.choice(words)
    guessed_letters = set(" ")

    while True:

        # Limpiamos la pantalla
        termio.cls()

        print(HANG[tries])
        all_revealed = reveal(word, guessed_letters)

        # Condicion de victoria
        if all_revealed:
            print("\nGanaste!!")
            break

        # Condicion de derrota
        if tries == 7:
            print(f"\nPerdiste!!.  La palabra era {word}.")
            break

        letter = input(
            "\n Dame una letra (escribe 'salir' para terminar) -> ").upper()

        if letter == "SALIR":
            print("\nBye!")
            break
        
        elif letter in word:
            guessed_letters.add(letter)
            continue
        
        else: # letra incorrecta
            tries += 1


if __name__ == "__main__":
    main()
