
def dar_vuelto(n: float):

    monedas = [5,2,1,0.5,0.2,0.1]
    vuelto = []

    restante = n
    
    """
    restante = n = 8.50 

    moneda_actual   cant_moneda_actual   restante 
    ---------------------------------------------
    5               1                    3.50
    2               1                    1.50
    1               1                    0.5
    0.5             1                    0

    """

    while monedas:
        moneda_actual = monedas.pop(0)

        cant_moneda_actual = int(restante / moneda_actual)
        restante = round(restante % moneda_actual, 1)
        
        vuelto.append(cant_moneda_actual)
        moneda_actual += 1
        
    return vuelto


if __name__ == "__main__":
    
    n = input ("¿Cuál es el vuelto? ")

    vuelto = dar_vuelto(float(n))

    print("Debes dar:")
    print(f"{vuelto[0]} moneda de 5 soles.")
    print(f"{vuelto[1]} moneda de 2 soles.")
    print(f"{vuelto[2]} moneda de 1 sol.")
    print(f"{vuelto[3]} moneda de 50 centimos.")
    print(f"{vuelto[4]} moneda de 20 centimos.")
    print(f"{vuelto[5]} moneda de 10 centimos.")

