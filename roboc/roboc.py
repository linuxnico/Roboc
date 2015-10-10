# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
    cartes.append(Carte(nom_carte,contenu))
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

while True:
    try:
        numC=int(input("entrer le numero de carte choisi:"))
        break
    except:
        print("il faut un NUMERO!!! Reessayez\n")
        
print("c\'est parti!! on va jouer avec le labyrinthe numero {}".format(numC))



# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
