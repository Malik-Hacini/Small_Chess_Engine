import pytest
import os

from joueurs import*
from EtatJeu import*
from piece import*

def init_partie_test(nom_test):
    j1=Joueur("J1", True)
    j2=Joueur("J2", False)
    chemin_fichier = os.path.join("Sauvegarde_Test_Valeur", nom_test)
    partie=EtatJeu(j1,j2, chemin_fichier)
    print(partie)
    return  j1, j2, partie

def test_valeur_initiale():
    j1, j2, etat=init_partie_test("test_valeur_initiale")
    assert etat.valeur==0

def test_valeur_avantage_blanc():
    j1, j2, etat=init_partie_test("test_valeur_initiale")
    assert etat.valeur==10