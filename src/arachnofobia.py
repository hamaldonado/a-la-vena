import random
import time
import termio as t
import kbhit

PERSON = [
    "_°/",
    " Ω "
]

SPRAY = "░"
RIGHT = 1
LEFT = -1


def draw_scenary():
    ceiling = "----+" * 10
    floor = "^" * 50

    t.cls()
    t.locate(1,1); print("A R A C H N O F O B I A".center(50))
    t.locate(2,1); print(ceiling)
    t.locate(22,1); print(floor)


def draw_person(position):
    t.locate(20,position); print(PERSON[0], end="", flush=True)
    t.locate(21,position); print(PERSON[1], end="", flush=True)


def erase_person(position):
    t.locate(20,position); print("   ", end="", flush=True)
    t.locate(21,position); print("   ", end="", flush=True)


def move_person(current_position, direction):
    
    if (direction == LEFT and current_position == 1) \
        or (direction == RIGHT and current_position == 49):
        return current_position

    new_position = current_position + direction

    erase_person(current_position)
    draw_person(new_position)

    return new_position


def apply_spray(spray, person_hpos):
    
    # Verificamos que no haya un spray ya lanzado.  Si ya hay uno devolvemos ese
    if spray != (-1, -1):
        return spray

    column = person_hpos + 2
    row = 19

    # dibujamos el spray en la posicion inicial (arriba de la mano derecha de la persona)
    t.locate(row, column); print(SPRAY, end="", flush=True)

    # devolvemos la posicion inicial del spray
    return (row, column)


def update_spray(spray, spiders_vpos):

    # Si no hay spray lanzado no hacemos nada
    if spray == (-1, -1):
        return (-1, -1)

    # Actualizamos la posicion del spray
    row, column = spray
    new_row = row - 1

    # Dibujamos el spray en su nueva posicion
    t.locate(row, column); print(" ", end="", flush=True)
    t.locate(new_row, column); print(SPRAY, end="", flush=True)

    # Colisiona con una arana?  Se libera el spray
    if check_colission(spray, spiders_vpos):
        t.locate(new_row, column); print(" ", end="", flush=True)
        return (-1, -1)

    # Alcanzo la fila 9 sin colisionar con alguna arana.  Se pierde el spray
    if new_row == 8:
        t.locate(new_row, column); print(" ", end="", flush=True)
        return (-1, -1)

    # Devolvemos la nueva posicion del spray
    return (new_row, column)


def update_spiders(spiders_vpos):
    
    # Actualizamos la posicion de las aranas
    for i in range(10):

        # ignoramos las aranas muertas
        if spiders_vpos[i] == -1:
            continue

        spiders_vpos[i] += random.randint(0,1)

        if spiders_vpos[i] >= 21:
            spiders_vpos[i] = 21
    
    # Dibujamos las aranas en las nuevas posiciones    
    for spider_index, spider_vpos in enumerate(spiders_vpos):

        # ignoramos las aranas muertas
        if spider_vpos == -1:
            continue

        # las spiders 0,1,2.. van en las columnas 5,10,15..
        spider_hpos = (spider_index + 1) * 5

        if spider_vpos > 3:
            t.locate(spider_vpos - 1, spider_hpos)
            print("|", end="", flush=True)
            
            t.locate(spider_vpos, spider_hpos)
            print("M", end="", flush=True)


def check_colission(spray, spiders_vpos):

    spray_vpos, spray_hpos = spray

    # El spray coincide con la columna de alguna spider?
    if spray_hpos % 5 == 0:

        spider_index = int(spray_hpos / 5) - 1 

        # El spray coincide con la fila de arana en la columna
        if spiders_vpos[spider_index] >= spray_vpos:

            # 1. Matamos la arana.  Primero la borramos de la pantalla
            for r in range(spiders_vpos[spider_index], 2, -1):
                t.locate(r, spray_hpos); print(" ", end="", flush=True)
            
            # 2. Asignamos el valor de la fila (vpos) a -1 para representar
            # la arana muerta
            spiders_vpos[spider_index] = -1

            # 3. Liberamos el spray
            return True

    return False


def check_winning_condition(spiders_vpos):

    for position in spiders_vpos:
        if position != -1:
            return False
    
    return True


def check_losing_condition(spiders_vpos, person_hpos):

    # Spider mas proxima al suelo
    closest_spider_vpos = max(spiders_vpos)
    
    # Ubicamos las columnas(hpos) donde se encuentra(n) la(s) spider(s) mas 
    # proxima(s) al suelo, es decir, la(s) spider(s) con el mayor numero 
    # de fila (vpos).  En caso haya mas de una, ponemos en la lista todas las 
    # coincidencias    
    closest_spider_hpos = []
    for i, spider_vpos in enumerate(spiders_vpos):
        if spider_vpos == closest_spider_vpos:
            closest_spider_hpos.append((i + 1) * 5)

    # Si alguna spider llego a bajar hasta la fila 21, pierde
    if closest_spider_vpos == 21:
        return True

    # Si alguna llego a bajar hasta la fila 20, y esta en la misma columna (hpos)
    # que la persona, pierde (le cae la spider en la cara o manos)
    if closest_spider_vpos == 20 \
        and ( 
            (person_hpos) in closest_spider_hpos \
            or (person_hpos + 1) in closest_spider_hpos \
            or (person_hpos + 2) in closest_spider_hpos ):
        return True
    
    return False


def main():

    t.hide_cursor()
    
    spiders_vpos = [2] * 10
    person_hpos = 24
    spray = (-1, -1)   # column, row del spray. Si es -1 no hay spray lanzado. 
    
    tick = 0
    
    draw_scenary()
    draw_person(person_hpos)
    
    kb = kbhit.KBHit()

    while True:
        
        if tick % 20 == 0:
            spray = update_spray(spray, spiders_vpos)
           

        if tick == 100:
            update_spiders(spiders_vpos)
                       
            lost = check_losing_condition(spiders_vpos, person_hpos)

            if lost:
                t.locate(12,1); print("GAME OVER".center(50, " "))
                break


            win = check_winning_condition(spiders_vpos)
            if win:
                t.locate(12,1); print("YOU WIN!".center(50, " "))
                break

            tick = 0
       

        if kb.kbhit():
            c = kb.getarrow()

            match c:
                case 0:
                    spray = apply_spray(spray, person_hpos)
                case 1: 
                    person_hpos = move_person(person_hpos, RIGHT)
                case 3: 
                    person_hpos = move_person(person_hpos, LEFT)
        
        tick +=1
        time.sleep(0.01)


    t.locate(25,1)
    kb.set_normal_term()
    t.show_cursor()  

main()