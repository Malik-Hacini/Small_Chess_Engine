import pytest
import os

from joueurs import*
from EtatJeu import*
from piece import*

def init_partie_test(nom_test):
    chemin_fichier = os.path.join("Sauvegarde_Test_Valeur", nom_test)
    partie=EtatJeu(sauvegarde=chemin_fichier)
    print(partie)
    return partie

def test_valeur_initiale():
    partie=init_partie_test("test_valeur_initiale")
    partie=init_partie_test("test_valeur_initiale")
    partie.calcul_valeur_tim()
    assert partie.valeur==0
    
def test_valeur_avantage_materiel():
    #Avantage Blanc
    partie=init_partie_test("test_avantage_blancs_Reine")
    partie.calcul_valeur()
    assert partie.valeur==9
    partie=init_partie_test("test_avantage_blancs_Tour")
    partie.calcul_valeur()
    assert partie.valeur==5
    partie=init_partie_test("test_avantage_blancs_Fou")
    partie.calcul_valeur()
    assert partie.valeur==3
    partie=init_partie_test("test_avantage_blancs_Cavalier")
    partie.calcul_valeur()
    assert partie.valeur==3
    partie=init_partie_test("test_avantage_blancs_Pion")
    partie.calcul_valeur()
    assert partie.valeur==1
    
    #Avantage Noir
    