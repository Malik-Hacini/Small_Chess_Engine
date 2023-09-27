'''
Fichier Contenant le comportement des différentes pièces du jeu
'''
from Partie import*

class Piece:

    def __init__(self, couleur=None, coord=None):
        '''
        param: 
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple(int, int) (obssice(1-8), ordonnée(1-8)) ou None si la pièce n'est pas sur le plateau
        '''
        self.couleur=couleur
        self.coord=coord
        self.liste_coups=[]
        self.premier_coup=True #Important de le savoir pour les pion le roi et les tours
    


    def tri_deplacement_echec(self, liste_cases_controllees: list, partie)->list:
        """Fonction qui simule une liste de déplacements et suprime les déplacements qui mène à des echecs

        Args:
            liste_deplacement (list): La liste de déplacement que l'on simule

        Returns:
            list: La liste des déplacements triée des situations qui mettent en échec
        """
        x_i, y_i = self.coord
        for deplacement in liste_cases_controllees:
            self.coord=deplacement
            print(self.coord)
            if partie.echec(self.couleur):
                liste_cases_controllees.remove(deplacement)
                
        self.coord=x_i,y_i
    
        return liste_cases_controllees
    
    def coups_possibles(self, partie):
        '''
        Fonction qui calcules les cases ou la piece peut aller. C'est à dire les cases qu'elle controle sans meetre le roi en echec
        Input: piece
        Output: liste des cases ou on peut aller
        '''
        liste_cases_controllees=self.cases_controllees(partie)
        self.liste_coups= self.tri_deplacement_echec(liste_cases_controllees, partie)
        
        return self.liste_coups



class Roi(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom="Roi"
        
        if self.couleur==True:
            self.symbole="♔"
        else:
            self.symbole="♚"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        liste_cases_controllees=[]
        x,y=self.coord
        if 1<=x+1<=8 and 1<=y+1<=8 and not partie.case_occupe(x+1,y+1, self.couleur):
            liste_cases_controllees.append((x+1,y+1))
        if 1<=x+1<=8 and 1<=y<=8 and not partie.case_occupe(x+1,y, self.couleur):
            liste_cases_controllees.append((x+1,y))
        if 1<=x+1<=8 and 1<=y-1<=8 and not partie.case_occupe(x+1,y-1, self.couleur):
            liste_cases_controllees.append((x+1,y-1))
        if 1<=x<=8 and 1<=y-1<=8 and not partie.case_occupe(x,y-1, self.couleur):
            liste_cases_controllees.append((x,y-1))
        if 1<=x-1<=8 and 1<=y-1<=8 and not partie.case_occupe(x-1,y-1, self.couleur):
            liste_cases_controllees.append((x-1,y-1))
        if 1<=x-1<=8 and 1<=y<=8 and not partie.case_occupe(x-1,y, self.couleur):
            liste_cases_controllees.append((x-1,y))
        if 1<=x-1<=8 and 1<=y+1<=8 and not partie.case_occupe(x-1,y+1, self.couleur):
            liste_cases_controllees.append((x-1,y+1))
        if 1<=x<=8 and 1<=y+1<=8 and not partie.case_occupe(x,y+1, self.couleur):
            liste_cases_controllees.append((x,y+1))
        
        return liste_cases_controllees
    
    def coups_possibles(self, partie):
        '''
        Fonction qui calcules les cases ou la piece peut aller. C'est à dire les cases qu'elle controle sans meetre le roi en echec
        Input: piece
        Output: liste des cases ou on peut aller
        '''
        liste_cases_controllees=self.cases_controllees(partie)
        self.liste_coups= self.tri_deplacement_echec(liste_cases_controllees, partie)
        print(self.liste_coups)
        return self.liste_coups


class Reine(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom="Reine"
        
        if self.couleur==True:
            self.symbole="♕"
        else:
            self.symbole="♛"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        '''
        Fonction qui rends la liste des cases controllées possible pour cette pièce
        Input: La piece
        Output: Listes des cases que la piece controlle possibles 
        '''
        liste_cases_controllees=[]

        #Déplacement de la tour
        #deplacement x croissant
        x,y = self.coord
        x+=1
        while x<=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1 #On continue 

        
        #deplacement x decroissant
        x,y = self.coord
        x-=1
        while x>=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                liste_cases_controllees.append((x,y))
                x-=1 #On continue

        
        #Déplacement y croissant
        x,y = self.coord
        y+=1
        while y<=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                y+=1 #On continue 

        
        #deplacement y decroissant
        x,y = self.coord
        y-=1
        while y>=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                liste_cases_controllees.append((x,y))
                y-=1 #On continue


        #déplacement du fou
        #deplacement diagonale droite haute x et y croissant
        x,y = self.coord
        x+=1
        y+=1
        while x<=8  and y <=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1
                y+=1 #On continue

        #deplacement diagonale droite basse x croissant et y décroissant
        x,y = self.coord
        x+=1
        y-=1
        while x<=8  and y >=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1
                y-=1 #On continue

        #deplacement diagonale gauche basse x décroissant et y décroissant
        x,y = self.coord
        x-=1
        y-=1
        while x<=8  and y >=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x-=1
                y-=1 #On continue

        #deplacement diagonale gauche haute x décroissant et y croissant
        x,y = self.coord
        x-=1
        y+=1
        while x<=8  and y <=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x-=1
                y+=1 #On continue
    
        return liste_cases_controllees


class Fou(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom=("Fou")
        
        if self.couleur==True:
            self.symbole="♗"
        else:
            self.symbole="♝"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        '''
        Fonction qui rends la liste des cases controllées possible pour cette pièce
        Input: La piece
        Output: Listes des cases que la piece controlle possibles 
        '''
        liste_cases_controllees=[]

        #deplacement diagonale droite haute x et y croissant
        x,y = self.coord
        x+=1
        y+=1
        while x<=8  and y <=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1
                y+=1 #On continue

        #deplacement diagonale droite basse x croissant et y décroissant
        x,y = self.coord
        x+=1
        y-=1
        while x<=8  and y >=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1
                y-=1 #On continue

        #deplacement diagonale gauche basse x décroissant et y décroissant
        x,y = self.coord
        x-=1
        y-=1
        while x<=8  and y >=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x-=1
                y-=1 #On continue

        #deplacement diagonale gauche haute x décroissant et y croissant
        x,y = self.coord
        x-=1
        y+=1
        while x<=8  and y <=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x-=1
                y+=1 #On continue
        
        print(liste_cases_controllees)
        return liste_cases_controllees


class Cavalier(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom="Cavalier"
        
        if self.couleur==True:
            self.symbole="♘"
        else:
            self.symbole="♞"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        '''
        Fonction qui rends la liste des cases controllées possible pour cette pièce
        Input: La piece
        Output: Listes des cases que la piece controlle possibles 
        '''
        liste_cases_controllees=[]

        x,y= self.coord
        

        if not partie.case_occupe(x+1,y+2, self.couleur) and 1<=x+1<=8 and 1<=y+2<=8:
            liste_cases_controllees.append((x+1,y+2))

        if not partie.case_occupe(x-1,y+2, self.couleur) and 1<=x-1<=8 and 1<=y+2<=8:
            liste_cases_controllees.append((x-1,y+2))

        if not partie.case_occupe(x-2,y+1, self.couleur) and 1<=x-2<=8 and 1<=y+1<=8:
            liste_cases_controllees.append((x-2,y+1))

        if not partie.case_occupe(x-2,y-1, self.couleur) and 1<=x-2<=8 and 1<=y-1<=8:
            liste_cases_controllees.append((x-2,y-1))

        if not partie.case_occupe(x-1,y-2, self.couleur) and 1<=x-1<=8 and 1<=y-2<=8:
            liste_cases_controllees.append((x-1,y-2))
        
        if not partie.case_occupe(x+1,y-2, self.couleur) and 1<=x+1<=8 and 1<=y-2<=8:
            liste_cases_controllees.append((x+1,y-2))

        if not partie.case_occupe(x+2,y-1, self.couleur) and 1<=x+2<=8 and 1<=y-1<=8:
            liste_cases_controllees.append((x+2,y-1))

        if not partie.case_occupe(x+2,y+1, self.couleur) and 1<=x+2<=8 and 1<=y+1<=8:
            liste_cases_controllees.append((x+2,y+1))
        
        return liste_cases_controllees
    
        

class Tour(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom="Tour"
        
        if self.couleur==True:
            self.symbole="♖"
        else:
            self.symbole="♜"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        '''
        Fonction qui rends la liste des cases controllées possible pour cette pièce
        Input: La piece
        Output: Listes des cases que la piece controlle possibles 
        '''
        liste_cases_controllees=[]
        
        #deplacement x croissant
        x,y = self.coord
        x+=1
        while x<=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                x+=1 #On continue 

        
        #deplacement x decroissant
        x,y = self.coord
        x-=1
        while x>=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                liste_cases_controllees.append((x,y))
                x-=1 #On continue

        
        #Déplacement y croissant
        x,y = self.coord
        y+=1
        while y<=8 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else:#Sinon
                liste_cases_controllees.append((x,y))
                y+=1 #On continue 

        
        #deplacement y decroissant
        x,y = self.coord
        y-=1
        while y>=1 and not partie.case_occupe(x,y, not self.couleur): #Tant que on est sur le plateau et que aucune de nos pièce nous bloque
            if partie.case_occupe(x,y, self.couleur): #Si une pièce adverse setrouve sur la cette case
                liste_cases_controllees.append((x,y)) #On la mange
                break #Et on s'arrete la 
            else: #Sinon
                liste_cases_controllees.append((x,y))
                y-=1 #On continue

        
        return liste_cases_controllees



class Pion(Piece):
    
    def __init__(self, couleur, coord=None):
        '''
        param:
            couleur: Bool (True<=>Blanc, False<=>Noir)
            coord: tuple (obssice(1-8), ordonnée(1-8))
        '''
        super().__init__(couleur, coord) 
        self.nom="Pion"
        
        if self.couleur==True:
            self.symbole="♙"
        else:
            self.symbole="♟"

    def __str__(self):
        return self.symbole

    def cases_controllees(self, partie):
        '''
        Fonction qui rends la liste des cases controllées possible pour cette pièce
        Input: La piece
        Output: Listes des cases que la piece controlle possibles 
        '''
        liste_cases_controllees=[]
        x,y=self.coord

        #Cas 1: Avancer d'une case
        if self.couleur: #Si blanc
            if y+1<=8: #Si la ligne du dessus est encore sur le plateau
                if not partie.case_occupe(x,y+1, self.couleur) and not partie.case_occupe(x,y+1, not self.couleur): #Si la case au dessus n'est pas occupe
                    liste_cases_controllees.append((x, y+1))  #On peut aller dans cette case

                elif x+1<=8: #Si la collone de droite est encore sur le plateau
                    if partie.case_occupe(x+1,y+1, self.couleur): #Si la case en diagonale droite est occupé par un pièce adverse
                        liste_cases_controllees.append((x+1, y+1))

                elif x-1<=8: #Si la collone de gauche est encore sur le plateau
                    if partie.case_occupe(x-1,y+1): #Si la case en diagonale gauche est occupé par une pièce adverse 
                        liste_cases_controllees.append((x-1, y+1))

        else: #Couleur noir
            if y-1<=8: #Si la ligne du dessous est encore sur le plateau
                if not partie.case_occupe(x,y-1, self.couleur) and not partie.case_occupe(x,y-1, not self.couleur): #Si la case en dessous n'est pas occupé
                   liste_cases_controllees.append((x, y-1))  #On peut aller dans cette case

                elif x+1<=8: #Si la collone de droite est encore sur le plateau
                    if partie.case_occupe(x+1,y-1, self.couleur): #Si la case en diagonale droite est occupé par un pièce adverse
                       liste_cases_controllees.append((x+1, y-1)) #On peut aller sur cette case

                elif x-1<=8: #Si la collone de gauche est encore sur le plateau
                    if partie.case_occupe(x-1,y-1, self.couleur): #Si la case en diagonale gauche est occupé par une pièce adverse 
                       liste_cases_controllees.append((x-1, y-1)) #On peut aller sur cette case


        #Cas 2: Avancer de 2 cases
        if self.premier_coup:
            if self.couleur: #Si blanc
                if not partie.case_occupe(x,y+1, self.couleur) and not partie.case_occupe(x,y+1, not self.couleur) and not partie.case_occupe(x,y+2, self.couleur) and not partie.case_occupe(x,y+2, not self.couleur):
                    liste_cases_controllees.append((x, y-2))

                else: #Si noir
                    if not partie.case_occupe(x,y-1, self.couleur) and not partie.case_occupe(x,y-1, not self.couleur) and not partie.case_occupe(x,y-2, self.couleur) and not partie.case_occupe(x,y-2, not self.couleur):
                        liste_cases_controllees.append((x, y-2))

        
        return(liste_cases_controllees)
