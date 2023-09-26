from pièce import*
from joueurs import*
from Partie import*

def case_occupe(x,y, couleur):
    '''
    Nous renvoie si la case de coordonnées x,y est déjà occupé par une des pieces de la même couleur
    Input:
        x,y: coordonnées de la case
        couleur: couleur de la piece concerné, on doit donc voir si la case est occupé par cette couleur

    Output: Bool
        La case est occupé par une piece de même couleur -> True
        La case n'est pas occupé par une piece de même couleur -> False
    '''
    try:
        piece=partie.plateau[f"({x},{y})"]
        if piece.couleur==couleur:
            return True
        else:
            return False
    except Exception:
        return False

def tri_deplacement_echec(piece: Pièce, liste_deplacement: list)->list:
    """Fonction qui simule une liste de déplacements et suprime les déplacements qui mène à des echecs

    Args:
        piece (Pièce): La pièce qu'on déplace 
        liste_deplacement (list): La liste de déplacement que l'on simule

    Returns:
        list: La liste des déplacements triée des situations qui mettent en échec
    """
    x_i, y_i = piece.coord
    for deplacement in liste_deplacement:
        x,y = deplacement
        piece.bouger_piece(x,y)
        if echec(piece.couleur):
            liste_deplacement.remove(deplacement)
    piece.bouger_piece(x_i, y_i)
    
    return liste_deplacement

def echec(couleur : bool) -> bool:
    """Fonction qui nous dis si le roi de la couleur demandé est en échec

    Args:
        couleur (bool): Couleur de du roi dont on veut savoir si il est en échec (True<=> Blanc et False <=> Noir)

    Returns:
        bool: True <=> Roi en échec
    """
    liste_case_controllee=[]
    if couleur: #On regarde l'échec du roi Blanc
        for piece in joueur2.pieces: #Pour les pièces noire en jeu
            liste_case_controllee+=piece.cases_controllées #On ajoute les case controllé par chaque pieces adverse à l'ensemble des cases controllé par l'adversaire

        for case in liste_case_controllee: # Pour chaque case controllé par l'adversaire
            x,y= case #On pprend ses coordonnées 
            try:
                piece=partie.plateau[f"({x},{y})"]
                if piece.nom=="Roi" and couleur: #On vérifie si cette pièce 
                    return True
                
            except Exception: #Il n'y a pas de case à ces coordonnées
                pass                
    
    else:
        for piece in joueur1.pieces:
            liste_case_controllee+=piece.cases_controllées

        for case in liste_case_controllee:
            x,y= case
            piece=partie.plateau[f"({x},{y})"]
            if piece.name=="Roi" and not piece.couleur:
                return True
            
    return False
