def joueur_minimax(jeu,etat):
    j=jeu.joueur(etat)
    
    def max_valeur(etat):
        if jeu.est_final(etat):
            return jeu.valeur(etat,j)
        v=-infinity
        for (m,s) in jeu.suivants(etat):
            v=max(v,min_valeur(s))
        return v

    def min_valeur(etat):
        if jeu.est_final(etat):
            return jeu.valeur(etat,j)
        v=infinity
        for (m,s) in jeu.suivants(etat):
            v=min(v,max_valeur(s))
        return v
    
    tab_suivants=jeu.suivants(etat)
    min_suivants=[min_valeur(s) for (e,s) in tab_suivants]
    M=max(min_suivants)  
    mouvement,e = tab_suivants[min_suivants.index(M)]
    return mouvement