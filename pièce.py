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

    def __init__(self, couleur=None, coord=None):
        '''
        param: 
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple(int, int) (obssice(1-8), ordonnée(1-8)) ou None si la pièce n'est pas sur le plateau
        '''
        self.couleur=couleur
        self.coord=coord
    
    def __str__(self):
        return " "



class Roi(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
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
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        for dy in range(-1,2):
            
            if case_existe(x-1, y+dy) and not case_controlle(x-1, y+dy) and not case_bloque(x-1, y+dy): #Verifier à gauche
                liste_coups.append((x-1, y+dy))
            
            if case_existe(x-1, y+dy) and not case_controlle(x-1, y+dy) and not case_bloque(x-1, y+dy): #Verifier a droite
                liste_coups.append((x-1, y+dy))

        if case_existe(x, y+1) and not case_controlle(x, y+1) and not case_bloque(x, y+1): #Verifie case au dessus
            liste_coups.append((x, y+1))
        
        if case_existe(x, y-1) and not case_controlle(x, y-1) and not case_bloque(x, y-1): #Verifie case en dessous
            liste_coups.append((x, y-1))

        


class Reine(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
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
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        pass


class Fou(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♗"
        else:
            self.symbole="♝"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        pass
    

class Cavalier(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♘"
        else:
            self.symbole="♞"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        pass

class Tour(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♖"
        else:
            self.symbole="♜"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        pass
        

class Pion(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Reine", couleur)
        
        if self.couleur==True:
            self.symbole="♙"
        else:
            self.symbole="♟"

    def __str__(self):
        return self.symbole

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        Input: La piece
        Output: Listes des coups possibles 
        '''
        liste_coups=[]
        x,y= self.coord
        pass
