import random

def secret_santa(names: list) -> dict:
    unmatched = list(names)
    friends = {}

    for name in names:
        chosen_one = random.choice([n for n in unmatched if n != name])
        friends[name] = chosen_one

        unmatched.remove(chosen_one)

    return friends


if __name__ == "__main__":

    print("Secret Santa\n")
    print("Escribe la lista de participantes para el sorteo, uno por línea.  Cuando termines, escribe 'listo'.")

    names = set()
    
    while True:
        name = input()
        if name == "listo":
            break
        names.add(name)

    pairs = secret_santa(names)

    print("\nLos amigos secretos son:\n")

    for pair in pairs:
        print(f"  - {pair} le regala a {pairs[pair]}")
    
