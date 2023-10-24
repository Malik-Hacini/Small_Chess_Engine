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
    partie.calcul_valeur()
    assert partie.valeur==0
    
def test_valeur_avantage_materiel():
    #Avantage Blanc
    partie=init_partie_test("test_avantage_blancs_Reine")
    partie.calcul_valeur()
    assert partie.valeur==8.95
    partie=init_partie_test("test_avantage_blancs_Tour")
    partie.calcul_valeur()
    assert partie.valeur==5
    partie=init_partie_test("test_avantage_blancs_Fou")
    partie.calcul_valeur()
    assert partie.valeur==2.95
    partie=init_partie_test("test_avantage_blancs_Cavalier")
    partie.calcul_valeur()
    assert partie.valeur==2.95
    partie=init_partie_test("test_avantage_blancs_Pion")
    partie.calcul_valeur()
    assert partie.valeur==0.8
    
    #Avantage Noir
    partie=init_partie_test("test_avantage_noirs_Reine")
    partie.calcul_valeur()
    assert partie.valeur==-8.95
    partie=init_partie_test("test_avantage_noirs_Tour")
    partie.calcul_valeur()
    assert partie.valeur==-5
    partie=init_partie_test("test_avantage_noirs_Fou")
    partie.calcul_valeur()
    assert partie.valeur==-2.95
    partie=init_partie_test("test_avantage_noirs_Cavalier")
    partie.calcul_valeur()
    assert partie.valeur==-2.95
    partie=init_partie_test("test_avantage_noirs_Pion")
    partie.calcul_valeur()
    assert partie.valeur==-0.8


def test_valeur_cases_controllees():
    partie=init_partie_test("test_valeur_cases_controllees_Tour")
    partie.calcul_valeur()
    assert partie.valeur==5.6
    partie=init_partie_test("test_valeur_cases_controllees_Fou")
    partie.calcul_valeur()
    assert partie.valeur==-3.35

def test_valeur_position():
    partie=init_partie_test("test_valeur_centre_blancs")
    partie.calcul_valeur()
    assert partie.valeur==1.6
    partie=init_partie_test("test_valeur_centre_noirs")
    partie.calcul_valeur()
    assert partie.valeur==-1.6
    partie=init_partie_test("test_valeur_sous_centre_blancs")
    partie.calcul_valeur()
    assert partie.valeur==1.2
    partie=init_partie_test("test_valeur_sous_centre_noirs")
    partie.calcul_valeur()
    assert partie.valeur==-1.2
    
def test_valeur_pions_doubles():
    partie=init_partie_test("test_pion_double_blancs")
    partie.calcul_valeur()
    assert partie.valeur==-0.05
