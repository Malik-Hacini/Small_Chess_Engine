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
            plateau=np.full((8,8),Piece())

            plateau[1]=[Pion(couleur=False,coord=(1,i)) for i in range(8)]
            plateau[6]=[Pion(couleur=True, coord=(6,i)) for i in range(8)]

            for couleur in [True,False]:

                if couleur: ligne=7
                else: ligne = 0
                
                for col in [0,7]: 
                    plateau[ligne,col]=Tour(couleur,coord=(ligne,col))
                   
                for col in [1,6]:
                    plateau[ligne,col]=Cavalier(couleur,coord=(ligne,col))
                   
                for col in [2,5]:
                    plateau[ligne,col]=Fou(couleur,coord=(ligne,col))
                    
                plateau[ligne,3]=Reine(couleur,coord=(ligne,3))
                plateau[ligne,4]=Roi(couleur, coord=(ligne,4))     
            
            
            
            
            self.plateau=plateau
            j1.pieces=[i for x in plateau for i in x if i.couleur==j1.couleur]
            j2.pieces=[i for x in plateau for i in x if i.couleur==j2.couleur]
            self.j1=j1
            self.j2=j2
                
                
        else :
            print("chargement de la partie")
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
        """méthode print pour la partie. Affiche le plateau dans
        son état actuel

        Returns:
            str: Le plateau.
        """
        
        p=""
        i=0
        num_ligne=[str(x) for x in range(8)]
        nom_col=["A","B" ,"C",
                 "D","E" ,"F","G","H"]
        
        p+="    " +  "    ".join(nom_col) +"\n"
        for ligne in self.plateau:
            
            p+=num_ligne[i] + "   "
            i+=1
            
            for piece in ligne:
                p+=piece.__str__() + "  | "
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
    
        
        
        
        
        
    
    
    
    def deplacer_piece(self, coord1: tuple[int,int], coord2: tuple[int, int])->np.ndarray:
        """Déplace une pièce du plateau à un autre endroit.
        Cette méthode n'est exécutée que si le coup est valide,
        il n'y a donc pas besoin de le vérifier.

        Args:
            coord1 (tuple[int,int]): Position de la pièce à déplacer
            coord2 (tuple[int,int]): Position finale de la pièce
        Returns:
            np.ndarray: Le plateau modifié
            """
        
        self.plateau[coord1[0],coord1[1]].coord=coord2

        self.plateau[coord1[0],coord1[1]] , self.plateau[coord2[0],coord2[1]] = Piece(), self.plateau[coord1[0],coord1[1]]
        
        




j1=Humain("Malik",1)
j2=Humain("Basile", 0)
p=Partie(j1,j2)

p.deplacer_piece((0,0),(3,3))
print(p)
for i in enumerate(j1.pieces):
    print(i)
    
    
p.sauvegarder("sauvegarde")
p2 = Partie(j1,j2,"sauvegarde")