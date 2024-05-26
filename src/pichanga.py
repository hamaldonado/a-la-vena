def pichanga(names: dict) -> dict:
    
    players = list(names)
    players.sort(key = lambda name : names[name], reverse=True)

    equipo_1 = []
    equipo_2 = []

    for i, player in enumerate(players):
        if i % 2 == 0:
            equipo_1.append(player)
        else:
            equipo_2.append(player)
    
    teams = {
        "Equipo 1": equipo_1,
        "Equipo 2": equipo_2
    }

    return teams


def main():

    names = {
        "Pepe": 10, 
        "Jorge": 5,
        "Luis": 2, 
        "Manuel": 10, 
        "Luana": 7, 
        "Sofia": 8, 
        "Ana": 1, 
        "Raquel": 5
        }

    groups = pichanga(names)
    print(groups)


if __name__ == "__main__":
    main()
