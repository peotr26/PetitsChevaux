############################
## Jeu du Serpent | Snake ##
############################

from tkinter import *

# Variables

# Tailles du canvas du jeu.
W = 600
H = 600

global taille_serpent
global etat
global taille_bloc
global stop
global game_over

etat = 6                # Variable de la direction du serpent
# 4 = gauche, 6 = droite, 8 = haut, 2 = bas
taille_serpent = 4      # Variable de la taille du serpent.
taille_bloc= int(H/20)  # Variable de la taille d'un carré faisant partie du serpent en fonction de la résolution.
stop = False            # Variable de si le jeu est arrêté.
game_over = False       # Variable de si la partie est finie ou non.

# Liste des coordonnées des blocs du serpent au début d'une partie 
serpent_base = (
    (W/2+(taille_bloc*0), W/2, H/2+(taille_bloc*0), H/2),
    (W/2+(taille_bloc*1), W/2, H/2+(taille_bloc*1), H/2),
    (W/2+(taille_bloc*2), W/2, H/2+(taille_bloc*2), H/2),
    (W/2+(taille_bloc*3), W/2, H/2+(taille_bloc*3), H/2)
)

# Liste des couleurs utilisés dans le programme:
couleur = (
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    '#6CBB3C',  # Vert
    '#FF0000',  # Rouge
)

# Fonctions

# Fonctions pour faire changer la direction du serpent avec le clavier.

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

# Fonctions pour la fin de partie et la gestion des bords de la cartes.

def activer_game_over():
    '''Fonction qui active la fin de partie.'''
    global stop, game_over
    stop = True ; game_over = True      # Arrête le serpent et marque la partie comme finie.
    
def ecran_game_over():
    '''Fonction qui dessine l'écran de fin de partie'''
    game.delete(ALL)
    game.create_text(W/2, H/2, text='Game \n over', font=('Impact', 30), fill=couleur[3])

def hors_limite(x:int, y:int):
    '''Fonction qui arrête la partie si le serpent sort de la carte dans une partie classique.'''
    if x >= W+int(taille_bloc/2) or y >= H+int(taille_bloc/2) or x <= 0-int(taille_bloc/2) or y <= 0-int(taille_bloc/2):
        activer_game_over()
    
def hors_limite_infinie(x:int, y:int):
    '''Fonction qui arrête la partie si le serpent sort de la carte dans une partie infinie.'''
    if x >= W+int(taille_bloc/2):
        serpent[0][0] = serpent[0][0] - (W+taille_bloc) ; serpent[0][2] = serpent[0][2] - (W+taille_bloc)
    elif y >= H+int(taille_bloc/2):
        serpent[0][1] = serpent[0][1] - (W+taille_bloc) ; serpent[0][3] = serpent[0][3] - (W+taille_bloc)
    elif x <= 0-int(taille_bloc/2):
        serpent[0][0] = serpent[0][0] + (W+taille_bloc) ; serpent[0][2] = serpent[0][2] + (W+taille_bloc)
    elif y <= 0-int(taille_bloc/2):
        serpent[0][1] = serpent[0][1] + (W+taille_bloc) ; serpent[0][3] = serpent[0][3] + (W+taille_bloc)
        
def suicide(x:int, y:int):
    '''Fonction qui arrête la partie si le serpent se mord la queue.'''
    print(x, y)
    for i in range(4, taille_serpent):
        if serpent[i][0] == x  or serpent[i][1] == y :
            activer_game_over()

# Fonctions pour le mouvement du serpent.

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

def bordure():
    '''Fonction qui gère les actions du serpent en fonction de son environement et du mode de jeu.'''
    if infinie == False:                # Mode classique
        hors_limite(serpent[0][0], serpent[0][1])
        if taille_serpent < 4:          # Afin d'éviter que la partie s'arrête sans que le serpent ne se soit mordu le corps.
            suicide(serpent[0][0], serpent[0][1])
    if infinie == True:                 # Mode infinie
        hors_limite_infinie(serpent[0][0], serpent[0][1])

def deplacement():
    '''Fonction qui deplace le reste du corps du serpent.'''
    tete()
    for i in range(1,taille_serpent):
        serpent[i] = origine[i-1]
    for i in range(0,taille_serpent):   
        game.create_rectangle(serpent[i], width=taille_bloc , outline=couleur[2], fill=couleur[2])
    effacement()
    bordure()
    if stop == False:                   # Arrête le serpent quand la partie est finie ou que le jeu est en pause.
        game.after(100, deplacement)
    if game_over == True:
        ecran_game_over()

def effacement():
    '''Fonction qui efface la queue du serpent.'''
    global nombre_iteration
    if nombre_iteration > 2:
        game.create_rectangle(origine[taille_serpent-1], width=taille_bloc, outline=couleur[1], fill=couleur[1])    # Efface l'ancien dernier bloc du serpent.
    nombre_iteration += 1
    
# Fonctions pour lancer une partie et la mettre en pause.

def pause(event):
    '''Fonction qui met en pause la partie.'''
    global stop, ecran_pause
    if game_over == True:
        return
    elif stop == False:     # Si le jeu n'est pas déja en arrêter.
        stop = True
        ecran_pause = game.create_text(W/2, H/2, text='Pause', font=('Impact', 30))
    elif stop == True:      #  Relance le jeu si il est arrêter.
        stop = False
        game.delete(ecran_pause)
        deplacement()

def nouvelle_partie_classique():
    '''Fonction qui commence une nouvelle partie.'''
    global stop, serpent, etat, game_over, infinie, nombre_iteration
    game.delete(ALL)
    serpent = list(serpent_base) ; stop = False ; etat = 6 ; game_over = False ; infinie = False ; nombre_iteration = 0
    deplacement()

def nouvelle_partie_infinie():
    '''Fonction qui commence une nouvelle partie.'''
    global stop, serpent, etat, game_over, infinie, nombre_iteration
    game.delete(ALL)
    serpent = list(serpent_base) ; stop = False ; etat = 6 ; game_over = False ; infinie = True ; nombre_iteration = 0
    deplacement()

# Fonctions pour permettre l'utilisation du jeu sans la souris.

def fin_partie(event):
    '''Fonction qui arrête la partie lorsqu'une touche est actionner.'''
    activer_game_over()
    
def quitter(event):
    '''Fonction pour quitter le jeu lorsqu'une touche est actionner.'''
    win.quit()

def lancer_classique(event):
    '''Fonction qui lance une partie classique lorsqu'une touche est actionner.'''
    nouvelle_partie_classique()
    
def lancer_infinie(event):
    '''Fonction qui lance une partie infinie lorsqu'une touche est actionner'''
    nouvelle_partie_infinie()

# Widgets

win = Tk()
win.title('Snake')

game = Canvas(win, width=W, height=H, bg=couleur[1])
game.grid(rowspan=14, column=1)

# Assignation des touches directionnelles pour choisir la direction du serpent
win.bind('<Up>', haut)
win.bind('<Down>', bas)
win.bind('<Left>', gauche)
win.bind('<Right>', droite)

# Assignation de la touche 'p' pour mettre le jeu en pause.
win.bind('<p>', pause)

# Assignation de la touche 'f' pour arrêter la partie.
win.bind('<f>', fin_partie)

# Assignation de la touche 'q' pour quitter le jeu.
win.bind('<q>', quitter)

# Assignation de la touche 'c' pour lancer une partie classique.
win.bind('<c>', lancer_classique)

# Assignation de la touche'i' pour lancer une partie infinie.
win.bind('<i>', lancer_infinie)

but1 = Button(win, text='Nouvelle partie \n classique [c]', fg=couleur[0], bg=couleur[1], command=nouvelle_partie_classique)
but1.grid(row=1, column=0)

but2 = Button(win, text='Nouvelle partie \n infinie [i]', fg=couleur[0], bg=couleur[1], command=nouvelle_partie_infinie)
but2.grid(row=2, column=0)

but3 = Button(win, text='Fin de partie [f]', fg=couleur[0], bg=couleur[1], command=activer_game_over)
but3.grid(row=3, column=0)

but4 = Button(win, text='Quitter [q]', fg=couleur[0], bg=couleur[1], command=win.quit)
but4.grid(row=13, column=0)

win.mainloop()
