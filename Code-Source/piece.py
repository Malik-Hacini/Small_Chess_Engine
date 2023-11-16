from EtatJeu import*
class Piece:
    """Classe destinée à représenter les pièces du jeu d'échec. Chaque pièce
       possède une couleur et une coordonnée (tuple).
       Chaque pièce en particulier est une sous-classe de cette classe (on y définira notamment les valeurs
       et symboles des pièces).
    """
    def __init__(self, couleur=None, coord=None):
        self.couleur=couleur
        self.coord=coord
        self.symbole=None
        
    def __str__(self):
        return self.symbole
    def coups_legaux(self,partie)->list[tuple[int,int]]:
        """Détermine tous les coups légaux qu'une pièce peut faire dans une partie.
           Le principe est de simuler les coups possibles, puis de trier parmi les coups menant 
           à un échec (donc non légaux)
        Args:
            partie (EtatJeu): La partie

        Returns:
           list[tuple[int,int]] : Les coups
        """
        coups = []
        for coord_f in self.coups_possibles(partie):
            #sauvegarde de l'ancien plateau
            piece_potentiellement_mangée = partie.plateau.get(coord_f,None)
            coord_i = self.coord
            #déplacement de la pièce
            self.coord=coord_f
            partie.plateau[coord_f] = partie.plateau.pop(coord_i)
            #On retire la pièce à l'adversaire
            if piece_potentiellement_mangée is not None:
                partie.pieces[not self.couleur].remove(piece_potentiellement_mangée)
            
            #On vérifie si il y a échec
            if not partie.echec():
                coups.append(coord_f)
            #retrait du coups
            self.coord=coord_i
            partie.plateau[coord_i] = partie.plateau.pop(coord_f)
            #On replace la pièce mangée
            if piece_potentiellement_mangée is not None:
                partie.plateau[coord_f] = piece_potentiellement_mangée
                partie.pieces[not self.couleur].append(piece_potentiellement_mangée)
        return coups
    

    
class Roi(Piece): 
    """Roi du jeu d'échecs. Hérite de Piece"""
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Roi"
        
        if self.couleur:
            self.symbole="♚"
            self.valeur=0
        else:
            self.symbole="♔"
            self.valeur=0
        self.odometre=0    
        
    def coups_possibles(self, partie)->list:
        """Renvoie tout les coups possibles (sans trier les coups mettant en échec) de la pièce.

        Args:
            partie (EtatJeu): La partie.

        Returns:
            list: Liste des coups
        """
        coups=[]
        x,y=self.coord
        
        for direction in [(1,1),(1,-1),(-1,-1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            if 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        coups.append((x,y))
        return coups
class Dame(Piece):
    """Dame du jeu d'échecs. Hérite de Piece"""
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Dame"
        
        if self.couleur:
            self.symbole="♛"
            self.valeur=9
        else:
            self.symbole="♕"
            self.valeur=-9
            
    def coups_possibles(self, partie):
        coups=[]
        x,y=self.coord
        
        for direction in [(1,1),(1,-1),(-1,-1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
        return coups

class Fou(Piece):
    """Fou du jeu d'échecs. Hérite de Piece"""
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom=("Fou")
        
        if self.couleur:
            self.symbole="♝"
            self.valeur=3   
        else:
            self.symbole="♗"
            self.valeur=-3
            
    def coups_possibles(self, partie):
        coups=[]
        
        for direction in [(1,1),(1,-1),(-1,-1),(-1,1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
    
        
        return coups
    


class Cavalier(Piece):
    """Cavlier du jeu d'échecs. Hérite de Piece"""
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Cavalier"
        
        if self.couleur:
            self.symbole="♞"
            self.valeur=3
        else:
            self.symbole="♘"
            self.valeur=-3
            
    def coups_possibles(self, partie):
        coups=[]
        x,y=self.coord 
        
        for direction in [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]:
            
            if 0<=x+direction[0]<=7 and 0<=y+direction[1]<=7:
                piece=partie.plateau.get((x+direction[0],y+direction[1]),None)
                if piece==None or piece.couleur!=self.couleur:
                    coups.append((x+direction[0],y+direction[1]))
        return coups



class Tour(Piece):
    """Tour du jeu d'échecs. Hérite de Piece"""
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Tour"
        
        if self.couleur:
            self.symbole="♜"
            self.valeur=5
        else:
            self.symbole="♖"
            self.valeur=-5
            
    def coups_possibles(self, partie):
        coups=[]
        x,y=self.coord
        
        for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
        return coups
    

class Pion(Piece):
    """Pion du jeu d'échecs. Hérite de Piece"""
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Pion"
        self.premier_coup=True
        
        if self.couleur:
            self.symbole="♟"
            self.valeur=1
        else:
            self.symbole="♙"
            self.valeur=-1
            
    def coups_possibles(self, partie):
        coups=[]
        x,y=self.coord

        if self.couleur:
            if y+1<=7:
                if partie.plateau.get((x,y+1),None)==None:
                    coups.append((x,y+1))
                    if self.coord[1]==1 and partie.plateau.get((x,y+2),None)==None and y+2<=7:
                        coups.append((x,y+2))
                for dx in [-1, 1]:
                    if 0<=x+dx<=7:
                        piece=partie.plateau.get((x+dx,y+1),None)
                        if piece != None and piece.couleur != self.couleur:
                            coups.append((x+dx, y+1))
        else:
            if y-1>=0:
                if partie.plateau.get((x,y-1),None)==None:
                    coups.append((x,y-1))
                    if self.coord[1]==6 and partie.plateau.get((x,y-2),None)==None and y-2>=0:
                        coups.append((x,y-2))
                for dx in [-1, 1]:
                    if 0<=x+dx<=7:
                        piece=partie.plateau.get((x+dx,y-1),None)
                        if piece != None and piece.couleur != self.couleur:
                            coups.append((x+dx, y-1))   
        return coups
    
    
    def promotion(self)->bool:
        """Détermine si le pion peut être promu, selon sa couleur.

        Returns:
            bool: True <=> Le pion peut être promu
        """
        if self.couleur and self.coord[1]==7:
            return True
        elif not self.couleur and self.coord[1]==0:
            return True
        return False