# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""
 
    def creer_labyrinthe_depuis_chaine(self,chaine):
            ligne=[]
            tableau=[]
            chaine=chaine.split("\n")
            for l in chaine:
                for c in l:
                    if c!="\n":
                        ligne.append(c)
                tableau.append(ligne)
                ligne=[]
            print(tableau)
            return tableau   

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    

