import termio as t
import time
import msvcrt

def marquee(text):
    t.cls()
    t.hide_cursor()

    column_limit = 202
    row_limit = 60

    column = column_limit - len(text)

    while True:

        marquee_head = text + " "
        marquee_tail = ""

        if column_limit - column < len(text):
            marquee_head = text[ :column_limit - column]
            marquee_tail = text[column_limit - column + 1 : ] + " "
        
        t.locate(30, column); print(marquee_head, end="", flush=True)
        t.locate(30, 1); print(marquee_tail, end="", flush=True)

        column -= 1

        if column == 0:
            column = column_limit

        if msvcrt.kbhit():
            t.cls()
            t.show_cursor()
            break

        time.sleep(0.2)

if __name__ == "__main__":

    text = input("¿Qué ponemos? ->")
    marquee(text)
    
