from numpy import average
import pytest
from joueurs import*
from EtatJeu import*
from piece import*
import time




#fonction pour initialiser un plateau avec deux bots
def initialiser_plateau_bots(partie="Plateau_base",profondeur_blanc = 2,profondeur_noir = 2):
    bot1,bot2 = IA("Joueur1",True,profondeur_blanc),IA("Joueur2",False,profondeur_noir)
    Jeu = EtatJeu(partie)
    return Jeu,bot1,bot2

#test IA aléatoire (niveau==0)
def test_IA_0():
    partie,bot1,bot2 = initialiser_plateau_bots(profondeur_blanc=0,profondeur_noir=0)
    #blanc
    coup = bot1.jouer_coup(partie)
    assert coup[0] in partie.mouvements(True).keys()
    assert coup[1] in partie.mouvements(True)[coup[0]]
    partie.deplacer_piece(coup[0],coup[1])
    #noir
    coup = bot2.jouer_coup(partie)
    assert coup[0] in partie.mouvements(False).keys()
    assert coup[1] in partie.mouvements(False)[coup[0]]
    

#test jouer un coup
def test_minimax_profondeur_1():
    partie,bot1,bot2 = initialiser_plateau_bots(profondeur_blanc=1,profondeur_noir=1)
    #blanc
    coup = bot1.jouer_coup(partie)
    assert coup[0] in partie.mouvements(True).keys()
    assert coup[1] in partie.mouvements(True)[coup[0]]
    partie.deplacer_piece(coup[0],coup[1])
    #noir
    coup = bot2.jouer_coup(partie)
    assert coup[0] in partie.mouvements(False).keys()
    assert coup[1] in partie.mouvements(False)[coup[0]]

def test_minimax_profondeur_2():
    partie,bot1,bot2 = initialiser_plateau_bots(profondeur_blanc=2,profondeur_noir=2)
    #blanc
    coup = bot1.jouer_coup(partie)
    assert coup[0] in partie.mouvements(True).keys()
    assert coup[1] in partie.mouvements(True)[coup[0]]
    partie.deplacer_piece(coup[0],coup[1])
    #noir
    coup = bot2.jouer_coup(partie)
    assert coup[0] in partie.mouvements(False).keys()
    assert coup[1] in partie.mouvements(False)[coup[0]]
    
    
def test_minimax_profondeur_3():
    partie,bot1,bot2 = initialiser_plateau_bots(profondeur_blanc=3,profondeur_noir=3)
    #blanc
    coup = bot1.jouer_coup(partie)
    assert coup[0] in partie.mouvements(True).keys()
    assert coup[1] in partie.mouvements(True)[coup[0]]
    partie.deplacer_piece(coup[0],coup[1])
    #noir
    coup = bot2.jouer_coup(partie)
    assert coup[0] in partie.mouvements(False).keys()
    assert coup[1] in partie.mouvements(False)[coup[0]]
    
#test si minimax ne se suicide pas 
def test_pas_de_suicide():
    #initialisation d'un plateau ou les blanc peuvent etre mis en mat en 1, on vérifie qu'il ne joue pas un coup qui le ferai perdre
    partie,bot_blanc,bot_noir = initialiser_plateau_bots("Sauvegarde_Test_IA\\suicide")
    coup = bot_blanc.jouer_coup(partie)
    partie.deplacer_piece(coup[0],coup[1])
    coup = bot_noir.jouer_coup(partie)
    partie.deplacer_piece(coup[0],coup[1])
    assert not partie.echec_et_mat()





#test si minimax et alphabeta jouent le meme coup (profondeur 2)
def test_alphabeta():
    plateaux = ["Sauvegarde_Test_IA\\Plateau_base","Sauvegarde_Test_IA\\suicide"]
    for plateau in plateaux:
        partie_ab,bot_blanc_ab,bot_noir_ab = initialiser_plateau_bots(plateau)
        partie_mm,bot_blanc_mm,bot_noir_mm= initialiser_plateau_bots(plateau)
        bot_blanc_mm.algo = "minimax"
        bot_noir_mm.algo = "minimax"
        if partie_ab.trait:
            assert bot_blanc_mm.jouer_coup(partie_ab) == bot_blanc_ab.jouer_coup(partie_ab)
            print(bot_blanc_mm.jouer_coup(partie_ab) == bot_blanc_ab.jouer_coup(partie_ab))
        else : 
            assert bot_noir_mm.jouer_coup(partie_ab) == bot_noir_ab.jouer_coup(partie_ab)
            print(bot_noir_mm.jouer_coup(partie_ab) == bot_noir_ab.jouer_coup(partie_ab))
            

    
    
    
#test différence de temps minimax alphabeta, différentes profondeurs
def test_durée_1():
    plateaux = ["Sauvegarde_Test_IA\\Plateau_base","Sauvegarde_Test_IA\\suicide"]
    rapports = []
    for plateau in plateaux:
        partie_ab,bot_blanc_ab,bot_noir_ab = initialiser_plateau_bots(plateau,1,1)
        partie_mm,bot_blanc_mm,bot_noir_mm= initialiser_plateau_bots(plateau,1,1)
        bot_blanc_mm.algo = "minimax"
        bot_noir_mm.algo = "minimax"
        if partie_ab.trait:
            debut = time.time()
            bot_blanc_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_blanc_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
        else:
            debut = time.time()
            bot_noir_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_noir_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
    print("moyenne profondeur 1 : "+str(round(average(rapports),3)))
        
def test_durée_2():
    plateaux = ["Sauvegarde_Test_IA\\Plateau_base","Sauvegarde_Test_IA\\suicide"]
    rapports = []
    for plateau in plateaux:
        partie_ab,bot_blanc_ab,bot_noir_ab = initialiser_plateau_bots(plateau,2,2)
        partie_mm,bot_blanc_mm,bot_noir_mm= initialiser_plateau_bots(plateau,2,2)
        bot_blanc_mm.algo = "minimax"
        bot_noir_mm.algo = "minimax"
        if partie_ab.trait:
            debut = time.time()
            bot_blanc_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_blanc_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
        else:
            debut = time.time()
            bot_noir_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_noir_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
    print("moyenne profondeur 2 : "+str(round(average(rapports),3)))     
    
   
def test_durée_3():
    plateaux = ["Sauvegarde_Test_IA\\Plateau_base","Sauvegarde_Test_IA\\suicide"]
    rapports = []
    for plateau in plateaux:
        partie_ab,bot_blanc_ab,bot_noir_ab = initialiser_plateau_bots(plateau,3,3)
        partie_mm,bot_blanc_mm,bot_noir_mm= initialiser_plateau_bots(plateau,3,3)
        bot_blanc_mm.algo = "minimax"
        bot_noir_mm.algo = "minimax"
        if partie_ab.trait:
            debut = time.time()
            bot_blanc_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_blanc_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
        else:
            debut = time.time()
            bot_noir_mm.jouer_coup(partie_ab)
            fin_mm = time.time()
            bot_noir_ab.jouer_coup(partie_ab)
            rapport = (fin_mm-debut)/(time.time()-fin_mm)
            print("alphabeta est "+str(round(rapport,3))+" plus rapide que minimax")
            rapports.append(rapport)
    print("moyenne profondeur 3 : "+str(round(average(rapports),3)))
        


