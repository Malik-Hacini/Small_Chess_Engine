from Partie import*
class Piece:


    def __init__(self, couleur=None, coord=None):
        self.couleur=couleur
        self.coord=coord
        self.coups=[]
        self.symbole=None
        
    def __str__(self):
        return self.symbole
    
    def coups_legaux(self, partie):
        """Fonction qui donene les coups légaux d'une pièce (cad possible et sans echec)

        Args:
            partie (_type_): _description_

        Returns:
            list: La liste des coordonnées ou la pièces peuts se déplacer 
        """
        self.coups=self.coups_possibles(partie)
        x_i, y_i= self.coord
        for coup in coups:
            pass
        
        return self.coups

        

    
class Roi(Piece): 
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Roi"
        
        if self.couleur:
            self.symbole="♚"
        else:
            self.symbole="♔"
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord
        for direction in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
            if 0<=x+direction[0]<=7 and 0<=y+direction[1]<=7:
                piece=partie.plateau.get((x+direction[0], y+direction[1]), None)
                if piece==None or piece.couleur!=self.couleur:
                    self.coups.append((x+direction[0], y+direction[1]))
        return self.coups
            
class Reine(Piece):
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Reine"
        
        if self.couleur:
            self.symbole="♛"
        else:
            self.symbole="♕"
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord
        
        for direction in [(1,1),(1,-1),(-1,-1),(-1,1),(1,0),(0,1),(-1,0),(0,-1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    self.coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        self.coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
        return self.coups

class Fou(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom=("Fou")
        
        if self.couleur:
            self.symbole="♝"        
        else:
            self.symbole="♗"
            
    def coups_possibles(self, partie):
        self.coups=[]
        
        for direction in [(1,1),(1,-1),(-1,-1),(-1,1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    self.coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        self.coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
        return self.coups
    


class Cavalier(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Cavalier"
        
        if self.couleur:
            self.symbole="♞"
        else:
            self.symbole="♘"
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord 
        
        for direction in [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]:
            
            if 0<=x+direction[0]<=7 and 0<=y+direction[1]<=7:
                piece=partie.plateau.get((x+direction[0],y+direction[1]),None)
                if piece==None or piece.couleur!=self.couleur:
                    self.coups.append((x+direction[0],y+direction[1]))
        return self.coups

class Tour(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Tour"
        
        if self.couleur:
            self.symbole="♜"
        else:
            self.symbole="♖"
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord
        
        for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
            x,y=self.coord   
            x+=direction[0]
            y+=direction[1]
            while 0<=x<=7  and 0<=y<=7:
                piece=partie.plateau.get((x,y),None)
                if piece==None:
                    self.coups.append((x,y))
                else:
                    if piece.couleur != self.couleur:
                        self.coups.append((x,y))
                        break
                    elif piece.couleur==self.couleur:
                        break
                x+=direction[0]
                y+=direction[1]
        return self.coups
    

class Pion(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Pion"
        self.premier_coup=True
        
        if self.couleur:
            self.symbole="♟"
        else:
            self.symbole="♙"
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord

        if self.couleur:
            if y+1<=7:
                if partie.plateau.get((x,y+1),None)==None:
                    self.coups.append((x,y+1))
                    if self.premier_coup and partie.plateau.get((x,y+2),None)==None and y+2<=7:
                        self.coups.append((x,y+2))
                for dx in [-1, 1]:
                    if 0<=x+dx<=7:
                        piece=partie.plateau.get((x+dx,y+1),None)
                        if piece != None and piece.couleur != self.couleur:
                            self.coups.append((x+dx, y+1))
        else:
            if y-1>=0:
                if partie.plateau.get((x,y-1),None)==None:
                    self.coups.append((x,y-1))
                    if self.premier_coup and partie.plateau.get((x,y-2),None)==None and y-2>=0:
                        self.coups.append((x,y-2))
                for dx in [-1, 1]:
                    if 0<=x+dx<=7:
                        piece=partie.plateau.get((x+dx,y-1),None)
                        if piece != None and piece.couleur != self.couleur:
                            self.coups.append((x+dx, y-1))        
        return self.coups
