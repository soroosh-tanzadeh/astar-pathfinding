import pygame
from Astar import h, algorithm
from Spot import Spot

width = 800
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("A* Pathfiding")

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
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


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
            spot.draw(win)
    # draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 100
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if started:
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                started = True
                algorithm(lambda:  draw(win, grid, ROWS, width),
                          grid, start, end)
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                spot = grid[row][col]
                if(spot.is_empty()):
                    if(not(start)):
                        start = spot
                        start.make_start()
                    elif(not(end)):
                        end = spot
                        end.make_end()
                    else:
                        spot.make_barrier()

                    spot.draw(window)

            elif pygame.mouse.get_pressed()[2]:
                if(not(spot.is_empty())):
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    spot = grid[row][col]

                    if(spot.is_start()):
                        start = None
                    elif(spot.is_end()):
                        end = None

                    spot.reset()
                    spot.draw(window)

    pygame.quit()


main(window, width)
