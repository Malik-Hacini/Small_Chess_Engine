import pytest
import os

from joueurs import*
from EtatJeu import*
from piece import*


def init_partie_test(nom_test):
    """Fonction qui initialise une partie à partir d'un plateau de test donné

    Args:
        nom_test (str): nom du fichier sauvegarde de test

    Returns:
        EtatJeu: L'état de la partie
    """
    chemin_fichier = os.path.join("Sauvegarde_Test_Piece", nom_test)
    partie=EtatJeu(sauvegarde=chemin_fichier)
    print(partie)
    return partie

#déplacement des pièces
def test_deplacement_pion():
    partie=init_partie_test("test_deplacement_pion")
    partie.pieces[1][1].premier_coup=False
    assert partie.pieces[1][0].coups_possibles(partie)==[(3, 4), (4, 4)]
    assert partie.pieces[1][1].coups_possibles(partie)==[]
    assert partie.pieces[1][2].coups_possibles(partie)==[(1, 2), (1, 3)]

def test_deplacement_fou():
    partie=init_partie_test("test_deplacement_fou")
    assert partie.pieces[1][0].coups_possibles(partie)==[(5,5),(6,6),(7,7),(5,3),(3,3),(2,2),(1,1),(3,5),(2,6),(1,7)]
            
def test_deplacement_tour():
    partie=init_partie_test("test_deplacement_tour")
    assert partie.pieces[0][1].coups_possibles(partie)==[(5, 4), (6, 4), (7, 4), (4, 5), (3, 4), (2, 4), (1, 4), (4, 3), (4, 2), (4, 1)]


def test_deplacement_reine():
    partie=init_partie_test("test_deplacement_reine")
    assert partie.pieces[0][0].coups_possibles(partie)==[(5, 5), (6, 6), (5, 3), (3, 3), (2, 2), (1, 1), (0, 0), (3, 5), (2, 6), (1, 7), (5, 4), (6, 4), (7, 4), (4, 5), (4, 6), (4, 7), (3, 4), (2, 4), (4, 3)]

def test_deplacement_cavalier():   
    partie=init_partie_test("test_deplacement_cavalier")
    assert partie.pieces[1][1].coups_possibles(partie)==[(5, 5), (3, 5), (2, 4), (2, 2), (3, 1), (5, 1), (6, 2)]
    
def test_coups_legaux():
    partie=init_partie_test("test_coups_legaux")
    assert partie.pieces[1][0].coups_possibles(partie)==[(5, 3), (3, 3), (2, 2), (2, 0), (6, 0), (6, 2)]
    assert partie.pieces[1][0].coups_legaux(partie)==[]