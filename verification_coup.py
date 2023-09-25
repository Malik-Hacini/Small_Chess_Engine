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


def case_controlle(x,y,couleur):
    '''
    Nous renvoie si la case de coordonnées x,y est controllé par l'adversaire
    Input:
        x,y: coordonnées de la case
        couleur: couleur de la piece concerné, on doit donc voir si la case est controllé par l'autre couleur

    Output: Bool
        La case est controllé par l'adversaire -> True
        La case n'est pas controllé par l'adversaire -> False
    '''
    pass

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
    piece=plateau[x][y]
    if piece.couleur==couleur:
        return True
    else:
        return False