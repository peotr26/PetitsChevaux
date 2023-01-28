############################
## Jeu du Serpent | Snake ##
############################

from tkinter import *

# Variables

W = 600
H = 600

global taille_serpent
global etat
global taille_bloc
global game_over

etat = 6                # Variable de la direction du serpent
# 4 = gauche, 6 = droite, 8 = haut, 2 = bas
taille_serpent = 4      # Variable de la taille du serpent.
taille_bloc= int(H/20)  # Variable de la taille d'un carré faisant partie du serpent en fonction de la résolution.
game_over = False       # Variable de si la partie est finie ou non.

# Liste des coordonnées des blocs du serpent au début d'une partie 
serpent_base = [
    [W/2+(taille_bloc*0), W/2, H/2+(taille_bloc*0), H/2],
    [W/2+(taille_bloc*1), W/2, H/2+(taille_bloc*1), H/2],
    [W/2+(taille_bloc*2), W/2, H/2+(taille_bloc*2), H/2],
    [W/2+(taille_bloc*3), W/2, H/2+(taille_bloc*3), H/2]
]

# Liste des couleurs utilisés dans le programme:
colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    '#6CBB3C',  # Vert
]

# Fonctions

def haut(event):
    '''Fonction qui change la direction du serpent vers le haut.'''
    global etat
    if etat == 4 or etat == 6:      # S'assure que le serpent ne puisse faire demi-tour.
        etat = 8

def bas(event):
    '''Fonction qui change la direction du serpent vers le bas.'''
    global etat
    if etat == 4 or etat == 6:      # Idem
        etat = 2

def droite(event):
    '''Fonction qui change la direction du serpent vers la droite.'''
    global etat
    if etat == 8 or etat == 2:      # Idem
        etat = 6

def gauche(event):
    '''Fonction qui change la direction du serpent vers la gauche.'''
    global etat
    if etat == 8 or etat == 2:      # Idem
        etat = 4

def ecran_game_over():
    '''Fonction qui dessine l'écran de fin de partie.'''
    global game_over
    game.delete(ALL)
    game.create_text(W/2-25, H/2-25, text='Game \n over')
    game_over = True                # Marque la partie comme terminé

def hors_limite(x:int, y:int):
    '''Fonction qui arrête la partie si le serpent sort de la carte.'''
    if x >= W+taille_bloc or y >= H+taille_bloc or x <= 0-taille_bloc or y <= 0-taille_bloc:
        ecran_game_over()  

def suicide(x:int, y:int):
    '''Fonction qui arrête la partie si le serpent se mord la queue.'''
    print(x, y)
    for i in range(4, taille_serpent):
        if serpent[i][0] == x  or serpent[i][1] == y :
            ecran_game_over()

def tete():
    '''Fonction qui change la position de la tête en fonction de la direction.'''
    global origine
    origine = list(serpent)
    if etat == 6:
        serpent[0] = [serpent[0][0]+taille_bloc, serpent[0][1], serpent[0][2]+taille_bloc, serpent[0][3]]
    if etat == 4:
        serpent[0] = [serpent[0][0]-taille_bloc, serpent[0][1], serpent[0][2]-taille_bloc, serpent[0][3]]
    if etat == 8:
        serpent[0] = [serpent[0][0], serpent[0][1]-taille_bloc, serpent[0][2], serpent[0][3]-taille_bloc]
    if etat == 2:
        serpent[0] = [serpent[0][0], serpent[0][1]+taille_bloc, serpent[0][2], serpent[0][3]+taille_bloc]

def deplacement():
    '''Fonction qui deplace le reste du corps du serpent.'''
    tete()
    for i in range(1,taille_serpent):
        serpent[i] = origine[i-1]
    for i in range(0,taille_serpent):   # Efface l'ancien dernier bloc du serpent.
        game.create_rectangle(serpent[i], width=taille_bloc , outline=colour[2], fill=colour[2])
    game.create_rectangle(origine[taille_serpent-1], width=taille_bloc, outline=colour[1], fill=colour[1])
    hors_limite(serpent[0][0], serpent[0][1])
    if taille_serpent < 4:              # Afin d'éviter que la partie s'arrête sans que le serpent ne se soit mordu le corps.
        suicide(serpent[0][0], serpent[0][1])
    if game_over == False:              # Arrête le serpent quand la partie est finie.
        game.after(100, deplacement)

def nouvelle_partie():
    '''Fonction qui commence une nouvelle partie.'''
    global game_over, serpent, etat
    game.delete(ALL)
    serpent = list(serpent_base) ; game_over = False ; etat = 6
    deplacement()

# Widgets

win = Tk()
win.title('Snake')

game = Canvas(win, width=W, height=H, bg=colour[1])
game.grid(rowspan=14, column=1)

# Assignation des touches directionnelles pour choisir la direction du serpent
win.bind('<KeyPress-Up>', haut)
win.bind('<KeyPress-Down>', bas)
win.bind('<KeyPress-Left>', gauche)
win.bind('<KeyPress-Right>', droite)

but1 = Button(win, text='Nouvelle \n partie', fg=colour[0], bg=colour[1], command=nouvelle_partie)
but1.grid(row=1, column=0)

but2 = Button(win, text='Quitter', fg=colour[0], bg=colour[1], command=win.quit)
but2.grid(row=13, column=0)

win.mainloop()