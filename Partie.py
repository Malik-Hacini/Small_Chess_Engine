from joueurs import*
from pièce import*
import numpy as np

class Partie:
    
    """Partie de jeu d'échecs
    """
    def __init__(self,j1 :Joueur, j2:Joueur, plateau: np.ndarray = None):
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
        """
        if plateau is None:
            plateau=np.full((8,8),Piece())

            plateau[1]=[Pion(False) for i in range(8)]
            plateau[6]=[Pion(True) for i in range(8)]

            for couleur in [True,False]:
                if couleur: ligne=7
                else: ligne = 0
                
                for col in [0,7]:
                    plateau[ligne,col]=Tour(couleur)
                for col in [1,6]:
                    plateau[ligne,col]=Cavalier(couleur)
                for col in [2,5]:
                    plateau[ligne,col]=Fou(couleur)   
                
                plateau[ligne,3]=Reine(couleur)
                plateau[ligne,4]=Roi(couleur)
        self.plateau=plateau
        j1.pieces=[i for x in plateau for i in x if i.couleur==j1.couleur]
        j2.pieces=[i for x in plateau for i in x if i.couleur==j2.couleur]
        self.j1=j1
        self.j2=j2
    

    def __str__(self)->str:
        """méthode print pour la partie. Affiche le plateau dans
        son état actuel

        Returns:
            str: Le plateau.
        """
        
        p=""
        i=0
        num_ligne=[str(x) for x in range(8)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        p+="    " +  "    ".join(nom_col) +"\n"
        for ligne in self.plateau:
            
            p+=num_ligne[i] + "   "
            i+=1
            
            for piece in ligne:
                p+=piece.__str__() + "  | "
            p+=  "\n" + "   "+ "-"*41 + "\n"
        p+=" "*5 +  "    ".join(nom_col) 
            
             
        return p
    
    def deplacer_piece(self, coord1: tuple[int,int], coord2: tuple[int, int])->np.ndarray:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord1 (tuple[int,int]): Position de la pièce à déplacer
            coord2 (tuple[int,int]): Position finale de la pièce
        Returns:
            np.ndarray: Le plateau modifié
            """

        self.plateau[coord1[0],coord1[1]] , self.plateau[coord2[0],coord2[1]] = Piece(), self.plateau[coord1[0],coord1[1]]

j1=Humain("Malik",1)
j2=Humain("Basile", 0)
p=Partie(j1,j2)

p.deplacer_piece((0,0),(3,3))
print(p)
for i in enumerate(j1.pieces):
    print(i)