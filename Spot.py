import pygame

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


class Spot:
    def __init__(self, row, col, width, total_rows, color=WHITE):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = color
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    #############################
    # Getter Functions
    #############################

    def get_pos(self):
        return (self.row, self.col)

    def get_width(self):
        return self.width

    def get_color(self):
        return self.color

    def is_closed(self):
        return self.color == YELLOW

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_end(self):
        return self.color == PURPLE

    def is_start(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def is_empty(self):
        return self.color == WHITE

    #############################
    # Setter Functions
    #############################

    def make_closed(self):
        self.color = YELLOW

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = ORANGE

    def make_end(self):
        self.color = PURPLE

    def make_start(self):
        self.color = TURQUOISE

    # Draw Function
    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        row, col = self.get_pos()
        total_rows = self.total_rows

        # Right
        if(col < total_rows - 1 and not(grid[row][col + 1].is_barrier())):
            self.neighbors.append(grid[row][col + 1])

        # Left
        if(col > 0 and not(grid[row][col - 1].is_barrier())):
            self.neighbors.append(grid[row][col - 1])

        # Top
        if(row > 0 and not(grid[row - 1][col].is_barrier())):
            self.neighbors.append(grid[row - 1][col])

        # Bottom
        if(row < total_rows - 1 and not(grid[row + 1][col].is_barrier())):
            self.neighbors.append(grid[row + 1][col])

        # Bottom Left
        if((col > 0 and row < total_rows - 1) and not(grid[row + 1][col - 1].is_barrier())):
            self.neighbors.append(grid[row + 1][col - 1])

         # Bottom Right
        if((col < total_rows - 1 and row < total_rows - 1) and not(grid[row + 1][col + 1].is_barrier())):
            self.neighbors.append(grid[row + 1][col + 1])

        # Top Left
        if((col > 0 and row > 0) and not(grid[row - 1][col - 1].is_barrier())):
            self.neighbors.append(grid[row - 1][col - 1])

        # Top Right
        if((col < total_rows - 1 and row > 0) and not(grid[row - 1][col + 1].is_barrier())):
            self.neighbors.append(grid[row - 1][col + 1])

    def __it__(self, other):
        return False
