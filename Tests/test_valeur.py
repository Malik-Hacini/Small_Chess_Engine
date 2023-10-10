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
    assert partie.valeur==0
    
def test_valeur_avantage_blancs():
    partie=init_partie_test("test_avantage_blancs_Reine")
    partie.calcul_valeur
    assert partie.valeur==10