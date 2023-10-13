import numpy as np
class Joueur():
    def __init__(self,nom : str,couleur : bool) -> None:
        """création d'un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True -> blanc, False -> noir
        """
        self.nom = nom
        self.couleur = couleur
        self.pieces = []


class Humain(Joueur):
    def __init__(self, nom: str, couleur: bool) -> None:
        super().__init__(nom, couleur)
        
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:

        #demander la case à veut jouer
            #vérifier si elle possedes des coups possibles
        coup_jouable  = False
        while not coup_jouable:
            
            piece_deplacable = False
            
            while not piece_deplacable:
                coord_p = input(f"{self.nom}, ou est la pièce à bouger ? \n")
                
                if coord_p == "save" : return "save"
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(coord_p)==2:
                    print("ce n'est pas un coup valide! IL DOIT Y AVOIR 2 CHARACTERES \n")
                
                elif coord_p[0] not in ("a","b","c","d","e","f","g","h") or coord_p[1] not in ("1","2","3","4","5","6","7","8"):
                    print("Ce n'est pas un coup valide! \n")
                
                
                else : 
                    #Transformation de la position de la pièce de notation algébrique aux coordonnées absolues dans le plateau.
                    #Pour la ligne, cela dépend de la couleur du joueur, l'affichage étant renversé quand les noirs jouent.
                    coord_p = (ord(coord_p[0])-97,int(coord_p[1])-1)
                    
                    
                    
                    if coord_p not in partie.plateau.keys() : print("Cette case est vide.")
                    
                    elif partie.plateau[coord_p] not in self.pieces: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[coord_p].coups_legaux(partie) == [] : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_deplacable = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles=partie.plateau[coord_p].coups_legaux(partie)
            
            
                
                
            coups_a_afficher_not_alg=[(chr(coup[0]+97)+str(coup[1]+1)) for coup in coups_possibles]
            
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

                coup_int = (ord(coup[0])-97,int(coup[1])-1)
                        
                premier_passage=False
            coup_jouable=True

        return coord_p,coup_int
        
class IA(Joueur):
    def __init__(self, nom: str, couleur: bool, pieces:list = []) -> None:
        super().__init__(nom, couleur, pieces)      
    pass    
        
        
        