import pytest
import os

from joueurs import*
from EtatJeu import*
from piece import*


def init_partie_test(nom_test):
    chemin_fichier = os.path.join("Sauvegarde_Test_Piece", nom_test)
    partie=EtatJeu(sauvegarde=chemin_fichier)
    print(partie)
    return partie

#déplacement des pièces
def test_deplacement_pion():
    partie=init_partie_test("test_deplacement_pion")
    partie.pieces[1][1].premier_coup=False
    assert partie.pieces[1][0].coups_possibles(partie)==[(2,2),(2,3)]
    assert partie.pieces[1][1].coups_possibles(partie)==[(4,3),(5,3)]
    assert partie.pieces[1][2].coups_possibles(partie)==[]

def test_deplacement_fou():
    partie=init_partie_test("test_deplacement_fou")
    assert partie.pieces[1][0].coups_possibles(partie)==[(5,5),(6,6),(7,7),(5,3),(3,3),(2,2),(1,1),(3,5),(2,6),(1,7)]
            
def test_deplacement_tour():
    partie=init_partie_test("test_deplacement_tour")
    assert partie.pieces[1][0].coups_possibles(partie)==[(5,3),(4,4),(4,5),(4,6),(3,3),(2,3),(1,3),(0,3),(4,2),(4,1),(4,0)]


def test_deplacement_reine():
    partie=init_partie_test("test_deplacement_reine")
    assert partie.pieces[1][0].coups_possibles(partie)==[(5, 4), (6, 5), (7, 6), (5, 2), (6, 1), (7, 0), (3, 2), (3, 4), (2, 5), (5, 3), (4, 4), (4, 5), (4, 6), (4, 7), (3, 3), (2, 3), (1, 3), (0, 3), (4, 2), (4, 1)]