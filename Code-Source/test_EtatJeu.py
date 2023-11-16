import pytest
import coverage
import os
from EtatJeu import * 


def init_partie_test(nom_test):
    """Fonction qui initialise une partie à partir d'un plateau de test donné

    Args:
        nom_test (str): nom du fichier sauvegarde de test

    Returns:
        EtatJeu: L'état de la partie
    """
    chemin_fichier = os.path.join("Sauvegarde_Test_EtatJeu", nom_test)
    partie=EtatJeu(sauvegarde=chemin_fichier)
    print(partie)
    return partie


def test_pat():
    partie=init_partie_test("pat_1")
    assert partie.nulle()
    partie=init_partie_test("pat_2")
    partie.pieces[1][0].odometre=40
    assert partie.nulle()
    
def test_echec():
    partie=init_partie_test("avec_echec")
    assert partie.echec()
    partie=init_partie_test("sans_echec")
    assert not partie.echec()

def test_mat():
    partie=init_partie_test("avec_mat")
    assert partie.echec_et_mat()
    partie=init_partie_test("sans_mat")
    assert not partie.echec_et_mat()
    
#Test valeur:
def test_valeur():
    #Test de situation finale
    partie=init_partie_test("avec_mat")
    assert partie.calcul_valeur()==-1000
    partie=init_partie_test("pat_1")
    assert partie.calcul_valeur()==0
    #Test centre et sous centre
    partie=init_partie_test("controle_centre_et_ss_centre")
    assert partie.calcul_valeur()==0.4
    #Test pions allignés
    partie=init_partie_test("pions_allignes")
    assert partie.calcul_valeur()==-0.1
<<<<<<< HEAD

def test_promotion():
    partie=init_partie_test("promotion")
    partie.deplacer_piece((7,6),(7,7))
    for piece in partie.pieces[not partie.trait]:
        assert not isinstance(piece, Pion)
    assert isinstance(partie.plateau[(7,7)], Dame)
=======
>>>>>>> 261a4baf7ac7652a9b5d225f5b959bec934475b7
