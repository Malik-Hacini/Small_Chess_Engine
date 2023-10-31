import pytest
from joueurs import*
from EtatJeu import*
from piece import*

def initialiser_plateau_bots(partie):
    bot1,bot2 = IA("Joueur1",True,2),IA("Joueur2",False,2)
    Jeu = EtatJeu(partie)
    return Jeu,bot1,bot2