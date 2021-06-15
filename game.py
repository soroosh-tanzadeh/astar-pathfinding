from tkinter.constants import NONE
import pygame
from Astar import algorithm
import Spot
from tkinter import messagebox

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


def resetGrid(grid, window,KeepStartEnd=False):
    for row in range(len(grid)):
        for column in range(len(grid)):
            spot = grid[row][column]
            if(KeepStartEnd):
                if(not(Spot.is_barrier(spot)) and not(Spot.is_start(spot)) and not(Spot.is_end(spot))):
                    grid[row][column] = Spot.reset(spot)
                    Spot.draw(spot, window)
            else:
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
    # draw_grid(win, rows, width)
    pygame.display.update()


def ix(dic, n): #don't use dict as  a variable name
   try:
       return dic[list(dic)[n]] # or sorted(dic)[n] if you want the keys to be sorted
   except IndexError:
       print('not enough keys')


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def neighbor_startAndEnd(path, grid,win):
    firstSpot = Spot.update_neighbors(ix(path,0), grid)
    lastSpot = Spot.update_neighbors(ix(path,len(list(path)) - 1), grid)

    startFound = False
    endFound = False

    for spot in firstSpot['neighbors']:
        if(Spot.is_start(spot)):
            startFound = True
        elif(Spot.is_end(spot)):
            endFound = True
    for spot in lastSpot['neighbors']:
        if(Spot.is_start(spot)):
            startFound = True
        elif(Spot.is_end(spot)):
            endFound = True
    
    return endFound and startFound


def main(win, width, saveFunction=None, grid=None, start=None, end=None):
    ROWS = 50
    if(grid == None):
        grid = make_grid(ROWS, width)

    run = True
    started = False
    play = False
    userPath = {}
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
                        print(path)
                        if(path != False):
                            saveFunction(grid, ROWS, path)
                        else:
                            messagebox.showwarning(
                                "Can't save", "No Path found to the end point")
                elif event.key == pygame.K_p:
                    if(start and end):
                        resetGrid(grid,win,True)
                        play = True
                elif event.key == pygame.K_c:
                    if(neighbor_startAndEnd(userPath,grid,win)):
                        play = False
                        started = True
                        path = algorithm(lambda:  draw(win, grid, ROWS, width),
                                grid, start, end)
                        started = False
                        score = len(list(userPath)) - len(path)
                        if(score <= 0):
                            socre = 100
                            messagebox.showinfo(
                                "Wonderful", "Your score : "+str(socre))
                        else:
                            messagebox.showinfo(
                                "Opps", "This is not the shortest path \n press P to play again")
                        resetGrid(grid,win,True)
                        

                    

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
                        if(play):
                            neighbors = Spot.update_neighbors(spot,grid)['neighbors']
                            canMakePath = False
                            for neighbor in neighbors:
                                if(Spot.is_start(neighbor) or Spot.is_end(neighbor) or Spot.is_path(neighbor)):
                                    canMakePath = True
                            
                            if(canMakePath):
                                spot = Spot.make_path(spot)
                                userPath[spot['id']] = spot
                                Spot.draw(spot, win)
                                grid[row][col] = spot
                            continue
                        else:
                            spot = Spot.make_barrier(spot)
                        grid[row][col] = spot

                    Spot.draw(spot, win)

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if(not(Spot.is_empty(spot))):

                    if(not(Spot.is_start(spot)) and not(Spot.is_end(spot)) and not(Spot.is_barrier(spot))):
                        del userPath[spot['id']]
                        spot = Spot.reset(spot)
                        grid[row][col] = spot
                        Spot.draw(spot, win)
                        continue

                    if(Spot.is_start(spot)):
                        start = None
                    elif(Spot.is_end(spot)):
                        end = None

                    spot = Spot.reset(spot)
                    grid[row][col] = spot
                    Spot.draw(spot, win)
                    
                    

    pygame.quit()
