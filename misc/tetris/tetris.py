import curses
import random
import sys
import select
import time

GAME_LOOP_SECS = 0.5

BOARD_WIDTH = 20
BOARD_HEIGHT = 20

# Each starts positioned at top of board
TOP_CENTER = int((BOARD_WIDTH + 1) / 2)

PIECES = [
    # line
    set([(TOP_CENTER - 2, 0), (TOP_CENTER - 1, 0), (TOP_CENTER, 0), (TOP_CENTER + 1, 0)]),

    # l
    set([(TOP_CENTER - 2, 0), (TOP_CENTER - 2, 1), (TOP_CENTER - 1, 1), (TOP_CENTER, 1)]),

    # t
    set([(TOP_CENTER - 2, 1), (TOP_CENTER - 1, 0), (TOP_CENTER - 1, 1), (TOP_CENTER, 1)]),

    # s
    set([(TOP_CENTER - 2, 1), (TOP_CENTER - 1, 1), (TOP_CENTER - 1, 0), (TOP_CENTER, 0)])
]

def random_piece():
    return random.choice(PIECES)

# NOTE: rotate around top-left most square
class State():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.filled = set()
        self.falling_piece = random_piece()

def time_step(state):
    hit_bottom = False
    for x,y in state.falling_piece:
        if (x, y + 1) in state.filled or y == state.height - 1:
            hit_bottom = True

    if hit_bottom:
        state.filled |= set(state.falling_piece)
        state.falling_piece = random_piece()
    else:
        state.falling_piece = [(x, y + 1) for (x, y) in state.falling_piece]

def is_cell_valid(cell, state):
    if cell[0] < 1 or cell[0] > state.width - 1 or cell[1] > state.height - 1:
        return False
    elif cell in state.filled:
        return False
    else:
        return True

def is_valid_piece_placement(piece, state):
    return all(is_cell_valid(cell, state) for cell in piece)

def rotate_piece(piece, state):
    """Returns the piece after one counter-clockwise rotation.

    If the rotation results in an invalid configuration, returns the original piece.
    """
    (rotation_x, rotation_y) = sorted(list(piece))[0]
    rspace_piece = [(x - rotation_x, y - rotation_y) for (x, y) in piece]
    rspace_rotated_piece = [(-1 * y, x) for (x, y) in rspace_piece]
    rotated_piece = set([(x + rotation_x, y + rotation_y) for (x, y) in rspace_rotated_piece])

    if is_valid_piece_placement(rotated_piece, state):
        return rotated_piece
    else:
        return piece

def process_keypress(screen, state):
    keypress = screen.getch()

    # L
    if keypress == 260:
        if all((x > 1 for (x,y) in state.falling_piece)):
            state.falling_piece = [(x - 1, y) for (x, y) in state.falling_piece]

    # R
    elif keypress == 261:
        if all((x < state.width - 1 for (x,y) in state.falling_piece)):
            state.falling_piece = [(x + 1, y) for (x, y) in state.falling_piece]

    # U
    elif keypress == 259:
        state.falling_piece = rotate_piece(state.falling_piece, state)

    # space
    elif keypress == 32:
        # TODO: fast fall
        pass

def clear_rows(state):
    pass

def render(screen, state):
    screen.clear()

    # Add borders
    for y in range(state.height):
        screen.addch(y, state.width + 1, '|')
        screen.addch(y, 0, '|')
    for x in range(1, state.width + 1):
        screen.addch(state.height - 1, x, '_')

    # Add filled squares
    for x,y in state.filled:
        screen.addch(y, x + 1, 'x')

    # Add falling piece
    for x,y in state.falling_piece:
        if y > 0: # NOTE: allow for cells to exist above game board
            screen.addch(y, x + 1, 'x')

    screen.refresh()

def game_loop(screen):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.nodelay(1) # non-blocking keypresses

    state = State(BOARD_WIDTH, BOARD_HEIGHT)
    while True:
        process_keypress(screen, state)
        time_step(state)
        clear_rows(state)

        render(screen, state)
        time.sleep(GAME_LOOP_SECS)

if __name__ == "__main__":
    curses.wrapper(game_loop)
