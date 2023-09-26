from joueurs import*
from pièce import*
import numpy as np

class Partie:
    
    """Partie de jeu d'échecs
    """
    def __init__(self,j1 :Joueur, j2:Joueur, plateau: str = None):
        """Construit une partie d'échecs.
        Commence par créer un plateau si il n'est pas fourni,
        puis attribue les pièces de ce plateau aux joueurs
        de la partie, selon leur couleurs. Attribue aussi leur position aux pièces.

        Args:
            plateau (_type_, optional): Plateau de jeu. None si non fourni (nouvelle partie)
            j1 (Joueur) : Premier joueur de la partie, instance de la classe Joueur
            j2 (Joueur) : Second joueur de la partie, instance de la classe Joueur
        """
        if plateau is None:
            plateau={}

            for i in range(8):
                plateau[f"(6,{i})"]=Pion(couleur=False,coord=(1,i))
                plateau[f"(1,{i})"]=Pion(couleur=True, coord=(6,i)) 

            for couleur in(True,False):
                
                
                if couleur: ligne = 0
                else: ligne = 7
                
                for col in [0,7]: 
                    plateau[f"({ligne},{col})"]=Tour(couleur,coord=(ligne,col))
                   
                for col in [1,6]:
                    plateau[f"({ligne},{col})"]=Cavalier(couleur,coord=(ligne,col))
                   
                for col in [2,5]:
                    plateau[f"({ligne},{col})"]=Fou(couleur,coord=(ligne,col))
                    
                plateau[f"({ligne},3)"]=Reine(couleur,coord=(ligne,3))
                plateau[f"({ligne},4)"]=Roi(couleur, coord=(ligne,4))     
            
            
            
            
            self.plateau=plateau
            j1.pieces=[value for key,value in plateau.items() if value.couleur==j1.couleur]
            j2.pieces=[value for key,value in plateau.items() if value.couleur==j2.couleur]
            self.j1=j1
            self.j2=j2
                
                
        else :
            print("Chargement de la partie")
            fichier = open(plateau+".txt", 'r')
            sauv_txt = fichier.read()
            fichier.close()
            #maintenant il faut extraire le texte important : 
            pionsj1,pionsj2 = sauv_txt.split("\n")
            pionsj1 = pionsj1[10:]
            pionsj2 = pionsj2[10:]
            #for i in pionsj1.split(";"):
            print(pionsj1)
            plateau=np.full((8,8),Piece())


    def __str__(self)->str:
        """Méthode print pour la partie. Affiche le plateau dans
        son état actuel.

        Returns:
            str: Le plateau.
        """
        
        p=""
        i=0
        num_ligne=[str(x) for x in range(1,9)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        p+="    " +  "    ".join(nom_col) +"\n"
        for i in range(8):
           
            p+=num_ligne[i] + "   "
            
            for j in range(8):
                try:
                    p+=self.plateau[(i,j)].__str__() + "  | "
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
            sauvegarde+=f"({i.nom},{i.couleur},{i.coord});"
        sauvegarde+="\nJoueur2 : "    
        for i in self.j1.pieces:
            sauvegarde+=f"({i.nom},{i.couleur},{i.coord});"
            
        if sauvegarde is None:
            nom_fichier = input("nom du fichier de sauvegarde : ")
        fichier = open(nom_fichier+".txt", 'w')
        fichier.write(sauvegarde)
        fichier.close()
    
    
    
    def deplacer_piece(self, coord1: tuple[int,int], coord2: tuple[int, int])->dict:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord1 (tuple[int,int]): Position de la pièce à déplacer
            coord2 (tuple[int,int]): Position finale de la pièce
        Returns:
            dict: Le plateau modifié
            """

        if isinstance(self.plateau[coord1] ,Pion):
            self.plateau[coord1].premier_coup=False
        
        
        self.plateau[coord2] = self.plateau.pop(coord1)
                
    def echec(self,couleur: bool) -> bool:
        """Fonction qui nous dis si le roi de la couleur demandé est en échec

        Args:
            couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

        Returns:
            bool: True <=> Roi en échec
        """
        liste_case_controllee=[]
        if couleur: #On regarde l'échec du roi Blanc
            for piece in self.j2.pieces: #Pour les pièces noire en jeu
                liste_case_controllee+=piece.cases_controllees #On ajoute les case controllé par chaque pieces adverse à l'ensemble des cases controllé par l'adversaire

            for case in liste_case_controllee: # Pour chaque case controllé par l'adversaire
                try:
                    piece=self.plateau[case]
                    if piece.nom=="Roi" and couleur: #On vérifie si cette pièce 
                        return True
                    
                except: #Il n'y a pas de case à ces coordonnées
                    pass                
        
        else:
            for piece in self.j1.pieces:
                liste_case_controllee+=piece.cases_controllées

            for case in liste_case_controllee:
                piece=self.plateau[case]
                if piece.nom=="Roi" and not piece.couleur:
                    return True
                
        return False


    def case_occupe(self, coord: tuple[int,int], couleur: bool):
        '''
        Nous renvoie si la case de coordonnées coord est déjà occupé par une des pieces de la même couleur
        Input:
            coord (tuple[int,int]): coordonnées de la case
            couleur: couleur de la piece concerné, on doit donc voir si la case est occupé par cette couleur

        Output: Bool
            La case est occupé par une piece de même couleur -> True
            La case n'est pas occupé par une piece de même couleur -> False
        '''
        try:
            piece=self.plateau[coord]
            if piece.couleur==couleur:
                return True
            else:
                return False
        except:
            return False


    def echec_et_mat():
        pass
    
    def gagnant(self):
        
        pass
           





j1=Humain("Malik",1)
j2=Humain("Basile", 0)
p=Partie(j1,j2)

p.deplacer_piece((0,0),(3,3))
print(p)

