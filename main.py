from tkinter import *

# Variables

W = 400
H = 400

global taille_serpent
#global etat[0]
global taille_bloc

etat = [6] # 4 = gauche, 6 = droite, 8 = haut, 2 = bas
taille_serpent = 4
taille_bloc= H/20

serpent_base = [
    [W/2+(taille_bloc*0), W/2, H/2+(taille_bloc*0), H/2],
    [W/2+(taille_bloc*1), W/2, H/2+(taille_bloc*1), H/2],
    [W/2+(taille_bloc*2), W/2, H/2+(taille_bloc*2), H/2],
    [W/2+(taille_bloc*3), W/2, H/2+(taille_bloc*3), H/2]
]

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    'green'
]

# Fonctions

def haut(event):
    print('Haut')
    if etat[0] == 4 or etat[0] == 6:
        etat[0] = 8

def bas(event):
    print('Bas')
    if etat[0] == 4 or etat[0] == 6:
        etat[0] = 2

def droite(event):
    print('Droite')
    if etat[0] == 8 or etat[0] == 2:
        etat[0] =  6

def gauche(event):
    print('Gauche')
    if etat[0] == 8 or etat[0] == 2:
        etat[0] = 4

def hors_limite(x:int, y:int):
    if x >= W-taille_bloc or y >= H-taille_bloc or x <= 0-taille_bloc or y <= 0-taille_bloc:
        game.delete(ALL)
        game.create_text(W/2-25, H/2-25, text='Game \n over')

def suicide(x:int, y:int, serpent:list):
    for i in range(0, int(taille_bloc)):
        if serpent[i][0] < x < serpent[i][1] or serpent[i][2] < y < serpent[i][3]:
            game.delete(ALL)
            game.create_text(W/2-25, H/2-25, text='Game \n over')

def new_game():
    game.delete(ALL)
    global serpent
    serpent = list(serpent_base)
    deplacement()

def deplacement():
    if etat[0] == 6:
        origine = list(serpent)
        serpent[0] = [serpent[0][0]+taille_bloc, serpent[0][1], serpent[0][2]+taille_bloc, serpent[0][3]]
    if etat[0] == 4:
        origine = list(serpent)
        serpent[0] = [serpent[0][0]-taille_bloc, serpent[0][1], serpent[0][2]-taille_bloc, serpent[0][3]]
    if etat[0] == 8:
        origine = list(serpent)
        serpent[0] = [serpent[0][0], serpent[0][1]-taille_bloc, serpent[0][2], serpent[0][3]-taille_bloc]
    if etat[0] == 2:
        origine = list(serpent)
        serpent[0] = [serpent[0][0], serpent[0][1]+taille_bloc, serpent[0][2], serpent[0][3]+taille_bloc]
    for i in range(1,taille_serpent):
        serpent[i] = origine[i-1]
    for i in range(0,taille_serpent):
        game.create_rectangle(serpent[i], width=taille_bloc , outline=colour[2], fill=colour[2])
    game.create_rectangle(origine[taille_serpent-1], width=taille_bloc, outline=colour[1], fill=colour[1])
    hors_limite(serpent[0][0], serpent[0][1])
    suicide(serpent[0][0], serpent[0][1], serpent)
    game.after(100, deplacement)

# Widgets

win = Tk()
win.title('Snake')

game = Canvas(win, width=W, height=H, bg=colour[1])
game.grid(rowspan=14, column=1)

win.bind('<KeyPress-Up>', haut)
win.bind('<KeyPress-Down>', bas)
win.bind('<KeyPress-Left>', gauche)
win.bind('<KeyPress-Right>', droite)

but1 = Button(win, text='Start new game', fg=colour[0], bg=colour[1], command=new_game)
but1.grid(row=1, column=0)

but2 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but2.grid(row=13, column=0)

win.mainloop()