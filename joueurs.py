import numpy as np
class Joueur():
    def __init__(self,nom : str,couleur : bool, pieces : list = []) -> None:
        """création d'un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True -> blanc, False -> noir
        """
        self.nom = nom
        self.couleur = couleur
        self.pieces = pieces 


class Humain(Joueur):
    def __init__(self, nom: str, couleur: bool, pieces: list= []) -> None:
        super().__init__(nom, couleur, pieces)
        
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:

        #demander la case à veut jouer
            #vérifier si elle possedes des coups possibles
        coup_jouable  = False
        while not coup_jouable:
            
            piece_existe = False
            
            while not piece_existe:
                coord_p = input("Ou est la pièce à bouger ? \n")
                
                if coord_p == "save" : return "save"
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(coord_p)==2:
                    print("ce n'est pas un coup valide! IL DOIT Y AVOIR 2 CHARACTERES \n")
                
                elif coord_p[0] not in ("A","B","C","D","E","F","G","H") or coord_p[1] not in ("1","2","3","4","5","6","7","8"):
                    print("Ce n'est pas un coup valide! \n")
                    
                else : 
                    #vérifier si la piece est au joueur
                    
                    coord_p = (ord(coord_p[0])-65,int(coord_p[1])-1)
                    if coord_p not in [piece.coord for piece in self.pieces]: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[coord_p].coups_possibles(partie) == None : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_existe = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles =partie.plateau[coord_p].coups_possibles(partie)
            
            coups_possibles_not_alg=[(chr(coup[0]+65)+str(coup[1]+1)) for coup in coups_possibles]
            
            coups_possibles_output=""
            for coup in coups_possibles_not_alg:
                coups_possibles_output+=f"{coup}, "
            
            
            print(f"vous pouvez déplacer votre {partie.plateau[coord_p].nom} sur les cases suivantes : ", coups_possibles_output[:-2]+".")
            #vérifier si le joueur veut bien jouer cette piece ou modifier son coupS
            coup_int = None
            while coup_int not in coups_possibles and coord_p is not None:
            
                
                #demander la case où le joueur veut déplacer le pion
                coup = input("Quel coup voulez-vous jouer (None si vous voulez jouer une autre piece)? \n")
                coup_int=(ord(coup[0])-65,int(coup[1])-1)
                if coup_int is "None": coord_p = None
                elif coup_int not in coups_possibles: print("Ce coup n'est pas valide. \n")
            coup_jouable=True

        return coord_p,coup_int
        
class IA(Joueur):
    def __init__(self, nom: str, couleur: bool, pieces:list = []) -> None:
        super().__init__(nom, couleur, pieces)      
    pass    
        
        
        