import random

"""
def form_groups(names: list, size: int) -> list:
    unselected = list(names)
    group_count = len(names) // size + 1
    formed_groups = []

    for _ in range(1, group_count + 1):

        if size > len(unselected):
            size = len(unselected)

        formed_group = []

        for _ in range(size):
            chosen_one = random.choice(unselected)
            formed_group.append(chosen_one)
            unselected.remove(chosen_one)

        formed_groups.append(formed_group)

    return formed_groups    
"""
    
def form_groups(names: list, group_count: int) -> list:
    
    group_size = len(names) // group_count
    
    # No pueden haber grupos de menos de dos integrantes
    if group_size < 2:
        return []

    shuffled_names = names.copy()
    random.shuffle(shuffled_names)
    formed_groups = []

    # Primero acomodamos todos los que podamos en "group_count" grupos de tamaño "grupe_size"
    for _ in range(group_count):
        formed_group = []

        for _ in range(group_size):
            formed_group.append(shuffled_names.pop(0))
            
        formed_groups.append(formed_group)

    # Segundo, los que se quedaron sin grupo, los distribuimos uno a uno en los equipos creados
    for group in formed_groups:

        # Si ya no quedan mas para dsitribuir, terminamos
        if not shuffled_names:
            break

        group.append(shuffled_names.pop(0))

    return formed_groups


def main():
    names = ["Acosta", "Buendia", "Cornejo", "Davila", "Fernandez", 
             "Lopez", "Mesa", "Palomares", "Ruiz", "Yupanqui", "Zapata"]
    
    groups = form_groups(names, 3)
    
    for group in groups:
        print(group)


if __name__ == "__main__":
    main()

    