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
