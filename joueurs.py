import numpy as np
class Joueur():
<<<<<<< HEAD
    def __init__(self,nom : str,couleur : bool, pieces : list = []) -> None:
=======
    def __init__(self,nom : str,couleur : bool) -> None:
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        """création d'un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True -> blanc, False -> noir
        """
        self.nom = nom
        self.couleur = couleur
        self.pieces = []


class Humain(Joueur):
<<<<<<< HEAD
    def __init__(self, nom: str, couleur: bool, pieces: list= []) -> None:
        super().__init__(nom, couleur, pieces)
        
    
    def jouer_coup(self,partie: dict) -> None:
=======
    def __init__(self, nom: str, couleur: bool) -> None:
        super().__init__(nom, couleur)
        
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147

        #demander la case à veut jouer
            #vérifier si elle possedes des coups possibles
        coup_jouable  = False
        while not coup_jouable:
            
<<<<<<< HEAD
            piece_existe = False
            
            while not piece_existe:
                p = input("Ou est la pièce à bouger ? \n")
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(p)==2:print("ce n'est pas un coup valide! IL DOIT Y AVOIR 2 CHARACTERES \n")
                
                elif p[0] not in ("A","B","C","D","E","F","G","H") or p[1] not in ("1","2","3","4","5","6","7","8"):print("Ce n'est pas un coup valide! \n")
                else : 
                    #vérifier si la piece est au joueur
                    
                    p = (ord(p[0])-65,int(p[1])-1)
                    if p not in [piece.coord for piece in self.pieces]: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[p].coups_possibles(partie) == None : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_existe = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles =partie.plateau[p].coups_possibles(partie)
            print(f"vous pouvez déplacer votre {partie.plateau[p].nom} sur les cases suivantes : ", coups_possibles)
            #vérifier si le joueur veut bien jouer cette piece ou modifier son coup
            coup = None
            while coup not in coups_possibles and p is not None:
=======
            piece_deplacable = False
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
            
            while not piece_deplacable:
                coord_p = input(f"{self.nom}, ou est la pièce à bouger ? \n")
                
                if coord_p == "save" : return "save"
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(coord_p)==2:
                    print("ce n'est pas un coup valide! IL DOIT Y AVOIR 2 CHARACTERES \n")
                
                elif coord_p[0] not in ("A","B","C","D","E","F","G","H") or coord_p[1] not in ("1","2","3","4","5","6","7","8"):
                    print("Ce n'est pas un coup valide! \n")
                
                
                else : 
                    #Transformation de la position de la pièce de notation algébrique aux coordonnées absolues dans le plateau.
                    #Pour la ligne, cela dépend de la couleur du joueur, l'affichage étant renversé quand les noirs jouent.
                    coord_p = (ord(coord_p[0])-65,int(coord_p[1])-1)
                    
                    
                    
                    if coord_p not in partie.plateau.keys() : print("Cette case est vide.")
                    
                    elif partie.plateau[coord_p] not in self.pieces: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[coord_p].coups_possibles(partie) == [] : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_deplacable = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles=partie.plateau[coord_p].coups_possibles(partie)
            
            
                
                
            coups_a_afficher_not_alg=[(chr(coup[0]+65)+str(coup[1]+1)) for coup in coups_possibles]
            
            coups_a_afficher_output=""
            for coup in coups_a_afficher_not_alg:
                coups_a_afficher_output+=f"{coup}, "
            
            
            print(f"vous pouvez déplacer votre {partie.plateau[coord_p].nom} sur les cases suivantes : ", coups_a_afficher_output[:-2]+".")
            #vérifier si le joueur veut bien jouer cette piece ou modifier son coupS
            coup_int = None
            premier_passage=True
            while coup_int not in coups_possibles:
                
                if not premier_passage:
                    print("Ce coup n'est pas valide. \n")
                
                #demander la case où le joueur veut déplacer le pion
                coup = input("Quel coup voulez-vous jouer (None si vous voulez jouer une autre piece)? \n")
<<<<<<< HEAD
                if coup is "None": p = None
                elif coup not in coups_possibles: print("Ce coup n'est pas valide. \n")
            
        #déplacer la pièce sur le plateau
        partie.plateau.jouer(p,coup)
=======

                coup_int = (ord(coup[0])-65,int(coup[1])-1)
                        
                premier_passage=False
            coup_jouable=True

        return coord_p,coup_int
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        
class IA(Joueur):
    def __init__(self, nom: str, couleur: bool, pieces:list = []) -> None:
        super().__init__(nom, couleur, pieces)      
    pass    
        
        
        