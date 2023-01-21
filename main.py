from tkinter import *
from time import sleep

# Variables

W = 400
H = 400

etat = [6] # 4 = gauche, 6 = droite, 8 = haut, 2 = bas
taille = [4]

serpent = [
    [200, 200, 205, 205],
    [205, 200, 210, 205],
    [210, 200, 215, 205],
    [215, 200, 220, 205]
]

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
]

# Fonctions

def haut():
    print('Haut')
    if etat[0] == 4 or etat[0] == 6:
        etat[0] = 8

def bas():
    print('Bas')
    if etat[0] == 4 or etat[0] == 6:
        etat[0] = 2

def droite():
    if etat[0] == 8 or etat[0] == 2:
        etat[0] =  6

def gauche():
    if etat[0] == 8 or etat[0] == 2:
        etat[0] = 4

def off_limit(x, y):
    if x >= 400 or y >= 400:
        win.quit()

def new_game():
    deplacement()

def deplacement():
    if etat[0] == 6:
        origine = list(serpent)
        for i in range(0,taille[0]):
            serpent[i] = [serpent[i][0]+20, serpent[i][1], serpent[i][2]+20, serpent[i][3]]
    if etat[0] == 4:
        origine = list(serpent)
        for i in range(0,taille[0]):
            serpent[i] = [serpent[i][0]-20, serpent[i][1], serpent[i][2]-20, serpent[i][3]]
    if etat[0] == 8:
        origine = list(serpent)
        for i in range(0,taille[0]):
            serpent[i] = [serpent[i][0], serpent[i][1]-20, serpent[i][2], serpent[i][3]-20]
    if etat[0] == 2:
        origine = list(serpent)
        for i in range(0,taille[0]):
            serpent[i] = [serpent[i][0], serpent[i][1]+20, serpent[i][2], serpent[i][3]+20]
    for i in range(0,taille[0]):
        game.create_rectangle(serpent[i])
    for i in range(0, taille[0]):
        game.create_rectangle(origine[i], outline=colour[1])
    #off_limit(serpent[0][0], serpent[0][1])
    game.after(150, deplacement)

# Widgets

win = Tk()
win.title('Snake')

game = Canvas(win, width=W, height=H, bg=colour[1])
game.grid(rowspan=14, column=1)

game.bind('<Up>', haut)
game.bind('<Down>', bas)
game.bind('<Left>', gauche)
game.bind('<Right>', droite)

but1 = Button(win, text='Start new game', fg=colour[0], bg=colour[1], command=new_game)
but1.grid(row=1, column=0)

but2 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but2.grid(row=13, column=0)

win.mainloop()