# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Bounds
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4

# Players
PLAYER = False
CPU = True

# Board states
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

# GUI window
SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE / 2 - 5)
