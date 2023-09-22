'''
Fichier Contenant le comportement des différentes pièces du jeu
'''

class Piece:
    '''
    Les 
    '''

    def __init__(self, couleur, position):
        '''
        param: 
            couleur: Bool (True<=>Blanc, False<=>Noir)
            position: tuple (obssice(1-8), ordonnée(1-8))
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

    def coups_possibles(self):
        '''
        Fonction qui rends la liste des coups de déplacement possible pour cette pièce
        '''
        liste_coups=[]
        x,y= position
        for i in range(-1,2):
            if plateau.existance_case(x-1,y+i) and not plateau.echec(x-1, y+i):
                liste_coups.append(x-1,y+i)

        pass



class Reine(Piece):
    pass

class Fou(Piece):
    pass

class Cavalier(Piece):
    pass

class Tour(Piece):
    pass

class Pion(Piece):
    pass

