from tkinter import *

# Variables

W = 400
H = 400

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
]

# Fonctions

def new_game():
    deplacement()

def deplacement():
    x=10 ; y=10
    game.create_rectangle(x, y, x+5, y+5)
    game.after(20, deplacement)

# Classes

class snake_body():
    def __init__(self, size, direction):
        self.size = size
        self.direction = direction
        self = game.create_rectangle()
    def move():
        game.move(self)
        game.after(20, self.move)

# Widgets

win = Tk()
win.title('Snake')

game = Canvas(win, width=W, height=H, bg=colour[1])
game.grid(rowspan=14, column=1)

but1 = Button(win, text='Start new game', fg=colour[0], bg=colour[1], command=new_game)
but1.grid(row=1, column=0)

but2 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but2.grid(row=13, column=0)

win.mainloop()