def existance_case(x,y):
    '''
    Vérifie si la case x,y existe
    Input: coordonnées x,y de la case
    Output: Bool True=> Case existe, False=> Case n'existe pas
    '''
    if 0>x or x>8:
        return False
    elif 0>y or y>8:
        return False
    else:
        return True

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
    piece=partie.plateau[x][y]
    if piece.couleur==couleur:
        return True
    else:
        return False

def tri_deplacement_echec(piece, liste_deplacement):
    '''
    Vérifie si il y a une situation d'échec contre  la couleur d'une pièce déplacé à une liste de déplacement. Par la même
    occasion supprime les déplacement qui conduisent à une situation d'échec.
    Input: piece: Pièce  La pièce que l'on déplace 
           liste_deplacement: list La liste des déplacement qu'on veut faire
    Output: liste_déplacement: list La liste ou on a retiré les déplacements qui mène à un échec
    '''
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
    if couleur:
        for piece in joueur2.pieces:
            liste_case_controllee+=piece.cases_controllées

        for case in liste_case_controllee:
            x,y= case
            piece=partie.plateau[x][y]
            if piece.name=="Roi" and piece.couleur:
                return True
    
    else:
        for piece in joueur1.pieces:
            liste_case_controllee+=piece.cases_controllées

        for case in liste_case_controllee:
            x,y= case
            piece=partie.plateau[x][y]
            if piece.name=="Roi" and not piece.couleur:
                return True
            
    return False
