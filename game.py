from tkinter.constants import NONE
import pygame
from Astar import algorithm
import Spot

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot.create_spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def resetGrid(grid, window):
    for row in range(len(grid)):
        for column in range(len(grid)):
            spot = grid[row][column]
            if(not(Spot.is_barrier(spot))):
                grid[row][column] = Spot.reset(spot)
                Spot.draw(spot, window)


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            Spot.draw(spot, win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width, saveFunction=None, grid=None, start=None, end=None):
    ROWS = 50
    if(grid == None):
        grid = make_grid(ROWS, width)

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if started:
                continue

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    started = True
                    algorithm(lambda:  draw(win, grid, ROWS, width),
                              grid, start, end)
                    started = False
                elif event.key == pygame.K_r:
                    start = None
                    end = None
                    resetGrid(grid, win)
                elif event.key == pygame.K_s:
                    if(saveFunction != None):
                        path = algorithm(lambda:  draw(win, grid, ROWS, width),
                                         grid, start, end)
                        saveFunction(grid, ROWS, path)

            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                spot = grid[row][col]
                if(Spot.is_empty(spot)):
                    if(not(start)):
                        spot = Spot.make_start(spot)
                        grid[row][col] = spot
                        start = spot
                    elif(not(end)):
                        spot = Spot.make_end(spot)
                        grid[row][col] = spot
                        end = spot
                    else:
                        spot = Spot.make_barrier(spot)
                        grid[row][col] = spot

                    Spot.draw(spot, win)

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if(not(Spot.is_empty(spot))):

                    if(Spot.is_start(spot)):
                        start = None
                    elif(Spot.is_end(spot)):
                        end = None

                    spot = Spot.reset(spot)
                    grid[row][col] = spot
                    Spot.draw(spot, win)

    pygame.quit()
