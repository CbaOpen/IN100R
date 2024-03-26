import random
import tkinter as tk
from mots import mots

# initialisation variables globales
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
dx = 30
dy = 30

mot = ""
lettres_mot = set(mot)
alphabet = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
lettres_utilisees = set()
vies = 7
objet_a_effacer = []



def choisi_mot():
    """
    Choisi un mot aleatoirement dans la liste mots et la renvoie en majuscule
    """
    mot = random.choice(mots)
    return mot.upper()


def poteau1():
    """
    dessine le poteau vertical
    """
    pass
    # ligne_pied = 
    # objet_a_effacer.append(ligne_pied)

    
    # ligne_verticale = 
    # objet_a_effacer.append(ligne_verticale)


def poteau2():
    """
    dessine le poteau horizontal en haut
    """
    pass
    
    # ligne_horizontale = 
    # objet_a_effacer.append(ligne_horizontale)
    
    # ligne_diago = 
    # objet_a_effacer.append(ligne_diago)


def tete():
    """
    dessine la tete du pendu
    """
    x0 = 2*CANVAS_WIDTH/3
    y0 = CANVAS_HEIGHT/4
    x1 = x0
    y1 = y0 + dy*2
    objet_a_effacer.append(canvas.create_line((x0,y0),(x1,y1), fill="white",width=5))

    x0 = x0 - dx
    y0 = y1
    x1 = x1 + dx
    y1 = y1 + 2*dy
    objet_a_effacer.append(canvas.create_oval((x0,y0), (x1,y1), outline="white", width=5))

    # Oeil gauche
    centre_gauche_x = 2*CANVAS_WIDTH/3 - dx/4
    centre_gauche_y = CANVAS_HEIGHT/4 + dy*2.8
    x0 = centre_gauche_x - dx/4
    y0 = centre_gauche_y - dy/4
    x1 = centre_gauche_x + dx/4
    y1 = centre_gauche_y + dy/4
    objet_a_effacer.append(canvas.create_line((x0,y0),(x1,y1), fill="white"))

    x0 = centre_gauche_x + dx/4
    y0 = centre_gauche_y - dy/4
    x1 = centre_gauche_x - dx/4
    y1 = centre_gauche_y + dy/4
    objet_a_effacer.append(canvas.create_line((x0,y0),(x1,y1), fill="white"))

    #Oeil droit
    centre_gauche_x = 2*CANVAS_WIDTH/3 + dx/4
    centre_gauche_y = CANVAS_HEIGHT/4 + dy*2.8
    x0 = centre_gauche_x - dx/4
    y0 = centre_gauche_y - dy/4
    x1 = centre_gauche_x + dx/4
    y1 = centre_gauche_y + dy/4
    objet_a_effacer.append(canvas.create_line((x0,y0),(x1,y1), fill="white"))

    x0 = centre_gauche_x + dx/4
    y0 = centre_gauche_y - dy/4
    x1 = centre_gauche_x - dx/4
    y1 = centre_gauche_y + dy/4
    objet_a_effacer.append(canvas.create_line((x0,y0),(x1,y1), fill="white"))


def corps():
    """
    dessine le corps du pendu
    """
    pass
    # corps = 
    # objet_a_effacer.append(corps)


def bras():
    """
    dessine les bras du pendu
    """
    pass
    
    # bras_gauche = 
    # objet_a_effacer.append(bras_gauche)
    
    # bras_droit = 
    # objet_a_effacer.append(bras_droit)


def jambe_gauche():
    """
    dessine la jambe gauche
    """
    pass
    
    # jambe_gauche = 
    # objet_a_effacer.append(jambe_gauche)


def jambe_droite():
    """
    dessine la jambe droite
    """
    pass
    
    # jambe_droite = 
    # objet_a_effacer.append(jambe_droite)

visu_tk=[jambe_droite,jambe_gauche,bras,corps,tete,poteau2,poteau1]




def test_nouvelle_lettre(event):
    """
    Lorsque l'utilisateur entre une nouvelle lettre, le porgramme appelle cette fonction
    qui test si la lettre est :
    - valide
    - comprise dans le mot à trouver : si oui, découvre la lettre dans le mot à trouver, sinon enlève une vie
    Puis la fonction met à jour le l'interface graphique :
    - les infos sur les lettres utilisées
    - le visuel du pendu
    - le mot à trouver
    """
    global mot, lettres_mot, alphabet, lettres_utilisees, vies
    
    nouvelle_lettre = user_entry.get().upper() # recupère la lettre donnée par l'utilisateur
    user_entry.delete(0, tk.END) # supprime la lettre de la zone d'entree de text

    # verifie que la lettre est dans le mot et non utilisée
    if nouvelle_lettre in alphabet - lettres_utilisees:
        lettres_utilisees.add(nouvelle_lettre)
        if nouvelle_lettre in lettres_mot:
            lettres_mot.remove(nouvelle_lettre)
        else:
            vies = vies - 1  # takes away a life if wrong

    # met à jour les informations 
    label_vies_lettres.config(text=f"Vous avez {vies} vies et vous avez utilisé les lettres :\n {' '.join(lettres_utilisees)}")
    liste_mot = [lettre if lettre in lettres_utilisees else '-' for lettre in mot]
    canvas.itemconfigure(label_mot_cache,text=' '.join(liste_mot))
    
    # met à jour le visuel du pendu
    if vies < 7:
        visu_tk[vies]()

    # verifie si le joueur a plus de vie (perdu) ou si le mot a été trouvé (gagne)
    if vies == 0:
        centre_x = CANVAS_WIDTH/2
        centre_y = 100
        info_perd = canvas.create_text(centre_x, centre_y) # affichier le message apres avoir perdu
        objet_a_effacer.append(info_perd)
    elif len(lettres_mot) == 0:
        centre_x = CANVAS_WIDTH/2
        centre_y = 100
        info_gagne = canvas.create_text(centre_x, centre_y) # affichier le message apres avoir gagné
        objet_a_effacer.append(info_gagne)



def pendu():
    """
    Initialise une nouvelle partie de pendu. Cette fonction est appelée dès le lancement du programme ou lorsque l'utilisateur
    clique sur le bouton nouvelle partie.
    - Efface les infos et le visuel de la partie précédente
    - initialise un nouveau mot, le nombre de vie
    """
    global mot, lettres_mot, alphabet, lettres_utilisees, vies, objet_a_effacer
    
    # efface les dessins sur le canvas 
    for objet in objet_a_effacer:
        canvas.delete(objet)
    objet_a_effacer=[]

    # initialisation de la partie
    mot = choisi_mot() 
    lettres_mot = set(mot)
    lettres_utilisees = set()
    vies = 7
    
    label_vies_lettres.config(text=f"Vous avez {vies} vies et vous avez utilisé les lettres :\n {' '.join(lettres_utilisees)}")

    liste_mot = [lettre if lettre in lettres_utilisees else '-' for lettre in mot]
    canvas.itemconfigure(label_mot_cache,text=' '.join(liste_mot))
    
    



if __name__ == '__main__':
    """
    Début du programme :
    - initialisation de l'interface graphique : creation de tous les widgets et leurs placement
    - appel à la fonction pendu à la fin pour lancer une nouvelle partie directement
    """
    
    racine =  # creation fenetre graphique
    racine.title("Jeu du pendu") # nom de la fenetre

    canvas =  # creation du canvas de largeur CANVAS_WIDTH, de hauteur CANVAS_HEIGHT et de couleur noire
    bouton_new_game =   # creation du bouton "nouvelle partie" et qui appel la fonction pendu
    bouton_quitter =  # creation du bouton "quitter" et qui appel la fonction racine.destroy (permet de fermer la fenetre et quitter le jeu)
    
    user_entry = tk.Entry(racine,font = ("helvetica", "20")) # creation d'une zone d'entree de text
    user_entry.bind("<Return>", test_nouvelle_lettre) # lie la zone d'entree à la fonction test_nouvelle_lettre (gestion d'évènement)
    
    label_vies_lettres =  # creation d'un label qui permet d'afficher le nombre de vie et de lettres utilisees. l'argument text=""
    label_user_entry =  # label devant la zone d'entre de texte qui indique à l'utilisateur de rentrer une nouvelle lettre
    label_mot_cache = canvas.create_text(CANVAS_WIDTH/2,50,text="", fill="white", font = ("helvetica", "20")) # creation d'une zone de text dans le canvas qui affichera le mot à trouver
    
    canvas.grid(row=0, column=0,columnspan=2,rowspan=2) # placement du canvas
    bouton_new_game.grid() # placement colonne à droite du canvas
    bouton_quitter.grid() # placement colonne à droite du canvas

    
    label_vies_lettres.grid() # placement en dessous du canvas
    user_entry.grid() # placmement en dessous du canvas, à droite du label label_user_entry
    label_user_entry.grid() # placmement en dessous du canvas, à gauche de la zone d'entree de text
    
    pendu() # cree une premiere partie

    racine.mainloop() # boucle principale
