import termio as t
from termio import Color, Attr

t.cls()

print(f"Este es un texto en {Attr.ITALIC}cursiva{Attr.ITALIC_OFF} y este otro \
en {Attr.BOLD}negrita{Attr.BOLD_OFF}.")

print(f"Este es un texto en {Color.F_WHITE}{Color.B_RED}blanco sobre rojo{Color.NORMAL}.  Este ya no.")

