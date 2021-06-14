import pygame
import uuid

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 255, 0]
YELLOW = [255, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
PURPLE = [128, 0, 128]
ORANGE = [255, 165, 0]
GREY = [128, 128, 128]
TURQUOISE = [64, 224, 208]


def create_spot(row, col, width, total_rows, color=WHITE):
    return {
        'id': str(uuid.uuid4()),
        'row': row,
        'col': col,
        'width': width,
        'x': row * width,
        'y': col * width,
        'color': color,
        'neighbors': [],
        'total_rows': total_rows
    }


def get_pos(spot):
    return (spot['row'], spot['col'])


def get_width(spot):
    return spot['width']


def get_color(spot):
    return spot['color']


def is_closed(spot):
    return spot['color'] == YELLOW


def is_open(spot):
    return spot['color'] == GREEN


def is_barrier(spot):
    return spot['color'] == BLACK


def is_end(spot):
    return spot['color'] == PURPLE


def is_start(spot):
    return spot['color'] == TURQUOISE


def reset(spot):
    spot['color'] = WHITE
    return spot


def is_empty(spot):
    return spot['color'] == WHITE

    #############################
    # Setter Functions
    #############################


def make_closed(spot):
    spot['color'] = YELLOW
    return spot


def make_open(spot):
    spot['color'] = GREEN
    return spot


def make_barrier(spot):
    spot['color'] = BLACK
    return spot


def make_path(spot):
    spot['color'] = ORANGE
    return spot


def make_end(spot):
    spot['color'] = PURPLE
    return spot


def make_start(spot):
    spot['color'] = TURQUOISE
    return spot


def draw(spot, win):
    pygame.draw.rect(
        win, spot['color'], (spot['x'], spot['y'], spot['width'], spot['width']))


def update_neighbors(spot, grid):
    spot['neighbors'] = []
    row, col = get_pos(spot)
    total_rows = spot['total_rows']

    neighbors = []

    # Right
    if(col < total_rows - 1 and not(is_barrier(grid[row][col + 1]))):
        neighbors.append(grid[row][col + 1])

    # Left
    if(col > 0 and not(is_barrier(grid[row][col - 1]))):
        neighbors.append(grid[row][col - 1])

    # Top
    if(row > 0 and not(is_barrier(grid[row - 1][col]))):
        neighbors.append(grid[row - 1][col])

    # Bottom
    if(row < total_rows - 1 and not(is_barrier(grid[row + 1][col]))):
        neighbors.append(grid[row + 1][col])

    # Bottom Left
    if((col > 0 and row < total_rows - 1) and not(is_barrier(grid[row + 1][col - 1]))):
        neighbors.append(grid[row + 1][col - 1])

    # Bottom Right
    if((col < total_rows - 1 and row < total_rows - 1) and not(is_barrier(grid[row + 1][col + 1]))):
        neighbors.append(grid[row + 1][col + 1])

    # Top Left
    if((col > 0 and row > 0) and not(is_barrier(grid[row - 1][col - 1]))):
        neighbors.append(grid[row - 1][col - 1])

    # Top Right
    if((col < total_rows - 1 and row > 0) and not(is_barrier(grid[row - 1][col + 1]))):
        neighbors.append(grid[row - 1][col + 1])

    spot['neighbors'] = neighbors
    return spot


# class Spot:
#     def __init__(self, row, col, width, total_rows, color=WHITE):
#         self.row = row
#         self.col = col
#         self.width = width
#         self.x = row * width
#         self.y = col * width
#         self.color = color
#         self.neighbors = []
#         self.total_rows = total_rows
#     #############################
#     # Getter Functions
#     #############################

#     def get_pos(self):
#         return (self.row, self.col)

#     def get_width(self):
#         return self.width

#     def get_color(self):
#         return self.color

#     def is_closed(self):
#         return self.color == YELLOW

#     def is_open(self):
#         return self.color == GREEN

#     def is_barrier(self):
#         return self.color == BLACK

#     def is_end(self):
#         return self.color == PURPLE

#     def is_start(self):
#         return self.color == TURQUOISE

#     def reset(self):
#         self.color = WHITE

#     def is_empty(self):
#         return self.color == WHITE

#     #############################
#     # Setter Functions
#     #############################

#     def make_closed(self):
#         self.color = YELLOW

#     def make_open(self):
#         self.color = GREEN

#     def make_barrier(self):
#         self.color = BLACK

#     def make_path(self):
#         self.color = ORANGE

#     def make_end(self):
#         self.color = PURPLE

#     def make_start(self):
#         self.color = TURQUOISE

#     # Draw Function
#     def draw(self, win):
#         pygame.draw.rect(
#             win, self.color, (self.x, self.y, self.width, self.width))

#     def update_neighbors(self, grid):
#         self.neighbors = []
#         row, col = self.get_pos()
#         total_rows = self.total_rows

#         # Right
#         if(col < total_rows - 1 and not(grid[row][col + 1].is_barrier())):
#             self.neighbors.append(grid[row][col + 1])

#         # Left
#         if(col > 0 and not(grid[row][col - 1].is_barrier())):
#             self.neighbors.append(grid[row][col - 1])

#         # Top
#         if(row > 0 and not(grid[row - 1][col].is_barrier())):
#             self.neighbors.append(grid[row - 1][col])

#         # Bottom
#         if(row < total_rows - 1 and not(grid[row + 1][col].is_barrier())):
#             self.neighbors.append(grid[row + 1][col])

#         # Bottom Left
#         if((col > 0 and row < total_rows - 1) and not(grid[row + 1][col - 1].is_barrier())):
#             self.neighbors.append(grid[row + 1][col - 1])

#      # Bottom Right
#         if((col < total_rows - 1 and row < total_rows - 1) and not(grid[row + 1][col + 1].is_barrier())):
#             self.neighbors.append(grid[row + 1][col + 1])

#         # Top Left
#         if((col > 0 and row > 0) and not(grid[row - 1][col - 1].is_barrier())):
#             self.neighbors.append(grid[row - 1][col - 1])

#         # Top Right
#         if((col < total_rows - 1 and row > 0) and not(grid[row - 1][col + 1].is_barrier())):
#             self.neighbors.append(grid[row - 1][col + 1])
