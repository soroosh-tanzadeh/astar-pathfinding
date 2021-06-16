from tkinter.constants import W
import DataManager
from tkinter import Button, Frame, Label, Tk
from tkinter.filedialog import asksaveasfile, askopenfile
import pygame

import game


def saveFunction(grid, rows, path):
    files = [('Json File', '*.json')]
    selectedFile = asksaveasfile(
        filetypes=files, defaultextension=files)
    if(selectedFile != None):
        DataManager.save(selectedFile, grid, rows, path)


def newBoard():
    width = 800
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("A* Pathfiding")
    game.main(window, width, lambda grid, rows,
              path: saveFunction(grid, rows, path))


def loadGame():
    files = [('Json File', '*.json')]
    selectedFile = askopenfile(
        filetypes=files, defaultextension=files)
    if(selectedFile != None):
        width = 800
        window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("A* Pathfiding")
        grid, start, end = DataManager.read(selectedFile)
        game.main(window, width, lambda grid,
                  rows, path: saveFunction(grid, rows, path), grid, start, end)


root = Tk()
root.geometry("600x200")
root.title("Pathfinding game with A*")

toolbar = Frame(root, background="#d5e8d4", height=60)
toolbar.pack(side="top", fill="x")

start_button = Button(text="New Game Board", master=toolbar, command=newBoard)
start_button.grid(row=0, column=0, pady=4, padx=4)
load_button = Button(text="Load Game Board", master=toolbar, command=loadGame)
load_button.grid(row=0, column=1, pady=4, padx=4)


content = Frame(root, background="#FFF")
content.pack(side="bottom", fill="both", expand=True)

line_1 = Label(text="P : Start Drawing Path",
               master=content, background="#FFF")
line_2 = Label(text="C : Check Path that you draw",
               master=content, background="#FFF")
line_3 = Label(text="S : Save The Board", master=content, background="#FFF")
line_4 = Label(text="Space : Run A* algorithm",
               master=content, background="#FFF")
line_5 = Label(
    text="R : Reset Board (Keep barriers but remove open, closed, path, start and end nodes)", background="#FFF", master=content)

line_1.grid(row=1, column=0, pady=4, padx=1, sticky=W)
line_2.grid(row=2, column=0, pady=4, padx=1, sticky=W)
line_3.grid(row=3, column=0, pady=4, padx=1, sticky=W)
line_4.grid(row=4, column=0, pady=4, padx=1, sticky=W)
line_5.grid(row=5, column=0, pady=4, padx=1, sticky=W)

root.mainloop()
