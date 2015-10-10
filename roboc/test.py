#!/usr/bin/python
# -*-coding:Utf-8 -*


import os

def creer_labyrinthe_depuis_chaine(chaine):

    ligne=[]
    tableau=[]
    print("debut")
    chaine=chaine.split("\n")
    
    for l in chaine:
        for c in l:
            if c!="\n":
                ligne.append(c)
        tableau.append(ligne)
        ligne=[]
    print(tableau)
    return tableau


for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
            #print("tableau: {}".format(contenu))
    creer_labyrinthe_depuis_chaine(contenu)

