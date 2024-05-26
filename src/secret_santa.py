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
    names = ("Pepe", "Jorge", "Luis", "Manuel", "Luana", "Sofia", "Ana", "Raquel")
    friends = secret_santa(names)
    print(friends)
