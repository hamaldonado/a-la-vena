import time
import termio as t
from termio import Color
import kbhit
import random

# ── Constants ──
SCREEN_WIDTH = 60
SCREEN_HEIGHT = 20

GOAL_ROW = 3
RIVER_ROWS = [4, 5, 6]
ROAD_ROWS = [8, 9, 10, 11, 12]
START_ROW = 14

# Home positions (columns in the goal zone)
home_cols = [10, 20, 30, 40, 50]
NUM_HOMES = len(home_cols)

# ── Game state ──
frog_r = START_ROW
frog_c = 30
score = 0
lives = 3
level = 1
game_active = True
home_filled = []

# ── Lane definitions ──
# [row, type, direction, speed, char, obstacles]
# obstacles: list of [col, length]
# direction: 1=right, -1=left
# speed: ticks between movements

lanes = [
    # River lanes
    [4, 'river',  1, 3, '=', [[  6, 5], [21, 6], [38, 4], [53, 4]]],
    [5, 'river', -1, 2, '=', [[ 10, 4], [26, 5], [44, 6]]],
    [6, 'river',  1, 4, '=', [[  4, 6], [18, 5], [33, 4], [48, 5]]],
    # Road lanes
    [8,  'road',  1, 2, '#', [[ 14, 3], [34, 4], [52, 3]]],
    [9,  'road', -1, 3, '&', [[  6, 4], [28, 3], [46, 5]]],
    [10, 'road',  1, 4, '$', [[ 10, 3], [31, 4], [50, 3]]],
    [11, 'road', -1, 2, '#', [[ 20, 5], [39, 3]]],
    [12, 'road',  1, 3, '&', [[  8, 4], [24, 5], [44, 4]]],
]

# Tick counters for each lane (one per lane)
tick_counters = [0] * len(lanes)


# ── Scenery (static, drawn once) ──

def draw_scenery():
    t.cls()

    # ── Top border (row 2) ──
    print(Color.F_BRIGHT_YELLOW)
    t.locate(1, 1); print("FROGGER".center(SCREEN_WIDTH, '─'))
    t.locate(2, 1); print("#" * SCREEN_WIDTH)
    print(Color.F_DEFAULT)

    # ── Goal zone (row 3) ──
    t.locate(GOAL_ROW, 2)
    print(Color.F_CYAN + "~" * (SCREEN_WIDTH - 2) + Color.F_DEFAULT, end="")
    for hc in home_cols:
        t.locate(GOAL_ROW, hc)
        print(Color.F_BRIGHT_WHITE + "░" + Color.F_DEFAULT, end="")

    # ── River lanes (rows 4-6) ──
    for rr in RIVER_ROWS:
        t.locate(rr, 2)
        print(Color.F_CYAN + "~" * (SCREEN_WIDTH - 2) + Color.F_DEFAULT, end="")

    # ── Road lanes (rows 8-12) background ──
    for rr in ROAD_ROWS:
        t.locate(rr, 2)
        print(Color.F_GRAY + "." * (SCREEN_WIDTH - 2) + Color.F_DEFAULT, end="")

    # ── Dividers (rows 7, 13) ──
    print(Color.F_BRIGHT_YELLOW)
    t.locate(7, 2);  print("═" * (SCREEN_WIDTH - 2))
    t.locate(13, 2); print("═" * (SCREEN_WIDTH - 2))
    print(Color.F_DEFAULT)

    # ── Start zone (row 14) ──
    t.locate(START_ROW, 2)
    print(Color.F_GREEN + " " * (SCREEN_WIDTH - 2) + Color.F_DEFAULT)

    # ── Bottom border (row 15) ──
    print(Color.F_BRIGHT_YELLOW)
    t.locate(15, 1); print("#" * SCREEN_WIDTH)
    print(Color.F_DEFAULT)

    # ── Border sides (col 1 and SCREEN_WIDTH) ──
    print(Color.F_BRIGHT_YELLOW)
    for line in range(2, SCREEN_HEIGHT + 1):
        t.locate(line, 1); print("#")
        t.locate(line, SCREEN_WIDTH); print("#")
    print(Color.F_DEFAULT)

    # Status bar (row 1 will be updated dynamically)
    update_status()


# ── Status bar ──

def update_status():
    filled = sum(1 for f in home_filled if f)
    t.locate(1, 2)
    print(Color.F_BRIGHT_WHITE +
          f" FROGGER   Puntaje: {score:04d}   Vidas: {lives}   "
          f"Nivel: {level}   Homes: {filled}/{NUM_HOMES}   "
          + Color.F_DEFAULT, end="")

def show_message(text):
    """Show a temporary message at the bottom of the screen."""
    t.locate(17, 2)
    print(Color.F_BRIGHT_YELLOW + text.center(SCREEN_WIDTH - 4)
          + Color.F_DEFAULT)


# ── Obstacle drawing ──

def draw_obstacles():
    for lane in lanes:
        row = lane[0]
        ltype = lane[1]
        direction = lane[2]
        ch = lane[4]
        obstacles = lane[5]

        if ltype == 'river':
            # Redraw entire row as water first
            t.locate(row, 2)
            print(Color.F_CYAN + "~" * (SCREEN_WIDTH - 2) + Color.F_DEFAULT,
                  end="")
            # Then draw logs on top
            for obs in obstacles:
                col = obs[0]
                ln = obs[1]
                for i in range(ln):
                    c = col + i
                    if 2 <= c < SCREEN_WIDTH:
                        t.locate(row, c)
                        print(Color.F_BRIGHT_YELLOW + ch + Color.F_DEFAULT,
                              end="")
        else:
            # Redraw entire row as road first
            t.locate(row, 2)
            print(Color.F_GRAY + "." * (SCREEN_WIDTH - 2) + Color.F_DEFAULT,
                  end="")
            # Then draw cars on top
            for obs in obstacles:
                col = obs[0]
                ln = obs[1]
                for i in range(ln):
                    c = col + i
                    if 2 <= c < SCREEN_WIDTH:
                        t.locate(row, c)
                        if i == 0:
                            # Car front has headlight
                            print(Color.F_WHITE + "◄" + Color.F_DEFAULT
                                  if direction == -1 else
                                  Color.F_WHITE + "►" + Color.F_DEFAULT,
                                  end="")
                        else:
                            print(
                                (Color.F_RED if ch == '#'
                                 else Color.F_YELLOW if ch == '&'
                                 else Color.F_MAGENTA)
                                + ch + Color.F_DEFAULT,
                                end="")


def draw_frog():
    t.locate(frog_r, frog_c)
    print(Color.F_BRIGHT_GREEN + "@" + Color.F_DEFAULT, end="")


def erase_frog():
    # Determine what to put back in frog's place
    row = frog_r
    col = frog_c

    if row in RIVER_ROWS or row == GOAL_ROW:
        # Water
        if row == GOAL_ROW and col in home_cols:
            t.locate(row, col)
            print(Color.F_BRIGHT_WHITE + "░" + Color.F_DEFAULT, end="")
        else:
            t.locate(row, col)
            print(Color.F_CYAN + "~" + Color.F_DEFAULT, end="")
    elif row in ROAD_ROWS:
        t.locate(row, col)
        print(Color.F_GRAY + "." + Color.F_DEFAULT, end="")
    elif row in [7, 13]:
        t.locate(row, col)
        print(Color.F_BRIGHT_YELLOW + "═" + Color.F_DEFAULT, end="")
    else:
        t.locate(row, col)
        print(" ", end="")


# ── Obstacle movement ──

def move_obstacles():
    for i, lane in enumerate(lanes):
        tick_counters[i] = (tick_counters[i] + 1) % lane[3]  # speed
        if tick_counters[i] != 0:
            continue

        direction = lane[2]
        obstacles = lane[5]

        for obs in obstacles:
            obs[0] += direction

            # Wrap around
            if direction == 1:  # moving right
                if obs[0] >= SCREEN_WIDTH:
                    obs[0] = 2 - obs[1]
            else:  # moving left
                if obs[0] + obs[1] <= 1:
                    obs[0] = SCREEN_WIDTH - 2


# ── River mechanics ──

def find_log(row, col):
    """Return (lane_index, obstacle_index) if (row,col) is on a log, else None."""
    for li, lane in enumerate(lanes):
        if lane[0] != row or lane[1] != 'river':
            continue
        obstacles = lane[5]
        for oi, obs in enumerate(obstacles):
            if obs[0] <= col < obs[0] + obs[1]:
                return (li, oi)
    return None


def is_on_log(row, col):
    return find_log(row, col) is not None


def handle_river():
    """Carry frog with log if on one. Returns False if frog drowned."""
    global frog_r, frog_c

    in_river_zone = frog_r in RIVER_ROWS or frog_r == GOAL_ROW

    if not in_river_zone:
        return True

    # If on goal row and on a home, safe
    if frog_r == GOAL_ROW:
        for hi, hc in enumerate(home_cols):
            if frog_c == hc and not home_filled[hi]:
                return True  # Safe on home
        # On goal row but not on home → water → drown
        return False

    # In river zone: must be on a log
    log_pos = find_log(frog_r, frog_c)
    if log_pos is None:
        return False  # Drowned

    li, oi = log_pos
    lane = lanes[li]

    # Was the log moved this tick?
    if tick_counters[li] == 0:
        # Log moved → carry frog
        frog_c += lane[2]

        # Check if frog got carried out of bounds
        if frog_c <= 1 or frog_c >= SCREEN_WIDTH:
            return False  # Fell off edge

        # Check if frog is still on the log after moving
        if not is_on_log(frog_r, frog_c):
            return False  # Fell off log

    return True


# ── Car collision ──

def is_hit_by_car():
    """Check if frog is on a road lane and overlaps with a car."""
    if frog_r not in ROAD_ROWS:
        return False

    for lane in lanes:
        if lane[0] != frog_r or lane[1] != 'road':
            continue
        obstacles = lane[5]
        for obs in obstacles:
            if obs[0] <= frog_c < obs[0] + obs[1]:
                return True
    return False


# ── Goal check ──

def check_goal():
    """Returns True if frog reached an empty home."""
    global score

    if frog_r != GOAL_ROW:
        return False

    for hi, hc in enumerate(home_cols):
        if frog_c == hc and not home_filled[hi]:
            home_filled[hi] = True
            score += 10
            show_message(f"HOME!   +10 puntos")
            return True

    return False


# ── Game logic ──

def reset_frog():
    global frog_r, frog_c
    erase_frog()
    frog_r = START_ROW
    frog_c = 30
    draw_frog()


def frog_dies():
    global lives, game_active

    lives -= 1
    show_message("💀  RANA MUERTA!")
    time.sleep(0.8)

    if lives <= 0:
        game_active = False
        t.locate(10, 1)
        print(Color.F_BRIGHT_RED + "GAME OVER".center(SCREEN_WIDTH)
              + Color.F_DEFAULT)
        return

    reset_frog()
    update_status()


def handle_frog_movement(direction):
    """Move frog by 1 cell in given direction. direction: 0=up,1=right,2=down,3=left"""
    global frog_r, frog_c

    erase_frog()

    nr, nc = frog_r, frog_c

    match direction:
        case 0:  # UP
            nr -= 1
        case 1:  # RIGHT
            nc += 1
        case 2:  # DOWN
            nr += 1
        case 3:  # LEFT
            nc -= 1

    # Bound checks
    if nr < 3 or nr > START_ROW:
        return  # Can't move past boundaries
    if nc <= 1 or nc >= SCREEN_WIDTH:
        return  # Can't move past side boundaries

    frog_r, frog_c = nr, nc


def level_complete():
    global level, home_filled, game_active

    score += 50
    show_message(f"NIVEL {level} COMPLETADO!")
    time.sleep(1.2)

    level += 1
    home_filled = [False] * NUM_HOMES

    # Increase speed slightly
    for lane in lanes:
        if lane[3] > 1:
            lane[3] -= 1  # Increase speed (lower = faster)

    reset_frog()
    draw_obstacles()
    update_status()
    show_message(f"Nivel {level} — GO!")
    time.sleep(0.8)


# ── Main game loop ──

def main():
    global game_active, score, lives, level, home_filled, frog_r, frog_c

    # Reset everything
    frog_r = START_ROW
    frog_c = 30
    score = 0
    lives = 3
    level = 1
    game_active = True
    home_filled = [False] * NUM_HOMES

    # Reset lane speeds
    base_speeds = [3, 2, 4, 2, 3, 4, 2, 3]
    for i, lane in enumerate(lanes):
        lane[3] = base_speeds[i]

    # Reset obstacle positions
    base_obstacles = [
        [[  6, 5], [21, 6], [38, 4], [53, 4]],
        [[ 10, 4], [26, 5], [44, 6]],
        [[  4, 6], [18, 5], [33, 4], [48, 5]],
        [[ 14, 3], [34, 4], [52, 3]],
        [[  6, 4], [28, 3], [46, 5]],
        [[ 10, 3], [31, 4], [50, 3]],
        [[ 20, 5], [39, 3]],
        [[  8, 4], [24, 5], [44, 4]],
    ]
    for i, lane in enumerate(lanes):
        lane[5] = [obs[:] for obs in base_obstacles[i]]

    for i in range(len(tick_counters)):
        tick_counters[i] = 0

    draw_scenery()
    draw_obstacles()
    draw_frog()
    update_status()
    show_message(f"Nivel {level} — Usa las flechas para moverte!  🐸")

    kb = kbhit.KBHit()

    while game_active:

        # ── Input ──
        if kb.kbhit():
            c = kb.getarrow()

            match c:
                case 0 | 1 | 2 | 3:
                    handle_frog_movement(c)
                case 113 | 81:  # q / Q
                    game_active = False
                    show_message("Gracias por jugar!")
                    time.sleep(0.5)
                    continue

        # ── Move obstacles ──
        move_obstacles()

        # ── Redraw obstacles ──
        draw_obstacles()

        # ── River mechanics ──
        if not handle_river():
            frog_dies()
            continue

        # ── Car collision ──
        if is_hit_by_car():
            frog_dies()
            continue

        # ── Goal check ──
        if check_goal():
            if all(home_filled):
                level_complete()
            else:
                reset_frog()
            update_status()
            continue

        # ── Draw frog at new position ──
        draw_frog()
        update_status()

        time.sleep(0.12)

    # ── End ──
    t.locate(18, 1)
    print(Color.F_BRIGHT_WHITE + f"Score Final: {score}".center(SCREEN_WIDTH)
          + Color.F_DEFAULT)
    t.locate(19, 1)
    print("Presiona una tecla para salir..".center(SCREEN_WIDTH))
    kb.getch() if kb.kbhit() else None


# ── Entry point ──
if __name__ == "__main__":
    t.hide_cursor()
    main()
    t.show_cursor()
    t.locate(SCREEN_HEIGHT + 1, 1)