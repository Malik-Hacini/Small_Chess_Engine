import plateau



class joueur():
    def __init__(self,nom : str,couleur : bool, pieces : dict) -> None:
        """création un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True -> blanc, False -> noir
        """
        self.nom = nom
        self.couleur = couleur
        self.pieces = pieces 


class humain(joueur):
    def __init__(self, nom: str, couleur: bool, pieces: dict) -> None:
        super().__init__(nom, couleur, pieces)
        
    
    def jouer_coup(self,plateau : plateau) -> None:
        #donner les positions des pieces
        print("voici vos pieces")
        for piece in self.pieces:
            print(f"{piece.nom} : {piece.coord}")
        
        #demander la case à veut jouer
            #vérifier si elle possedes des coups possibles
        coup_jouable  = False
        while not coup_jouable:
            
            piece_existe = False
            while not piece_existe:
                p = input("quelle sont les coordonnées de la pièce à bouger?")
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(p)==2:print("ce n'est pas un coup valide!")
                
                elif p[0] not in ("a","b","c","d","e","f","g","h") or p[1] not in ("1","2","3","4","5","6","7","8"):print("Ce n'est pas un coup valide!")
                
                #vérifier si la piece est au joueur
                elif p not in [piece.coord for piece in self.piece]:print("Cette case ne comporte pas de piece de votre couleur.")
                #vérifier que la piece peut etre bougée
                elif p.coups_possible() == None : print("Cette pièce ne peut pas être bougée.")
                #la piece peut etre déplacée
                else : piece_existe = True
                
            #donner les coups possibles pour cette pièce
            coups_possibles =p.coups_possibles()
            print(f"vous pouvez déplacer votre {p.nom[0]} sur les cases suivantes : ", coups_possibles)
            #vérifier si le joueur veut bien jouer cette piece ou modifier son coup
            coup = None
            while coup not in coups_possibles and p is not None:
            
                
                #demander la case où le joueur veut déplacer le pion
                coup = input("Quel coup voulez-vous jouer (None si vous voulez jouer une autre piece)?")
                if coup is "None": p = None
                elif coup not in coups_possibles:print("Ce coup n'est pas valide.")
            
        #déplacer la pièce sur le plateau
        plateau.jouer(p.coord,coup)
        
        
        
        
        
        
#une piece possede:
    #couleur, position