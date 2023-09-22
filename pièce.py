'''
Fichier Contenant le comportement des différentes pièces du jeu
'''

def existance_case(x,y):
    '''
    Vérifie si la case x,y existe
    Input: coordonnées x,y de la case
    Output: Bool True=> Case existe, False=> Case n'existe pas
    '''
    if 0>x or x>8:
        return False
    elif 0>y or y>8:
        return False
    else:
        return True


class Piece:
    '''
    
    '''

    def __init__(self, couleur, position=None):
        '''
        param: 
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple(int, int) (obssice(1-8), ordonnée(1-8)) ou None si la pièce n'est pas sur le plateau
        '''
        self.couleur=couleur
        self.position=position



class Roi(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Roi", couleur)
        
        if self.couleur==True:
            self.symbole="♔"
        else:
            self.symbole="♚"

    def __str__(self):
        return self.symbole


    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: Piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.position
        for dy in range(-1,2):
            
            if case_existe(x-1, y+dy) and not case_controlle(x-1, y+dy) and not case_bloque(x-1, y+dy): #Verifier à gauche
                liste_coups.append((x-1, y+dy))
            
            if case_existe(x-1, y+dy) and not case_controlle(x-1, y+dy) and not case_bloque(x-1, y+dy): #Verifier a droite
                liste_coups.append((x-1, y+dy))


            


class Reine(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♕"
        else:
            self.symbole="♛"

        def __str__(self):
            return self.symbole


    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: Piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.position
        pass


class Fou(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♗"
        else:
            self.symbole="♝"

    def __str__(self):
            return self.symbole
    

class Cavalier(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♘"
        else:
            self.symbole="♞"

    def __str__(self):
            return self.symbole

class Tour(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♖"
        else:
            self.symbole="♜"

    def __str__(self):
            return self.symbole

class Pion(Piece):
    
    def __init__(self, couleur, position):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, position) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♙"
        else:
            self.symbole="♟"

    def __str__(self):
            return self.symbole

