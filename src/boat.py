import termio as t

def passengers_at_bank(river_bank):
    return ", ".join(river_bank)


def available_options(river_bank):

    options = []

    for passenger in river_bank:
        options.append(f"{passenger[0]}={passenger}")

    options.append("N=Nadie")

    return ", ".join(options)


def check_losing_condition(river_bank):

    if "Lobo" in river_bank and "Oveja" in river_bank:
        print("Perdiste. El Lobo se comio a la Oveja.")
        return True

    elif "Oveja" in river_bank and "Pasto" in river_bank:
        print("Perdiste. La Oveja se comio el Pasto.")
        return True

    return False


def check_winning_condition(river_bank):

    if {"Lobo", "Oveja", "Pasto"} == river_bank:
        print("Lo conseguiste!")
        return True

    return False

def main():

    passengers = {
        "L": "Lobo",
        "O": "Oveja",
        "P": "Pasto"
    }

    river_banks = [
        {'Lobo', 'Oveja', 'Pasto'},   # Orilla #1
        set()                         # Orilla #2
    ]
    
    current_bank = 0

    while True:
        t.cls()

        pab1 = passengers_at_bank(river_banks[0])
        pab2 = passengers_at_bank(river_banks[1])

        print(f"{'Orilla 1:':<30} Orilla 2:")
        print(f"{pab1:<30} {pab2}")
        
        print(f"\nEl barco esta en Onrilla {current_bank + 1}.")

        # Gano?
        if check_winning_condition(river_banks[1]):
            break

        # Perdio?
        prev_bank = 1 if current_bank == 0 else 0
        if check_losing_condition(river_banks[prev_bank]):
            break
        
        options = available_options(river_banks[current_bank])
        to_cross = input(f"A quien cruzamos? ({options}): ").upper()

        if current_bank == 0:
            dest_bank = 1
        else:
            dest_bank = 0
        
        if to_cross != 'N':
            river_banks[dest_bank].add(passengers[to_cross])
            river_banks[current_bank].discard(passengers[to_cross])
        
        current_bank = dest_bank


if __name__ == "__main__":
    main()


