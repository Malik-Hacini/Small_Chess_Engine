from joueurs import*
from piece import*
from Plateau import*
import numpy as np
class Partie:
    
    """Partie d'échecs de jeu d'échecs
    """
    def __init__(self,plateau=Plateau(),j1: joueur,j2: joueur):
        self.plateau=plateau
                    
            
                    