from joueurs import*
from piece import*
import numpy as np


class EtatJeu:
    
    """Partie de jeu d'échecs
    """
    def __init__(self, sauvegarde : str = "Plateau_base.fen"):
        """Construit une partie d'échecs.
        Construit le plateau et les pièces grâce au fichier de sauvegarde FEN donné (Le plateau de base du jeu d'échecs sinon)


        Args:
            sauvegarde (str, optional): Le nom du plateau de sauvegarde. Défault : "Plateau_base".
        """
        
        print("Chargement de la partie")
        #Création des pieces
        self.pieces=[[],[]]
        self.plateau = dict()
        
        
        #Lecture du fichier de sauvegarde
        fichier = open("sauvegardes\\"+sauvegarde, 'r')
        sauv_txt = fichier.read()
        fichier.close()
        #On extrait le texte qui compte du FEN (nous ne prenons pas en compte le roque, en passant etc)
        lignes, trait, roque, en_passant, demi_coup, coup_complet  = sauv_txt.split(" ")
        
        y=7
        for ligne in lignes.split("/"):
            x=0
            for element in ligne:
                if element in "123456789":
                    x+=int(element)
                else : 
                    if element.lower() == "k": piece = Roi(element.isupper(),(x,y))
                    if element.lower() == "q": piece = Dame(element.isupper(),(x,y))
                    if element.lower() == "b": piece = Fou(element.isupper(),(x,y))
                    if element.lower() == "n": piece = Cavalier(element.isupper(),(x,y))
                    if element.lower() == "r": piece = Tour(element.isupper(),(x,y))
                    if element.lower() == "p": piece = Pion(element.isupper(),(x,y))
                    #on ajoute la piece au plateau
                    self.plateau[(x,y)] = piece
                    
                    if element.isupper():
                        self.pieces[1].append(piece)
                    else:
                        self.pieces[0].append(piece)
                    x+=1
            y-=1
        self.trait = (trait == "w")
        
                
    def __str__(self)->str:
        """Méthode print pour la partie. Affiche le plateau dans
        son état actuel.
        Args:
            tour (bool) :  True <=> Tour aux blancs 
        Returns:
            str: Le plateau.
        """
        if self.trait:
            ordre_affichage=range(7,-1,-1)
        else:
            ordre_affichage=range(8)
        
        p=""

        num_ligne=[str(x) for x in range(1,9)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        
        p+=" "*5 +  "    ".join(nom_col) +"\n"
        
        for i in ordre_affichage:
           
           p+=num_ligne[i] + "  | "
               
           for j in range(8):
               symbole=self.plateau.get((j,i)," ").__str__()
               p+= symbole + "  | "
                

           p+=  "\n" + "   "+ "-"*41 + "\n"
           
        p+=" "*5 +  "    ".join(nom_col)
        
        return p
        
    
    
    def fen_position(self)->str:
        """Traduit une partie en notation FEN, afin de sauvegarder.

        Returns:
            str: FEN de la partie
        """
        pion=["p","P"]
        cavalier=["n","N"]
        fou=["b","B"]
        tour=["r","R"]
        dame=["q","Q"]
        roi=["k","K"]
        
        fen=""
        for ligne in range(7,-1,-1):
            vides=0
            for col in range(8):
                piece=self.plateau.get((col,ligne),None)

                if piece==None:
                    vides+=1
                else :
                    if vides !=0:
                        fen+=str(vides)
                        vides = 0
                    if isinstance(piece,Pion): fen+=f"{pion[piece.couleur]}" 
                    if isinstance(piece,Cavalier): fen+=f"{cavalier[piece.couleur]}" 
                    if isinstance(piece,Fou): fen+=f"{fou[piece.couleur]}" 
                    if isinstance(piece,Tour): fen+=f"{tour[piece.couleur]}" 
                    if isinstance(piece,Dame): fen+=f"{dame[piece.couleur]}" 
                    if isinstance(piece,Roi): fen+=f"{roi[piece.couleur]}" 
            if vides !=0:
                fen+=str(vides)
            fen+="/"
        trait=["b","w"]
        
        fen+=f" {trait[self.trait]} - - 0 0"
        return fen
        
    def sauvegarder(self,nom_fichier : str ):
        """Sauvegarde la partie dans le fichier indiqué

        Args:
            nom_fichier (str): le nom du fichier.
        """
        
        fichier = open("sauvegardes\\"+nom_fichier+".fen", 'w')
        fichier.write(self.fen_position())
        fichier.close()    
    
    def deplacer_piece(self, coord_i: tuple, coord_f: tuple)->np.ndarray:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord_i (tuple[int,int]): Position de la pièce à déplacer
            coord_f (tuple[int,int]): Position finale de la pièce
        Returns:
            np.ndarray: Le plateau modifié
            """
            
        #il faut aussi supprimer la piece de la liste des pieces pour le calcul de la valeur blyat
        #s'il y a une piece sur la case d'arrivée
        if coord_f in self.plateau.keys() :
            #retirer la piece du set de l'adversaire
            self.pieces[not self.trait].remove(self.plateau[coord_f])
        
        
        if isinstance(self.plateau[coord_i],Roi):
            self.plateau[coord_i].odometre+=1
        else:
            for piece in self.pieces[self.trait]:
                if isinstance(piece,Roi):
                    piece.odometre=0
        
        #changer les coordonnées dans la classe piece
        self.plateau[coord_i].coord=coord_f
        #on déplace la piece sur le plateau
        self.plateau[coord_f] = self.plateau.pop(coord_i)
        
        self.trait = not self.trait #On change le tour
    
    
    def mouvements(self,couleur:bool) -> dict[tuple[int,int],list[tuple[int,int]]]:
        """Retourne tout les coups possibles pour une certaine couleur dans l'état actuel,
        sous forme de dictionnaire.

        Args:
            couleur (bool): True <=> Blanc

        Returns:
            dict[tuple[int,int],list[tuple[int,int]]]: Dictionnaire des coups possibles, pour chaque pièce.
        """
        mouv = dict()
        for piece in self.pieces[couleur]:
            mouv[piece.coord] = piece.coups_legaux(self)
        return mouv
    


    def calcul_valeur(self)->float:
        """Fonction d'évaluation de l'état du jeu. Est basée sur JAI PAS TROUVE LE WIKI

        Returns:
            float: valeur du jeu
        """
        valeur=0
        if self.echec_et_mat():
            if self.gagnant():
                return 1000
            else:
                return -1000

        if self.nulle():
            return 0
                
        
        for pieces in [self.pieces[1], self.pieces[0]]:
            cases_controllees=set()
            pions=[]
            
            for piece in pieces:
                valeur+=piece.valeur
                
                for centre in [(3,3),(3,4),(4,4),(4,3)]:
                    if piece==self.plateau.get(centre,None):
                        valeur+=(0.5)*((-1)**(not piece.couleur))
                
                for sous_centre in [(2,2),(2,3),(2,4),(2,5),(3,5),(4,5),(5,5),(6,5),(6,4),(6,3),(6,2),(5,2),(3,2)]:
                    if piece==self.plateau.get(sous_centre, None):
                        valeur+=(0.1)*((-1)**(not piece.couleur))

    
                if isinstance(piece,Pion):
                    pions.append(piece)
                
                cases_controllees |= set(piece.coups_possibles(self))
                 
            valeur+=0.05*len(cases_controllees)*((-1)**(not piece.couleur))
            
            
            collones=[]
            for pion in pions:
                if pion.coord[0] not in collones:
                    collones.append(pion.coord[0])
                else:
                    valeur+=0.1*((-1)**piece.couleur)
        return round(valeur,3)
        
                
                
    
                
    def echec(self) -> bool:
        """Détermine si le roi du joueur à qui c'est le tour (trait de la partie) est en échec.
        
        Returns:
            bool: True <=> Roi en échec
        """
        #il faut trouver qui est le joueur à qui c'est le tour
        case_roi = None
        for piece in self.pieces[self.trait]:
            if isinstance(piece,Roi):
                case_roi = piece.coord#on récupere la case occupée par le roi
        pieces_adversaire = self.pieces[not (self.trait)]#on récupere les pieces de l'adversaire
        for piece in pieces_adversaire: #Pour les pièces de l'adversaire en jeu
            for case in piece.coups_possibles(self):# Pour chaque case controllé par l'adversaire
                if case == case_roi :#On vérifie si cette case est celle du roi
                    return True
        return False
        


   
    def echec_et_mat(self)->bool:
        """Détermine si le joueur à qui c'est le tour est en échec et mat.

        Returns:
            bool
        """
        if not self.echec() : return False #si le roi n'est pas en echec il n'y a pas mat
        #on regarde s'il existe des pièces qui ont le droit de bouger
        
  
        pieces_joueur = self.pieces[self.trait]
        for piece in pieces_joueur:
                if len(piece.coups_legaux(self))>0 :return False
        return True
    
    
    def gagnant(self)->bool:
        """Donne le gagnant de la partie, si il y en a un."""
    
        if self.echec_et_mat(): 
            return not self.trait #attention ici on ne renvoie que la couleur du trait, au main de décider quel joueur c'est
        return None
    
    def nulle(self)->bool:
        """Détermine si la partie est nulle selon les deux cas particuliers que nous avons défini : le pat et l'odomètre.
        Returns:
            bool: True <=> La partie est nulle
        """
        odometre=0
        coups=[]
        pieces_joueur = self.pieces[self.trait]
        for piece in pieces_joueur:
            coups+=piece.coups_legaux(self)
            if isinstance(piece,Roi):
                odometre=piece.odometre
        return (not self.echec_et_mat()and len(coups)==0) or (odometre>=10)