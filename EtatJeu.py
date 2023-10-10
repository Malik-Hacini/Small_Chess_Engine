from joueurs import*
from piece import*
import numpy as np
import copy

class EtatJeu:
    
    """Partie de jeu d'échecs
    """
    def __init__(self,j1 : Joueur, j2 : Joueur, sauvegarde : str = "Plateau_base"):
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs. Attribue aussi leur position aux pièces.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
            trait (bool) : prochaine couleur à jouer
        """
        print("Chargement de la partie")
        #création des joueurs
        self.joueurs=[j2,j1]
        
        
        #lecture du fichier de sauvegarde
        fichier = open(sauvegarde+".txt", 'r')
        sauv_txt = fichier.read()
        fichier.close()
        #maintenant il faut extraire le texte important : 
        pieces_j1,pieces_j2,trait_texte = sauv_txt.split("\n")
        pieces_j1 = pieces_j1[10:]
        pieces_j2 = pieces_j2[10:]
        trait_texte = trait_texte[8:]
        
        
        #dictionnaire de {coordonnées : objet piece}
        self.plateau = {}
        for pieces_j in (pieces_j1,pieces_j2):
            for p in pieces_j.split(";"):
                p = p[1:-1]
                p = p.split(",")
                type_piece = p[0]
                couleur_piece = True if p[1] == "True" else False
                coord_piece = (int(p[2]),int(p[3]))
                
                #pion tour cavalier fou roi reine 
                if type_piece == "Pion": piece = Pion(couleur_piece,coord_piece)
                if type_piece == "Tour": piece = Tour(couleur_piece,coord_piece)
                if type_piece == "Cavalier": piece = Cavalier(couleur_piece,coord_piece)
                if type_piece == "Fou": piece = Fou(couleur_piece,coord_piece)
                if type_piece == "Reine": piece = Reine(couleur_piece,coord_piece)
                if type_piece == "Roi": piece = Roi(couleur_piece,coord_piece)
                #on ajoute la piece au plateau
                self.plateau[coord_piece] = piece
                
                #on ajoute la piece au bon joueur

                if pieces_j == pieces_j1:
                    self.joueurs[1].pieces.append(piece)
                elif pieces_j == pieces_j2:
                    self.joueurs[0].pieces.append(piece)
                    
        if trait_texte == "blancs": self.trait = True
        else : self.trait = False
        self.valeur = 0
            
                
    def __str__(self)->str:
        """Méthode print pour la partie. Affiche le plateau dans
        son état actuel.Nous n'utilisons pas la métohde spéciale __str__, car En fonction du tour, l'affichage
        du plateau est renversé.
        
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
        
    
    
    def sauvegarder(self,nom_fichier : str = None) -> None:
        #ouvrir un fichier de sauvegarde en ecriture
        #écrire la sauvegarde sous format [(type de piece, couleur, coordonnées)]
        #fermer le fichier
        sauvegarde = f"{self.joueurs[1].nom} : "
        for piece in self.joueurs[1].pieces:
            sauvegarde+=f"[{piece.nom},{piece.couleur},{piece.coord[0]},{piece.coord[1]}];"    
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au dernier
        
        #sauvegarder le deuxieme joueur
        
        sauvegarde+=f"\n{self.joueurs[0].nom} : "
        for piece in self.joueurs[0].pieces:
            sauvegarde+=f"[{piece.nom},{piece.couleur},{piece.coord[0]},{piece.coord[1]}];"
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au  dernier 
        
        sauvegarde+="\nTrait : "
        if self.trait :sauvegarde+="blancs"
        else : sauvegarde+="noirs"
        
        
        #demander le fichier a sauvegarder s'il n'est pas spécifier par le programme (sauvegarde de base du jeu)
        if sauvegarde is None:
            nom_fichier = input("nom du fichier de sauvegarde : ")
            
        #écriture dans le fichier spécifier (écrase le texte déja existant ou crée un nouveau fichier)
        fichier = open(nom_fichier+".txt", 'w')
        fichier.write(sauvegarde)
        fichier.close()
        
        
        
        
    
    
    
    def deplacer_piece(self, coord1: tuple[int,int], coord2: tuple[int, int])->np.ndarray:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord1 (tuple[int,int]): Position de la pièce à déplacer
            coord2 (tuple[int,int]): Position finale de la pièce
        Returns:
            dict: Le plateau modifié
            """
        
                
    def echec(self) -> bool:
        """Fonction qui nous dis si le roi de la couleur demandé est en échec

        Args:
            couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

        Returns:
            bool: True <=> Roi en échec
        """
        #il faut trouver qui est le joueur à qui c'est le tour
        
        for piece in self.joueurs[self.trait].pieces : 
            if piece.nom == "Roi":case_roi = piece.coord#on récupere la case occupée par le roi
            else : pieces_adversaire = self.joueurs[not (self.trait)].pieces#on récupere les pieces de l'adversaire
            
        for piece in pieces_adversaire: #Pour les pièces de l'adversaire en jeu
            for case in piece.coups_possibles(self):# Pour chaque case controllé par l'adversaire
                if case == case_roi :#On vérifie si cette case est celle du roi
                    print(piece.nom,piece.couleur)
                    return True
        return False
        


   
    def echec_et_mat(self):
        #regarder si le roi est en echec, regarder s'il peut bouger, regarder s'il y a d'autre coups parmis les pieces
        if not self.echec() : return False #si le roi n'est pas en echec il n'y a pas mat
        #on regarde s'il existe des pièces qui ont le droit de bouger
        
  
        pieces_joueur = self.joueurs[self.trait].pieces
        for piece in pieces_joueur:
                print(piece, piece.coups_legaux(self),piece.coord)
                if len(piece.coups_legaux(self))>0 :return False
        return True
                
        
        """ 
        for j in (self.j1,self.j2):
            if j.couleur == self.trait:
                #récupérer les pieces du joueur
                pieces_joueur = j.pieces
                #récupérer la case du roi
                for piece in j.pieces : 
                    if piece.nom == "Roi":case_roi = piece.coord; #on récupere la case occupée par le roi
            else : pieces_adversaire = j.pieces#on récupere les pieces de l'adversaire
            
            
            
        for piece in pieces_joueur: #Pour les pièces de l'adversaire en jeu
            for case in piece.coups_possible(self):# Pour chaque coup possible de la piece sélectionnée
                #simuler un coup et vérifier si le roi est toujours en échec
                #comment faire une simulation?, on peut créer un nouveau plateau et vérifier s'il est en echec, ou on peut modifier le plateau de jeu actuel et inverser les coups après
                #je pense qu'il vaut mieux créer un nouveau plateau car ca sera nécessaire dans l'étape de l'IA
                plateau_sim = copy.deepcopy(self.plateau)
                #on va jouer le coups suggéré sur la simulation
                #créer une nouvelle partie avec un nouveau plateau
                bot1,bot2 = Joueur("Bot1",self.j1.couleur,copy.deepcopy(self.j1.pieces)),Joueur("Bot2",self.j1.couleur,copy.deepcopy(self.j2.pieces))
                simu = Partie(bot1,bot2,plateau_sim,self.trait)
                
                for bot in (bot1,bot2):
                    if bot.couleur == simu.trait:
                        joueur = bot
                for piece in bot.pieces :
                    for coup in piece.coup_possible():
                        #déplacer la piece
                        piece.coord=coup
                        simu.plateau[coup] = simu.plateau.pop(piece.coord)
                        #regarder s'il est en echec
                        if simu.
                """
                     
                    
                
                
                #vérifier si le roi est toujours en échec
                #il va falloir changer la structure pour l'adapter au cours d'IA
    def gagnant(self):
        
        if self.echec_et_mat(): 
            return self.joueurs[self.trait]
        
        
    def calcul_valeur(self)->float:
        """Fonction qui calcule la valeur du plateau. La valeur est positive si les blancs ont l'avantage et négative si 
        les noirs ont l'avantage 

        Returns:
            float: valeur du jeu
        """
        valeur=0
        for pieces in [self.pieces_j1, self.pieces_j2]:
            cases_controllees=set()
            for piece in pieces:
                
                valeur+=piece.valeur
                cases_controllees.add(set(piece.coups_legaux))            
            
                for centre in [(3,3),(3,4),(4,4),(4,3)]:
                    if piece==self.plateau.get(centre,None):
                        valeur+=(0.75*piece.valeur)
                
                for sous_centre in [(2,2),(2,3),(2,4),(2,5),(3,5),(4,5),(5,5),(6,5),(6,4),(6,3),(6,2),(5,2),(3,2)]:
                    if piece==self.plateau.get(sous_centre, None):
                        valeur+=(0,33*piece.valeur)
                    
            if pieces==self.pieces_j1:
                valeur+=len(cases_controllees)
            else:
                valeur-=len(cases_controllees)
        
        self.valeur=valeur