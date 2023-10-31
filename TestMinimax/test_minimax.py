import pytest
from joueurs import*
from EtatJeu import*
from piece import*

def initialiser_plateau_bots(partie):
    bot1,bot2 = IA("Joueur1",True,2),IA("Joueur2",False,2)
    Jeu = EtatJeu(partie)
    return Jeu,bot1,bot2

def test_minimax_0_profond():
    partie,bot1,bot2 = initialiser_plateau_bots()
    
def test_minimax_plus_profond():
    partie,bot_blanc,bot_noir = initialiser_plateau_bots("suicide")
    coup = bot_blanc.jouer_coup(partie)
    partie.deplacer_piece(coup[0],coup[1])
    print(partie)
    print(conv(coup[0],coup[1]))
    coup = bot_noir.jouer_coup(partie)
    partie.deplacer_piece(coup[0],coup[1])
    print(partie)
    print(conv(coup[0],coup[1]))
    assert not partie.echec_et_mat()
    
test_minimax_plus_profond()