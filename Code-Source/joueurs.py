import numpy as np
import math
from EtatJeu import *
import random


class Joueur():
    """Représente un joueur d'échecs,qui possède un nom et une couleur.
    Est destinée à être la super-classe des joueurs concrets (Humain, IA)
    """
    def __init__(self,nom : str,couleur : bool) -> None:
        """création d'un joueur

        Args:
            nom (str): nom du joueur
            couleur (bool): True <=> Blanc
        """
        self.nom = nom
        self.couleur = couleur


class Humain(Joueur):
    """Représente un joueur humain, qui possède un nom et une couleur.

    Args:
        Joueur (class): super classe
    """
    def __init__(self, nom: str, couleur: bool) -> None:
        super().__init__(nom, couleur)
        
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
        """Fait jouer un coup à l'utilisateur.

        Args:
            partie (dict): la partie en cours

        Returns:
            tuple[int,int]: le coup.
        """
        coup_jouable  = False
        while not coup_jouable:
            
            piece_deplacable = False
            
            while not piece_deplacable:
                #On doit vérifier la validité de chaque étape du coup.
                coord_p = input(f"{self.nom}, ou est la pièce à bouger ? \n")
                
                if coord_p in ["save","nulle"]: return coord_p
                if not len(coord_p)==2:
                    print("ce n'est pas un coup valide, veuillez respecter ce format : e2 \n")
                
                elif coord_p[0] not in ("a","b","c","d","e","f","g","h") or coord_p[1] not in ("1","2","3","4","5","6","7","8"):
                    print("Ce n'est pas un coup valide! \n")
                
                
                else : 
                    #Transformation de la position de la pièce de notation algébrique aux coordonnées absolues dans le plateau.
                    #Pour la ligne, cela dépend de la couleur du joueur, l'affichage étant renversé quand les noirs jouent.
                    coord_p = conv_str(coord_p)
                    if coord_p not in partie.plateau.keys() : print("Cette case est vide.")
                    
                    elif partie.plateau[coord_p] not in partie.pieces[self.couleur]: print("Cette case ne comporte pas de piece de votre couleur. \n")
                    #vérifier que la piece peut etre bougée
                    elif partie.plateau[coord_p].coups_legaux(partie) == [] : print("Cette pièce ne peut pas être bougée. \n")
                    #la piece peut etre déplacée
                    else : piece_deplacable = True
            
            #donner les coups possibles pour cette pièce
            coups_possibles=partie.plateau[coord_p].coups_legaux(partie)
            coups_a_afficher_not_alg=[conv_int(coup) for coup in coups_possibles]
            
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

                coup_int = conv_str(coup)
                        
                premier_passage=False
            coup_jouable=True

        return coord_p,coup_int
        
        
        
        
class IA(Joueur):
    """Représente un joueur de type IA du jeu d'échecs. Basée sur les fonctions minimax et alphabeta définies plus bas
    Une IA possède un nom, une couleur, et une profondeur (de recherche dans le minimax), représentée comme "niveau" à l'utilisateur.
    Args:
        Joueur (class): super classe
    """
    def __init__(self, nom: str, couleur: bool,profondeur = 0) -> None:
        """initialise une ia

        Args:
            nom (str): nom de l'ia 
            couleur (bool): couleur de l'ia
            profondeur (int, optional): profondeur du minimax/alphabeta. Defaults to 0.
        """
        super().__init__(nom, couleur)
        self.profondeur = profondeur
        self.endgame = False
        self.algo = "alphabeta"#permet de choisir l'algo de l'ia
    
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
        """Détermine le coup d'une IA, selon ses paramètres.

        Args:
            partie (dict): partie dans son état actuel.

        Returns:
            tuple[int,int]: coup.
        """
        couleurs=["noire","blanche"]
        print(f"\n L'IA {couleurs[self.couleur]} réflechit \n")
        meilleur_coup = None
        alpha = -math.inf
        beta = math.inf
        #coups aléatoire
        if self.profondeur == 0:
            coups = []
            for coord_i,coords_f in partie.mouvements(self.couleur).items():
                for coord_f in coords_f:
                    coups.append((coord_i,coord_f))
            return coups[random.randint(0,len(coups)-1)]
        
        #si le coup n'est pas aléatoire
        if self.couleur :
            meilleure_valeur = -math.inf
            for coord_i,coords_f in partie.mouvements(self.couleur).items():
                #récupere les coordonnées de départ de chaque piece qui peut être déplacée, et les cases sur laquelle elle peut se déplacer
                
                #Ici, l'idée est de simuler touts les coups possibles.
                #On sauvegarde toutes les informations de la partie que nous allons modifier pendant la simulation,
                #on les modifie pour en extraire la valeur du jeu après le coup, puis on les rétablit.
                

                #pour chaque coups possible dans les déplacement disponibles de la piece
                for coord_f in coords_f:
                    #sauvegarder les données du plateau de jeu
                    piece_retirée = partie.plateau.get(coord_f,None)
                    
                    #on sauvegarde l'odometre
                    for piece in partie.pieces[not partie.trait]:
                        if isinstance(piece,Roi):
                            sauv_odometre = piece.odometre
                            roi = piece
                    #on déplace la piece
                    partie.deplacer_piece(coord_i,coord_f)
                    
                    #calcul de la valeur avec l'algo voulu
                    if self.algo == "minimax" : 
                        valeur = minimax(partie,self.profondeur-1, not self.couleur)
                    else:
                        valeur = alphabeta(partie,self.profondeur-1,alpha,beta, not self.couleur)
                    
                    #retirer coup
                    #remettre la piece au bon endroit
                    partie.deplacer_piece(coord_f,coord_i)
                    if piece_retirée is not None:
                        partie.plateau[coord_f] = piece_retirée
                        partie.pieces[not partie.trait].append(piece_retirée)
                        
                    #remettre l'odometre à sa valeur de départ
                    roi.odometre = sauv_odometre
                    
                    #le joueur blanc le maximum
                    if valeur> meilleure_valeur:
                        meilleur_coup = coord_i,coord_f
                        meilleure_valeur = valeur
                        
                    #modification du alpha pour le minimax avec elagage alpha beta
                    alpha = max(alpha,valeur)
        else :
            meilleure_valeur = math.inf
            for coord_i,coords_f in partie.mouvements(self.couleur).items():
                #pour chaque coups possible dans les déplacement disponibles de la piece
                for coord_f in coords_f:
                    #sauvegarder les données du plateau de jeu
                    piece_retirée = partie.plateau.get(coord_f,None)
                    
                    #on sauvegarde l'odometre
                    for piece in partie.pieces[not partie.trait]:
                        if isinstance(piece,Roi):
                            sauv_odometre = piece.odometre
                            roi = piece
                            
                    #on bouge une piece
                    partie.deplacer_piece(coord_i,coord_f)
                    #calcul de la valeur avec l'algo voulu
                    if self.algo == "minimax" : 
                        valeur = minimax(partie,self.profondeur-1, not self.couleur)
                    else:
                        valeur = alphabeta(partie,self.profondeur-1,alpha,beta, not self.couleur)
                    
                    #retirer coup
                    partie.deplacer_piece(coord_f,coord_i)#remettre la piece au bon endroit
                    if piece_retirée is not None:
                        partie.plateau[coord_f] = piece_retirée
                        partie.pieces[not partie.trait].append(piece_retirée)
                    
                    #remettre l'odometre a sa valeur
                    roi.odometre = sauv_odometre
                
                    #le joueur noir veut le minimum, le joueur blanc le maximum
                    if valeur< meilleure_valeur:
                        meilleur_coup = coord_i,coord_f
                        meilleure_valeur = valeur
                    beta = min(beta,valeur)
        return meilleur_coup
    
def conv_str(coord):
    """Simple convertisseur de notation algébrique en coordonnées entières
    """
    return (ord(coord[0])-97,int(coord[1])-1)


def conv_int(coord):
    "Simple convertisseur de coordonnées entières en notation algébrique"""
    return(chr(97+coord[0])+str(coord[1]+1))



def minimax(etat, profondeur,couleur):
    """Implémentation de l'algorithme minimax appliqué à notre exemple

    Args:
        etat (EtatJeu): etat de la partie à analyser
        profondeur (int): nombre de profondeur restante a analyser
        couleur (bool): couleur dont il faut identifier la valeur du jeu

    Returns:
        int: valeur du minimax
    """
    if profondeur==0 or etat.echec_et_mat():
        return etat.calcul_valeur()
    if couleur:
        valeur = -math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #sauvegarder les données du plateau de jeu
                piece_retirée = etat.plateau.get(coord_f,None)
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                
                #on bouge la piece
                etat.deplacer_piece(coord_i,coord_f)
                #calcul recursif de la valeur
                valeur = max(valeur,minimax(etat,profondeur-1, not couleur))
                #retirer coup
                #remettre la piece au bon endroit
                etat.deplacer_piece(coord_f,coord_i)
                if piece_retirée is not None:
                    etat.plateau[coord_f] = piece_retirée
                    etat.pieces[not etat.trait].append(piece_retirée)
                #remettre l'odometre a sa valeur
                roi.odometre = sauv_odometre
                
        return valeur
    else :
        valeur = math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #sauvegarder les données du plateau de jeu
                piece_retirée = etat.plateau.get(coord_f,None)
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                        
                #on bouge la piece
                etat.deplacer_piece(coord_i,coord_f)
                #calcul recursif de la valeur
                valeur = min(valeur,minimax(etat,profondeur-1, not couleur))
                #retirer coup
                etat.deplacer_piece(coord_f,coord_i)#remettre la piece au bon endroit
                if piece_retirée is not None:
                    etat.plateau[coord_f] = piece_retirée
                    etat.pieces[not etat.trait].append(piece_retirée)
                #remettre l'odometre a sa valeur
                roi.odometre = sauv_odometre
                    
        return valeur



def alphabeta(etat, profondeur,alpha,beta,couleur):
    """Implémentation de l'algorithme minimax avec élagage alpha beta appliqué à notre exemple

    Args:
        etat (EtatJeu): etat de la partie à analyser
        profondeur (int): nombre de profondeur restante a analyser
        couleur (bool): couleur dont il faut identifier la valeur du jeu

    Returns:
        int: valeur du minimax
    """
    if profondeur==0 or etat.echec_et_mat():
        
        return etat.calcul_valeur()
    if couleur:
        valeur = -math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #sauvegarder les données du plateau de jeu
                piece_retirée = etat.plateau.get(coord_f,None)
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                #on bouge la piece
                
                etat.deplacer_piece(coord_i,coord_f)
                #calcul recursif de la valeur
                valeur = max(valeur,alphabeta(etat,profondeur-1,alpha,beta, not couleur))
                #retirer coup
                etat.deplacer_piece(coord_f,coord_i)#remettre la piece au bon endroit
                if piece_retirée is not None:
                    etat.plateau[coord_f] = piece_retirée
                    etat.pieces[not etat.trait].append(piece_retirée)
                #remettre l'odometre a sa valeur
                roi.odometre = sauv_odometre
                
                if valeur > beta :
                    break
                alpha = max(alpha,valeur)
        return valeur
    else :
        valeur = math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #sauvegarder les données du plateau de jeu
                piece_retirée = etat.plateau.get(coord_f,None)
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                
                #on bouge la piece        
                etat.deplacer_piece(coord_i,coord_f)
                #calcul recursif de la valeur
                valeur = min(valeur,alphabeta(etat,profondeur-1,alpha,beta, not couleur))
                #retirer le coup
                etat.deplacer_piece(coord_f,coord_i)#remettre la piece Nau bon endroit
                if piece_retirée is not None:
                    etat.plateau[coord_f] = piece_retirée
                    etat.pieces[not etat.trait].append(piece_retirée)
                    
                #remettre l'odometre a sa valeur
                roi.odometre = sauv_odometre
                
                if valeur < alpha :
                    break
                beta = min(beta,valeur)
        return valeur