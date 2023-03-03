# Cahier des charges du jeu Snake

## Membres du projet

- Maxime Lefèvre  
- Pierre Fernagu--Berthier  

## But du jeu

Manger le plus de pommes possibles dans un espace restreint.  

## Règles du jeu

- La partie est finie lorsque le serpent sort de la carte ou qu'il se mord la queue.  
- Dès qu'une pomme est avalée, la queue du serpent s'agrandit.  
- Une pomme vaut un point.  
- La vitesse du serpent est constante durant toute la partie.  

## Étapes de la création du jeu

1. Faire le système du mouvement du serpent (Pierre), et du placement des pommes + système du score (Maxime).  
2. Mettre ensemble les deux parties du code.  
3. Corriger les derniers bugs.  

## Caractéristiques

### Serpent

Le serpent est divisé en bloc de forme carré. La longueur d'un côté du carré est égale à la hauteur de la carte divisée par 20. Le serpent commence avec 4 blocs puis dès qu'il mange une pomme, le serpent grandit d'un bloc.  
La couleur du serpent est un vert qui correspond au code hexadécimal suivant : #6CBB3C.  

### Pomme

Une pomme fait la taille d'un bloc dont les côtés font la même taille que les côtés composant les blocs du serpent. Les pommes sont placées de façon aléatoire sur la carte.  
Les couleurs des pommes sont aussi aléatoires, choisis dans un ensemble de couleurs prédéfinies. Les codes hexadécimaux des couleurs sont les suivants : #FF0000 pour le rouge, #8db600 pour le vert et #FFA500 pour l'orange.  
### Carte

La carte est égale à la taille du canevas sur laquelle elle est dessinée. La carte est blanche. La carte est de forme carrée.  

### Interface

Les boutons ainsi que le score sont situés à droite du canevas. En haut, se trouve le score de la partie en cours. Puis, en dessous se trouve le bouton pour commencer la partie. En bas, se trouve le bouton pour quitter le jeu.  
Le nom de la fenêtre est *Snake*.  
Nous utilisons la librairie Tkinter pour l'interface graphique ainsi que le jeu.  

## Bugs connus

- Sur des ordinateurs peu puissants, le jeu peut commencer à ralentir et devenir injouable. Ceci est une limitation du choix de langage de programmation et de la librairie pour l'interface.  
- Le jeu ne fonctionne pas si la résolution du jeu est changé de la valeur de base, 600 pixels par 600 pixels.  
- La pomme peut très rarement venir se positionner dans le serpent, effacent la pomme et, mais ne comptabilisant pas le point. Afin de marquer le point, il faut avaler la pomme invisible. Néanmoins, ceci est très rare.  

## Captures d'écran 

Interface principale  
![Image](Screenshots/Main_Window.png)

Écran de fin de partie  
![Image](Screenshots/Game_Over.png)

Écran de pause  
![Image](Screenshots/Pause.png)
