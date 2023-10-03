from Partie import*
<<<<<<< HEAD

=======
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
class Piece:


    def __init__(self, couleur=None, coord=None):
        self.couleur=couleur
        self.coord=coord
        self.coups=[]
        self.symbole=None
        
    def __str__(self):
        return self.symbole
<<<<<<< HEAD
    
    def deplacer_piece(x,y):
        self.coord=(x,y)

=======

    
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
class Roi(Piece): 
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Roi"
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♔"
        else:
            self.symbole="♚"
        
=======
            self.symbole="♚"
        else:
            self.symbole="♔"
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
class Reine(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Reine"
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♕"
        else:
            self.symbole="♛"
=======
            self.symbole="♛"
        else:
            self.symbole="♕"
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord
<<<<<<< HEAD
        for i in range(x+1, 8):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((i,y))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((i,y))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(x-1, -1, -1):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((i,y))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((i,y))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(y+1, 8):
            piece=partie.plateau.get((x, i),None)
            if piece==None:
                self.coups.append((x,i))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((x,i))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(y-1, -1, -1):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((x,i))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((x,i))
                    break
                elif piece.couleur==self.couleur:
                    break
        x,y=self.coord   
        x+=1
        y+=1
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
            x+=1
            y+=1
        x,y=self.coord   
        x+=1
        y-=1
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
            x+=1
            y-=1
        x,y=self.coord   
        x-=1
        y-=1
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
            x-=1
            y-=1
        x,y=self.coord
        x-=1
        y+=1
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
            x-=1
            y+=1
=======
        
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
        """
        x,y=self.coord
        
        for coord in (x,y):
            for vect in [(1,8,1),(-1,-1,-1)]:
                for i in range(coord+vect[0],vect[1],vect[2]):
                    
                    piece=partie.plateau.get((i, y),None)
                    if piece==None:
                        self.coups.append((i,y))
                    else:
                        if piece.couleur!=self.couleur:
                            self.coups.append((i,y))
                            break
                        elif piece.couleur==self.couleur:
                            break"""
        
                
                
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        return self.coups

class Fou(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom=("Fou")
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♗"
        else:
            self.symbole="♝"        
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord   
        x+=1
        y+=1
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
            x+=1
            y+=1
        x,y=self.coord   
        x+=1
        y-=1
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
            x+=1
            y-=1
        x,y=self.coord   
        x-=1
        y-=1
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
            x-=1
            y-=1
        x,y=self.coord
        x-=1
        y+=1
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
            x-=1
            y+=1
        return self.coups
=======
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
    

>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147

class Cavalier(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Cavalier"
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♘"
        else:
            self.symbole="♞"
=======
            self.symbole="♞"
        else:
            self.symbole="♘"
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord 
<<<<<<< HEAD
        if 0<=x+1<=7 and 0<=y+2<=7:
            piece=partie.plateau.get((x+1,y+2),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x+1,y+2))
        if 0<=x-1<=7 and 0<=y+2<=7:
            piece=partie.plateau.get((x-1,y+2),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x-1,y+2))
        if 0<=x-2<=7 and 0<=y+1<=7:
            piece=partie.plateau.get((x-2,y+1),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x-2,y+1))
        if 0<=x-2<=7 and 0<=y-1<=7:
            piece=partie.plateau.get((x-2,y-1),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x-2,y-1))
        if 0<=x-1<=7 and 0<=y-2<=7:
            piece=partie.plateau.get((x-1,y-2),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x-1,y-2))
        if 0<=x+1<=7 and 0<=y-2<=7:
            piece=partie.plateau.get((x+1,y-2),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x+1,y-2))
        if 0<=x+2<=7 and 0<=y-1<=7:
            piece=partie.plateau.get((x+2,y-1),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x+2,y-1))
        if 0<=x+2<=7 and 0<=y+1<=7:
            piece=partie.plateau.get((x+2,y+1),None)
            if piece==None or piece.couleur!=self.couleur:
                self.coups.append((x+2,y+1))
=======
        
        for direction in [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1)]:
            
            if 0<=x+direction[0]<=7 and 0<=y+direction[1]<=7:
                piece=partie.plateau.get((x+direction[0],y+direction[1]),None)
                if piece==None or piece.couleur!=self.couleur:
                    self.coups.append((x+direction[0],y+direction[1]))
        
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        
        return self.coups



class Tour(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Tour"
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♖"
        else:
            self.symbole="♜"
=======
            self.symbole="♜"
        else:
            self.symbole="♖"
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
            
    def coups_possibles(self, partie):
        self.coups=[]
        x,y=self.coord
<<<<<<< HEAD
        for i in range(x+1, 8):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((i,y))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((i,y))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(x-1, -1, -1):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((i,y))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((i,y))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(y+1, 8):
            piece=partie.plateau.get((x, i),None)
            if piece==None:
                self.coups.append((x,i))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((x,i))
                    break
                elif piece.couleur==self.couleur:
                    break
        for i in range(y-1, -1, -1):
            piece=partie.plateau.get((i, y),None)
            if piece==None:
                self.coups.append((x,i))
            else:
                if piece.couleur!=self.couleur:
                    self.coups.append((x,i))
                    break
                elif piece.couleur==self.couleur:
                    break
=======
        
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
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
        return self.coups
    

class Pion(Piece):
    
    def __init__(self, couleur, coord=None):
        super().__init__(couleur, coord) 
        self.nom="Pion"
        self.premier_coup=True
        
        if self.couleur:
<<<<<<< HEAD
            self.symbole="♙"
        else:
            self.symbole="♟"
=======
            self.symbole="♟"
        else:
            self.symbole="♙"
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
            
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
<<<<<<< HEAD
        return self.coups
=======
        return self.coups
>>>>>>> 06aa0641d03c54f8308ba535ab171ed14e815147
