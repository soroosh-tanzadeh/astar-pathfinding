from DataManager import GridFile
from tkinter import Button, Tk
from tkinter.filedialog import asksaveasfile, askopenfile
import pygame

import game


def saveFunction(grid, rows):
    files = [('Json File', '*.json')]
    selectedFile = asksaveasfile(
        filetypes=files, defaultextension=files)
    if(selectedFile != None):
        file = GridFile(selectedFile.name)
        file.save(grid, rows)


def newBoard():
    width = 800
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A* Pathfiding")
    game.main(window, width, lambda grid, rows: saveFunction(grid, rows))


def loadGame():
    files = [('Json File', '*.json')]
    selectedFile = askopenfile(
        filetypes=files, defaultextension=files)
    if(selectedFile != None):
        file = GridFile(selectedFile.name)
        width = 800
        window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("A* Pathfiding")
        grid, start, end = file.read()
        game.main(window, width, lambda grid,
                  rows: saveFunction(grid, rows), grid, start, end)


root = Tk()
root.geometry("400x400")
root.title("Pathfinding game with A*")

start_button = Button(text="New Game Board", master=root, command=newBoard)
start_button.grid(row=0, column=0, pady=4, padx=4)
load_button = Button(text="Load Game Board", master=root, command=loadGame)
load_button.grid(row=0, column=1, pady=4, padx=4)


root.mainloop()
