import numpy as np
from pièce import*

class Plateau(np.ndarray):
    """Plateau de jeu d'échecs
    """
    def __init__(self):
        """Crée un plateau de début de partie d'échecs, en
        tant qu'array numpy.
        """
        
        plateau=np.full((8,8),Pion(False))

        plateau[1]=[Pion(False) for i in range(8) ]
        plateau[6]=[Pion(True) for i in range(8)]

        for couleur in [True,False]:
            if couleur: ligne=7
            else: ligne = 0
            
            for col in [1,6]:
                plateau[ligne,col]=Cavalier(couleur)
            for col in [2,5]:
                plateau[ligne,col]=Fou(couleur)   
            
            plateau[ligne,3]=Reine(couleur)
            plateau[ligne,4]=Roi(couleur)
        
            
    def __str__(self):
        
        for ligne in self:
            for piece in ligne:
                print(piece)
                
p=Plateau()
print(p)