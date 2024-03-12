"""
Jeu du pendu.
Pensez à revoir le cours sur les listes, notamment la fin sur les set
"""


import random
from mots import mots
from visuel_vies import visuel_vies

# Choisi aleatoirement un mot et le retourne en majuscule
def choisi_mot():
    pass


def pendu():
    mot =  # mot aleatoire
    lettres_mot =  # recupere les lettes du mot sans les doublons
    alphabet = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
    lettres_utilisees = set() # les lettres utilisees

    vies = 0 # nombre de vies

    while : # Quels sont les conditions pour pouvoir continuer a jouer et proposer de nouvelles lettres ?

        print(f"Vous avez {vies} vies et vous avez utilisez les lettres : {' '.join(lettres_utilisees)}")

        liste_mot = [] # Le mot sous forme de liste. Si l'utilisateur a trouve une des lettres, la mettre sinon mettre "-"
        print() # print le visuel du nombre de vie
        print('Mot actuel : ', ' '.join(liste_mot))

        nouvelle_lettre =  # demande une nouvelle lettre a l'utilisateur et la mettre en majuscule
        if nouvelle_lettre in alphabet - lettres_utilisees: # si la nouvelle lettre est dans l'alphabet et pas dans celle deja utilisees
            # ajouter la nouvelle lettre dans celles utilisees (pour ajouter dans un set, utiliser : truc_set.add(qqc))
            # Faire une condition qui permet d'enlever la nouvelle lettre du set lettres_mot (si elle est dedans) ou qui enlève une vie et print que la lettre n'est pas dans le mot (sinon) 
            # (pour enlever qqc dans un set, utiliser : truc_set.remove(qqc))


        elif : # Si la nouvelle lettre est dans celles utilisees
            print('\nVous avez déjà utilisée cette lettre, choisissez-en une autre.')

        else:
            print('\nCe n\'est pas une lettre valide.')

    # Ecrire la fin du programme : si l'utilisateur a perdu ou gagné
    

if __name__ == '__main__':
    pendu()