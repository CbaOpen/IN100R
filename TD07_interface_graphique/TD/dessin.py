import tkinter as tk
import random 

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500

def dessine_carre():
    """Dessine un carré de largeur 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas."""
    centre_x = # coordonnee x aleatoire du centre du carre
    centre_y = # coordonnee y aleatoire du centre du carre
    mon_canvas.create_rectangle((centre_x - 50, centre_y - 50),
                                (centre_x + 50, centre_y + 50),
                                fill="blue")

def dessine_disque():
    """Dessine un disque de rayon 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas."""
    centre_x =   # coordonnee x aleatoire du centre du cercle 
    centre_y =   # coordonnee y aleatoire du centre du cercle
    mon_canvas.create_oval()  # completer la fonction. Elle prend en arguement les coordonnes des points haut gauche et bas droit du carre imaginaire qui contient le cercle (voir la fonction dessine_carre pour s'aider)

def dessine_croix():
    """Dessine une croix de largeur 50 pixels sur une position aléatoire du canvas
    qui est stocké dans la variable globale mon_canvas. La croix est constituée
    d'une ligne verticale et d'une autre horizontale."""
    centre_x = # coordonnee x aleatoire du centre de la croix
    centre_y = # coordonnee x aleatoire du centre de la croix
    mon_canvas.create_line() # completer la fonction. elle prend en argument les coordonnees des points aux extremites de la ligne
    mon_canvas.create_line() # completer la fonction. elle prend en argument les coordonnees des points aux extremites de la ligne


def change_couleur():
    """Modifie le contenu de la variable globale couleur par une valeur donnée
    par l'utilisateur."""
    global couleur # permet de modifier la variable couleur qui est definie en dehors de la fonction
    couleur = # demande à l'utilisateur une nouvelle couleur


couleur = "blue" #couleur des dessins

racine =  # creation de la fenetre graphique
racine.title("Mon dessin") # donne un nom a la fenetre graphique

### Creation des boutons 

bouton_carre = tk.Button(racine, text="Carré")  # creation du bouton carre
bouton_cercle = # creation du bouton cercle
bouton_croix = # creation du bouton croix
bouton_couleur = # creation du bouton choisir une couleur




mon_canvas =  #creation du canvas, mettre un fond noir avec l'arguement bg

### Placement des differents widget dans la fenetre graphique. Le placement se fait en ligne et colonne
mon_canvas.grid(row=1, column=1, rowspan=3) # emplacement de la zone de dessin. rowspan indique que le canvas se place sur 3 lignes en tout (ici sur les lignes 1, 2 et 3)
bouton_couleur.grid() # placer le bouton au bon endroit
bouton_cercle.grid()  # placer le bouton au bon endroit
bouton_carre.grid()   # placer le bouton au bon endroit
bouton_croix.grid()   # placer le bouton au bon endroit


racine.mainloop()
