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


def update_spiders(spiders):
    
    # Actualizamos la posicion de las aranas
    for i in range(10):
        spiders[i] += random.randint(0,1)

        if spiders[i] >= 21:
            spiders[i] = 21
    
    # Dibujamos las aranas en las nuevas posiciones    
    for spider, steps in enumerate(spiders):

        # las spiders 0,1,2.. van en las columnas 5,10,15..
        column = (spider + 1) * 5

         # Baja
        row = 3    
        while row < steps:
            t.locate(row, column)
            print("|", end="", flush=True)
            row += 1

        t.locate(row, column)
        print("M", end="", flush=True)


def check_losing_condition(spiders, person_pos):

    # Spider mas proxima al suelo
    closest_spider_row = max(spiders)
    
    # Ubicamos las columnas donde se encuentra la spider mas proxima al suelo
    # En caso haya mas de una, ponemos en la lista todas las coincidencias    
    closest_spider_columns = []
    for i, spider in enumerate(spiders):
        if spider == closest_spider_row:
            closest_spider_columns.append((i + 1) * 5)

    # Si alguna spider llego a bajar hasta la fila 21, pierde
    if closest_spider_row == 21:
        return True

    # Si alguna llego a bajar hasta la fila 20, y esta en la misma columna
    # que la persona, pierde (le cae la spider en la cara o manos)
    if closest_spider_row == 20 \
        and ( 
            (person_pos) in closest_spider_columns \
            or (person_pos + 1) in closest_spider_columns \
            or (person_pos + 2) in closest_spider_columns ):
        return True
    
    return False


def main():

    spiders = [2] * 10
    sprays = [-1] * 50
    person_pos = 24
    tick = 0
    
    draw_scenary()
    draw_person(person_pos)
    
    kb = kbhit.KBHit()

    while True:
        
        if tick == 10:
            update_spiders(spiders)
            #update_sprays()
            
            lost = check_losing_condition(spiders, person_pos)

            if lost:
                break
            tick = 0

        if kb.kbhit():
            c = kb.getarrow()

            match c:
                case 1: 
                    person_pos = move_person(person_pos, RIGHT)
                case 3: 
                    person_pos = move_person(person_pos, LEFT)
        
        tick +=1
        time.sleep(0.05)

    kb.set_normal_term()
        

main()