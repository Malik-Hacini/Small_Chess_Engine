import numpy as np
import math
import EtatJeu
import copy
import time


class Joueur():
    def __init__(self,nom : str,couleur : bool) -> None:
        """création d'un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True -> blanc, False -> noir
        """
        self.nom = nom
        self.couleur = couleur


class Humain(Joueur):
    def __init__(self, nom: str, couleur: bool) -> None:
        super().__init__(nom, couleur)
        
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:

        #demander la case à jouer
        #vérifier si elle possedes des coups possibles
        #print(minimax(partie, 2, partie.trait))
        coup_jouable  = False
        while not coup_jouable:
            
            piece_deplacable = False
            
            while not piece_deplacable:
                coord_p = input(f"{self.nom}, ou est la pièce à bouger ? \n")
                
                if coord_p == "save" : return "save"
                # vérifier que le coup est au bon format cad (a:h),(1:8)
                if not len(coord_p)==2:
                    print("ce n'est pas un coup valide, veuillez respecter ce format : e2 \n")
                
                elif coord_p[0] not in ("a","b","c","d","e","f","g","h") or coord_p[1] not in ("1","2","3","4","5","6","7","8"):
                    print("Ce n'est pas un coup valide! \n")
                
                
                else : 
                    #Transformation de la position de la pièce de notation algébrique aux coordonnées absolues dans le plateau.
                    #Pour la ligne, cela dépend de la couleur du joueur, l'affichage étant renversé quand les noirs jouent.
                    coord_p = (ord(coord_p[0])-97,int(coord_p[1])-1)
                    if coord_p not in partie.plateau.keys() : print("Cette case est vide.")
                    
                    elif partie.plateau[coord_p] not in partie.pieces[self.couleur]: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[coord_p].coups_legaux(partie) == [] : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_deplacable = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles=partie.plateau[coord_p].coups_legaux(partie)
            coups_a_afficher_not_alg=[(chr(coup[0]+97)+str(coup[1]+1)) for coup in coups_possibles]
            
            coups_a_afficher_output=""
            for coup in coups_a_afficher_not_alg:
                coups_a_afficher_output+=f"{coup}, "
            
            
            print(f"vous pouvez déplacer votre {partie.plateau[coord_p].nom} sur les cases suivantes : ", coups_a_afficher_output[:-2]+".")
            #vérifier si le joueur veut bien jouer cette piece ou modifier son coupS
            coup_int = None
            premier_passage=True
            while coup_int not in coups_possibles:
                
                if not premier_passage:
                    print("Ce coup n'est pas valide. \n")
                
                #demander la case où le joueur veut déplacer le pion
                coup = input("Quel coup voulez-vous jouer (None si vous voulez jouer une autre piece)? \n")

                coup_int = (ord(coup[0])-97,int(coup[1])-1)
                        
                premier_passage=False
            coup_jouable=True

        return coord_p,coup_int
        
        
        
class IA(Joueur):
    def __init__(self, nom: str, couleur: bool) -> None:
        super().__init__(nom, couleur)      
        
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
        """Permet a l'ia de jouer un coup, cela calcule toutes les possibilités

        Args:
            partie (dict): Etat du Jeu a l'instant

        Returns:
            tuple[int,int]: coup joué
        """
        durées = []
        
        meilleur_coup = None
        max_valeur = ((-1)**(self.couleur))*math.inf
        
        chargement = 0
        taille = len(partie.mouvements(self.couleur).items())
        for coord_i,coords_f in partie.mouvements(self.couleur).items():
            chargement+=1/taille
            print(f'{round(chargement*100)}% effectués')
            #print(f" analyse du {partie.plateau[coord_i].nom} en {chr(97+coord_i[0])}{coord_i[1]+1}",end = ", ")
            #print(f'déplacementst possible : {coords_f}'  )
            
            for coord_f in coords_f:
                #créer un nouvel état où on bouge une piece
                départ = time.time()
                simu = copy.deepcopy(partie)
                durées.append(time.time()-départ)
                #on bouge une piece
                simu.deplacer_piece(coord_i,coord_f)
                #max
                val_minimax = minimax(simu,0,not self.couleur)
                #le joueur noir veut le minimum, le joueur blanc le maximum
                if (val_minimax > max_valeur and self.couleur) or (val_minimax < max_valeur and not self.couleur):
                    meilleur_coup = (coord_i,coord_f)
                    max_valeur = val_minimax
        print(sum(durées)/len(durées))
        return meilleur_coup
                    
            


    #déterminer le meilleur coup grace à minimax




def minimax( etat : EtatJeu ,profondeur : int,couleur : bool):
    if profondeur==0 or etat.echec_et_mat():
        etat.calcul_valeur()
        return etat.valeur
    if couleur:
        valeur = -math.inf
        for coord_i,coords_f in etat.mouvements(couleur).items():
            for coord_f in coords_f:
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                simu = copy.deepcopy(etat)
                #on bouge une piece
                simu.deplacer_piece(coord_i,coord_f)
                
                #max
                
                valeur = max(valeur,minimax(simu,profondeur-1, not couleur))
            
        return valeur            
    else :
        valeur  = math.inf
        for coord_i,coords_f in etat.mouvements(couleur).items():
            for coord_f in coords_f:
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                simu = copy.deepcopy(etat)
                #on bouge une piece
                simu.deplacer_piece(coord_i,coord_f)
                #max
                valeur = min(valeur,minimax(simu,profondeur-1, not couleur))
        return valeur
    
        
        
        