from numpy import average
import pytest
from joueurs import*
from EtatJeu import*
from piece import*

def initialiser_plateau_bots(partie,profondeur_blanc = 2,profondeur_noir = 2):
    bot1,bot2 = IA("Joueur1",True,profondeur_blanc),IA("Joueur2",False,profondeur_noir)
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
    
    

#test si minimax et alphabeta jouent le meme coup (profondeur 2)
def test_alphabeta():
    plateaux = ["Plateau_base","suicide"]
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
            
test_alphabeta()     
    
    
    
#test différence de temps minimax alphabeta, différentes profondeurs
def test_durée_1():
    plateaux = ["Plateau_base","suicide"]
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
    plateaux = ["Plateau_base","suicide"]
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
    plateaux = ["Plateau_base","suicide"]
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
        
test_durée_1()
test_durée_2()
test_durée_3()

#test elo profondeur 1 2 et 3


#raouter un cache

#faire un tableau plateau : profondeur : coup reccomandé

