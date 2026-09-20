import math

def es_primo(number: int) -> bool:
    x = 2
    t = int(math.sqrt(number) + 1)

    while x < t:
        if number % x == 0:
            return False
    
        x+=1

    else:
        return True


for i in range(1, 30):
    if es_primo(i):
        print(f"{i} SI es primo.")
    else:
        print(f"{i} NO es primo.")



            