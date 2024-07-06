# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR

class Color:
    """BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39
    GRAY = 90
    BRIGHT_RED = 91
    BRIGHT_GREEN = 92
    BRIGHT_YELLOW = 93
    BRIGHT_BLUE = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN = 96
    BRIGHT_WHITE = 97"""

    F_BLACK = f"\033[30m"
    F_RED = f"\033[31m"
    F_GREEN = f"\033[32m"
    F_YELLOW = f"\033[33m"
    F_BLUE = f"\033[34m"
    F_MAGENTA = f"\033[35m"
    F_CYAN = f"\033[36m"
    F_WHITE = f"\033[37m"
    F_DEFAULT = f"\033[39m"
    F_GRAY = f"\033[90m"
    F_BRIGHT_RED = f"\033[91m"
    F_BRIGHT_GREEN = f"\033[92m"
    F_BRIGHT_YELLOW = f"\033[93m"
    F_BRIGHT_BLUE = f"\033[94m"
    F_BRIGHT_MAGENTA = f"\033[95m"
    F_BRIGHT_CYAN = f"\033[96m"
    F_BRIGHT_WHITE = f"\033[97m"

    B_BLACK = f"\033[40m"
    B_RED = f"\033[41m"
    B_GREEN = f"\033[42m"
    B_YELLOW = f"\033[43m"
    B_BLUE = f"\033[44m"
    B_MAGENTA = f"\033[45m"
    B_CYAN = f"\033[46m"
    B_WHITE = f"\033[47m"
    B_DEFAULT = f"\033[49m"
    B_GRAY = f"\033[100m"
    B_BRIGHT_RED = f"\033[101m"
    B_BRIGHT_GREEN = f"\033[102m"
    B_BRIGHT_YELLOW = f"\033[103m"
    B_BRIGHT_BLUE = f"\033[104m"
    B_BRIGHT_MAGENTA = f"\033[105m"
    B_BRIGHT_CYAN = f"\033[106m"
    B_BRIGHT_WHITE = f"\033[107m"

    NORMAL = f"\033[39;49m"


class Attr:
    
    NORMAL = f"\033[0m"
    BOLD = f"\033[1m"
    FAINT = f"\033[2m"
    ITALIC = f"\033[3m"
    UNDER = f"\033[4m"
    BLINK = f"\033[5m"
    INVERT = f"\033[7m"
    STRIKE = f"\033[9m"

    BOLD_OFF = f"\033[22m"
    FAINT_OFF = f"\033[22m"
    ITALIC_OFF = f"\033[23m"
    UNDER_OFF = f"\033[24m"
    BLINK_OFF = f"\033[25m"
    INVERT_OFF = f"\033[27m"
    STRIKE_OFF = f"\033[29m"
    


def cls():
    print(f"\033c", end="", flush=True)

def locate(line, column):
    print(f"\033[{line};{column}H", end="", flush=True)

def move_up(lines):
    print(f"\033[{lines}A")

def move_down(lines):
    print(f"\033[{lines}B")

def move_right(lines):
    print(f"\033[{lines}C")

def move_left(lines):
    print(f"\033[{lines}D")

def move_to_column(column):
    print(f"\033[{column}G")

def hide_cursor():
    print("\033[?25l")  # Ocultar Cursor
    
def show_cursor():
    print("\033[?25h")  # Mostrar Cursor

"""
def set_color(fgcolor=Color.DEFAULT , bgcolor=Color.DEFAULT):
    print(f"\033[{fgcolor};{bgcolor+10}m", end="")

def set_attribute(format=Attribute.NORMAL):
    print(f"\033[{format}m", end="")

def cprint(text, 
           fgcolor=Color.DEFAULT, 
           bgcolor=Color.DEFAULT, 
           attr=[Attribute.NORMAL], **kwargs):
    
    f_begin = ""

    for a in attr:
        f_begin += f"\033[{a}m"

    f_begin += f"\033[{fgcolor};{bgcolor+10}m"
    f_end = f"\033[{Attribute.NORMAL}m\033[{Color.DEFAULT};{Color.DEFAULT+10}m"
    
    print(f"{f_begin}{text}{f_end}", **kwargs)
"""