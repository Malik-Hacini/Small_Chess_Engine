import numpy as np
import math
from EtatJeu import *
from stockfish import Stockfish
import random

stockfish = Stockfish("stockfish\\stockfish-windows-x86-64-avx2.exe")




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
        
class Stockfish(Joueur):
    
    def __init__(self, nom: str, couleur: bool, elo : int = 1350) -> None:
        super().__init__(nom, couleur)
        #stockfish.set_elo_rating(elo)
        stockfish.set_skill_level(elo)
        
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
        
        stockfish.set_fen_position(partie.fen_position())
        
        move = stockfish.get_best_move()
        return (conv_str(move[:2]),conv_str(move[2:]))
        
        
        
        
class IA(Joueur):
    """Représente un joueur de type IA du jeu d'échecs. Basée sur les fonctions minimax et alphabeta définies plus bas
    Une IA possède un nom, une couleur, et une profondeur (de recherche dans le minimax), représentée comme "niveau" à l'utilisateur.
    Args:
        Joueur (class): super classe
    """
    def __init__(self, nom: str, couleur: bool,profondeur = 0) -> None:
        super().__init__(nom, couleur)
        self.profondeur = profondeur
        self.endgame = False
        self.algo = "alphabeta"
    
    
    def jouer_coup(self,partie: dict) -> tuple[int,int]:
        """Détermine le coup d'une IA, selon ses paramètres.

        Args:
            partie (dict): partie dans son état actuel.

        Returns:
            tuple[int,int]: coup.
        """
        
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
        
        
        if self.couleur :
            meilleure_valeur = -math.inf
            for coord_i,coords_f in partie.mouvements(self.couleur).items():
                
                #Ici, l'idée est de simuler touts les coups possibles.
                #On sauvegarde toutes les informations de la partie que nous allons modifier pendant la simulation,
                #on les modifie pour en extraire la valeur du jeu après le coup, puis on les rétablit.
                

                #pour chaque coups possible dans les déplacement disponibles de la piece
                for coord_f in coords_f:
                    #créer un nouvel état où on bouge une piece
                    #simu = copy.deepcopy(partie)
                    piece_retirée = partie.plateau.get(coord_f,None)
                    #on bouge une piece
                    
                    #on sauvegarde l'odometre
                    for piece in partie.pieces[not partie.trait]:
                        if isinstance(piece,Roi):
                            sauv_odometre = piece.odometre
                            roi = piece
                    
                        
                    partie.deplacer_piece(coord_i,coord_f)
                    #max
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
                    
                    #le joueur blanc le maximum
                    if valeur> meilleure_valeur:
                        meilleur_coup = coord_i,coord_f
                        meilleure_valeur = valeur
                    #cette condition ne sert a rien on compare une valeur finie à plus l'infinie. car beta ne change pas
                    if valeur > beta :
                        break
                    alpha = max(alpha,valeur)
        else :
            meilleure_valeur = math.inf
            for coord_i,coords_f in partie.mouvements(self.couleur).items():
                
                #pour chaque coups possible dans les déplacement disponibles de la piece
                for coord_f in coords_f:
                    #créer un nouvel état où on bouge une piece
                    #simu = copy.deepcopy(partie)
                    piece_retirée = partie.plateau.get(coord_f,None)
                    #on bouge une piece
                    
                    #on sauvegarde l'odometre
                    for piece in partie.pieces[not partie.trait]:
                        if isinstance(piece,Roi):
                            sauv_odometre = piece.odometre
                            roi = piece
                            
                    
                    partie.deplacer_piece(coord_i,coord_f)
                    #max
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
                    #print(valeur)
                    if valeur< meilleure_valeur:
                        meilleur_coup = coord_i,coord_f
                        meilleure_valeur = valeur
                    if valeur < alpha :
                        break
                    beta = min(beta,valeur)
            
        #print(time.time()-début)
        return meilleur_coup
    
def conv_str(coord):
    """Simple convertisseur de notation algébrique en coordonnées entières
    """
    return (ord(coord[0])-97,int(coord[1])-1)


def conv_int(coord):
    "Simple convertisseur de coordonnées entières en notation algébrique"""
    return(chr(97+coord[0])+str(coord[1]+1))



def minimax(etat, profondeur,couleur):
    
    """A FAIRE"""
    if profondeur==0 or etat.echec_et_mat():
        return etat.calcul_valeur()
    if couleur:
        valeur = -math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                piece_retirée = etat.plateau.get(coord_f,None)
                #on bouge une piece
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                
                etat.deplacer_piece(coord_i,coord_f)
                #max
                valeur = max(valeur,minimax(etat,profondeur-1, not couleur))
                #retirer coup
                etat.deplacer_piece(coord_f,coord_i)#remettre la piece au bon endroit
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
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                piece_retirée = etat.plateau.get(coord_f,None)
                #on bouge une piece
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                        
                etat.deplacer_piece(coord_i,coord_f)
                #max
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
    """A FAIRE"""
    if profondeur==0 or etat.echec_et_mat():
        
        return etat.calcul_valeur()
    if couleur:
        valeur = -math.inf
        for coord_i,coords_f in etat.mouvements(etat.trait).items():
            for coord_f in coords_f:
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                piece_retirée = etat.plateau.get(coord_f,None)
                #on bouge une piece
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                
                etat.deplacer_piece(coord_i,coord_f)
                #max
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
                #créer un nouvel état où on bouge une piece, penser à changer le tour
                piece_retirée = etat.plateau.get(coord_f,None)
                #on bouge une piece
                
                #on sauvegarde l'odometre
                for piece in etat.pieces[not etat.trait]:
                    if isinstance(piece,Roi):
                        sauv_odometre = piece.odometre
                        roi = piece
                        
                        
                        
                etat.deplacer_piece(coord_i,coord_f)
                #max
                valeur = min(valeur,alphabeta(etat,profondeur-1,alpha,beta, not couleur))
                #retirer coup
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