from joueurs import*
from piece import*
import numpy as np

class EtatJeu:
    
    """Partie de jeu d'échecs
    """
    def __init__(self,j1 : Joueur, j2 : Joueur, plateau = "Plateau_base"):
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs. Attribue aussi leur position aux pièces.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
        """
        print("Chargement de la partie")
        #création des joueurs
        self.j1=j1
        self.j2=j2
       
        #lecture du fichier de sauvegarde
        fichier = open(plateau+".txt", 'r')
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
                    self.j1.pieces.append(piece)
                elif pieces_j == pieces_j2:
                    self.j2.pieces.append(piece)
                    
        if trait_texte == "blancs": self.trait = True
        else : self.trait = False
        self.valeur = 0
                
    def __str__(self)->str:
        """Méthode print pour lpartie. Affiche le plateau dans
        son état actuel.Nous n'utilisons pas la métohde spéciale __str__, car En fonction du tour, l'affichage
        du plateau est renversé.
        
        Args:
            tour (bool) :  True <=> Tour aux blancs 
        Returns:
            str: Le plateau.
        """
        print(self.trait)
        if self.trait:
            ordre_affichage=range(7,-1,-1)
        else:
            ordre_affichage=range(8)
        
        p=""
        i=0
        num_ligne=[str(x) for x in range(1,9)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        
        p+=" "*5 +  "    ".join(nom_col) +"\n"
        
        for i in ordre_affichage:
           
           p+=num_ligne[i] + "   "
               
           for j in range(8):
                try:
                    p+=self.plateau[(j,i)].__str__() + "  | "
                except KeyError:
                    p+= " " + "  | "
                
           i+=1
           p+=  "\n" + "   "+ "-"*41 + "\n"
           
        p+=" "*5 +  "    ".join(nom_col)
        
        return p
        
    
    
    def sauvegarder(self,nom_fichier : str = None) -> None:
        #ouvrir un fichier de sauvegarde en ecriture
        #écrire la sauvegarde sous format [(type de piece, couleur, coordonnées)]
        #fermer le fichier
        sauvegarde = "Joueur1 : "
        for i in self.j1.pieces:
            sauvegarde+=f"[{i.nom},{i.couleur},{i.coord[0]},{i.coord[1]}];"    
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au dernier
        
        #sauvegarder le deuxieme joueur
        
        sauvegarde+="\nJoueur2 : "
        for i in self.j1.pieces:
            sauvegarde+=f"[{i.nom},{i.couleur},{i.coord[0]},{i.coord[1]}];"
        sauvegarde = sauvegarde[:-1]#enlever le point virgule au  dernier 
        
        sauvegarde+="\Trait : "
        if self.trait == True:sauvegarde+="blancs"
        else : sauvegarde+="noirs"
        
        
        #demander le fichier a sauvegarder s'il n'est pas spécifier par le programme (sauvegarde de base du jeu)
        if sauvegarde is None:
            nom_fichier = input("nom du fichier de sauvegarde : ")
            
        #écriture dans le fichier spécifier (écrase le texte déja existant ou crée un nouveau fichier)
        fichier = open(nom_fichier+".txt", 'w')
        fichier.write(sauvegarde)
        fichier.close()
    
        
        

                
    def echec(self,couleur: bool ) -> bool:
        """Fonction qui nous dis si le roi de la couleur demandé est en échec

        Args:
            couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

        Returns:
            bool: True <=> Roi en échec
        """
        #il faut trouver qui est le joueur blanc?
        for j in (self.j1,self.j2):
            if j.couleur == couleur: 
                #récupérer la case du roi
                for piece in j.pieces : 
                    if piece.nom == "Roi":case_roi = piece.coord#on récupere la case occupée par le roi
            else : pieces_adversaire = j.pieces#on récupere les pieces de l'adversaire
            
        for piece in pieces_adversaire: #Pour les pièces de l'adversaire en jeu
            for case in piece.cases_controllees(self):# Pour chaque case controllé par l'adversaire
                if case == case_roi :#On vérifie si cette case est celle du roi
                    return True
        return False
        


   
    def echec_et_mat(self,couleur):
        #regarder si le roi est en echec, regarder s'il peut bouger, regarder s'il y a d'autre coups parmis les pieces
        if not self.echec(couleur) : return False #si le roi n'est pas en echec il n'y a pas mat
        for j in (self.j1,self.j2):
            if j.couleur == couleur: 
                #récupérer les pieces du joueur
                pieces_joueur = j.pieces
                #récupérer la case du roi
                for piece in j.pieces : 
                    if piece.nom == "Roi":case_roi = piece.coord; #on récupere la case occupée par le roi
            else : pieces_adversaire = j.pieces#on récupere les pieces de l'adversaire
            
        for piece in pieces_joueur: #Pour les pièces de l'adversaire en jeu
            for case in piece.cases_controllees(self):# Pour chaque coup possible de la piece sélectionnée
                #simuler un coup et vérifier si le roi est toujours en échec
                #comment faire une simulation?, on peut créer un nouveau plateau et vérifier s'il est en echec, ou on peut modifier le plateau de jeu actuel et inverser les coups après
                #je pense qu'il vaut mieux créer un nouveau plateau car ca sera nécessaire dans l'étape de l'IA
                plateau_sim = self.plateau.copy()
                #on va jouer le coups suggéré sur la simulation 
                pass
                #vérifier si le roi est toujours en échec
                #il va falloir changer la structure pour l'adapter au cours d'IA
            return False

   
    def echec_et_mat(self,couleur):
        pass
    
    def gagnant(self):
        
        if self.echec_et_mat(True): return self.j1
        
        elif self.echec_et_mat(False): return self.j2
        
        return None  