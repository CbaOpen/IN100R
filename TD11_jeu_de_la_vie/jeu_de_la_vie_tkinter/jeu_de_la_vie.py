import tkinter as tk


# initialisation variables globales
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
nb_ligne = 50
nb_colonne = 50
largeur_case = CANVAS_WIDTH // nb_ligne
hauteur_case = CANVAS_HEIGHT // nb_colonne

mort = "M"
vivant = "V"
iterations = 0

grille = []
grille_canvas = []

continuer_jeu = False

def init_grille():
    grille = []
    for _ in range(0,nb_ligne):
        ligne = []
        for _ in range(0,nb_colonne):
            ligne.append(mort)
        grille.append(ligne)

    return grille

def creer_grille_gui():
    global grille_canvas
    for i in range(nb_ligne):
        ligne_canvas = []
        for j in range(nb_colonne):
            ligne_canvas.append(canvas.create_rectangle((j*largeur_case, i*hauteur_case),
                    ((j+1)*largeur_case, (i+1)*hauteur_case), outline="grey",fill="black"))
        grille_canvas.append(ligne_canvas)

def nouveau_jeu():
    global grille, grille_canvas, iterations

    for ligne in grille_canvas:
        for rectangle in ligne:
            canvas.delete(rectangle)
    grille_canvas = []

    grille = init_grille()
    creer_grille_gui()

    iterations=0
    Label_iterations.config(text = f"Nombre d'iterations : {iterations}")



def recup_ligne_col(x,y):
    ligne = -1
    col = -1

    for j in range(0,nb_ligne):
        if j*hauteur_case < y < (j+1)*hauteur_case:
            ligne = j
            break

    for i in range(0,nb_colonne):
        if i*largeur_case < x < (i+1)*largeur_case:
            col = i
            break
        
    return ligne, col

def maj_grille(ligne, col, statut):
    global grille_canvas

    if statut == mort:
        canvas.itemconfig(grille_canvas[ligne][col],fill="black")
    else:
        canvas.itemconfig(grille_canvas[ligne][col],fill="orange")

def change_couleur(event):
    global grille

    if "button" not in str(event.widget):
        ligne, col = recup_ligne_col(event.x, event.y)

        if ligne != -1 and col != -1:
            if grille[ligne][col] == mort:
                grille[ligne][col] = vivant
            else :
                grille[ligne][col] = mort

            maj_grille(ligne,col, grille[ligne][col])
    
def compte_nb_voisins(ligne,col):
    nb_voisin_vivant = 0

    for k in range(-1,2):
        for l in range(-1,2):
            if  not(k == 0 and l == 0): #si c'est pas la cellule ligne,col
                if (0 <= (ligne+k) < nb_ligne) and (0 <= (col+l) < nb_colonne): 
                    if grille[ligne+k][col+l] == vivant:
                        nb_voisin_vivant += 1

    return nb_voisin_vivant   

def jeu_vie_une_iteraction():
    global grille, grille_canvas, iterations

    new_grille = [ligne_cop[:] for ligne_cop in grille] # copie de la grille

    for i in range(0, nb_ligne):
        for j in range(0,nb_colonne):
            nb_voisin_vivant = compte_nb_voisins(i,j)
            
            if grille[i][j] == mort and nb_voisin_vivant == 3:
                new_grille[i][j] = vivant
            elif grille[i][j] == vivant and (nb_voisin_vivant != 2 and nb_voisin_vivant != 3):
                new_grille[i][j] = mort
            maj_grille(i, j, new_grille[i][j])

    grille = new_grille
    iterations += 1
    Label_iterations.config(text = f"Nombre d'iterations : {iterations}")

def jeu_vie_on_off():
    global continuer_jeu

    if bouton_lancer_auto['text'] == "LANCER":
        continuer_jeu = True
        bouton_lancer_auto.config(text="STOP")
        jeu_vie()
    elif bouton_lancer_auto['text'] == "STOP":
        continuer_jeu = False
        bouton_lancer_auto.config(text="LANCER")

def jeu_vie():
    if continuer_jeu:
        jeu_vie_une_iteraction()
        racine.after(1,jeu_vie)
    # while continuer_jeu:
        # jeu_vie_une_iteraction()
        # time.sleep(3)

if __name__ == '__main__':
    """
    Code principal du programme qui initialise l'interface graphique et cree une nouvelle partie
    """
    racine = tk.Tk() # creation fenetre graphique
    racine.title("JEU DE LA VIE") # nom de la fenetre

    canvas = tk.Canvas(racine, background="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT) # creation du canvas de largeur CANVAS_WIDTH, de hauteur CANVAS_HEIGHT et de couleur noire
    
    Label_iterations = tk.Label(racine,text=f"Nombre d'iterations : {iterations}",font = ("helvetica", "20"))
    
    bouton_new_game = tk.Button(racine, text="NOUVELLE PARTIE",font = ("helvetica", "20"), command=nouveau_jeu)  # creation du bouton "nouvelle partie" et qui appel la fonction pendu
    bouton_quitter = tk.Button(racine, text="QUITTER", font = ("helvetica", "20"), command=racine.destroy) # creation du bouton "quitter" et qui appel la fonction racine.destroy (permet de fermer la fenetre et quitter le jeu)
    
    bouton_lancer_auto = tk.Button(racine, text="LANCER",font = ("helvetica", "20"), command=jeu_vie_on_off)
    bouton_lancer_une_it = tk.Button(racine, text="LANCER une\n iteration",font = ("helvetica", "20"), command=jeu_vie_une_iteraction)

    racine.bind("<Button-1>", change_couleur)

    Label_iterations.grid(row=0,column=0,columnspan=2)
    canvas.grid(row=1, column=0,rowspan=4)
    bouton_new_game.grid(row=1, column=1) # placement colonne à droite du canvas
    bouton_lancer_auto.grid(row=2,column=1)
    bouton_lancer_une_it.grid(row=3,column=1)
    bouton_quitter.grid(row=4,column=1) # placement colonne à droite du canvas


    nouveau_jeu()

    racine.mainloop() # boucle principale

