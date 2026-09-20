
signos= [".", ",", ";", "!" "?"]
excluir={"they", "this", "that", "them", "those", "were", "didn't", "been", 
         "have", "from", "with", "there", "their", "into", "what", "when", 
         "your", "could", "very", "up", "down", "just", "over", "then"}

palabras_dict = {}
counter = 0

with open("data/harry.txt") as f:

    while True:
        linea = f.readline()

        # Se acabo el archivo
        if not linea:
            break

        # Quitamos puntuaciones
        for signo in signos:
            linea = linea.replace(signo, "")
        
        palabras = linea.strip().split(" ")

        for palabra in palabras:
            p = palabra.strip().lower()
            counter += 1

            if len(palabra) < 4 or palabra in excluir:
                continue

            palabras_dict[p] = palabras_dict.get(p, 0) + 1

            

    print(f"Se encontraron {counter} palabras, de las cuales {len(palabras_dict)} son palabras unicas.")
    
    l = list(palabras_dict.items())

    l.sort(key=lambda x: x[1], reverse=True)

    print("\nLas 20 palabras mas comunes son:")

    for pal, cant in l[:20]:
        print(f" - {pal} se encontro {cant} veces.")


