import random

def generate_password(length=8):

    pool = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "@#$%&!"
    ]

    chars = []
    t = 0

    for _ in range(length):
        chosen_char = random.choice(pool[t])
        chars.append(chosen_char)

        if t == 3:
            t = 0
        else:
            t += 1 

    random.shuffle(chars)

    return "".join(chars)


if __name__ == "__main__":
    l = int(input("¿De qué tamaño generamos la clave? -> "))
    
    p = generate_password(l)

    print(f"La clave generada es: {p}")




    

    

    



