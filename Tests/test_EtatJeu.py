import pytest
from EtatJeu import *

def test_sauvegarde():
    #on va initialiser un plateau sans jouer de coups, le sauvegarder, puis le comparer au plateau de base
    bot1,bot2 = Joueur("Joueur1","True"),Joueur("Joueur2","False")
    Jeu = EtatJeu(bot1,bot2)
    Jeu.sauvegarder("sauvegarde_de_test")
    
    fichier = open("sauvegarde_de_test.txt", 'r')
    sauv1 = fichier.read()
    fichier.close()
    
    fichier = open("Plateau_base.txt", 'r')
    base = fichier.read()
    fichier.close()
    
    assert base == sauv1
    
    
    
    
    #Maintenant on va jouer un coup, puis sauvegarder la partie, vérifier que le coups a bien été enregistré et que le tour est au joueur Noir.
    Jeu.plateau[(0,1)].coord=(0,2)
    Jeu.plateau[(0,2)] = Jeu.plateau.pop((0,1))
    Jeu.trait = not Jeu.trait
    print(Jeu.trait)
    
    #sauvegarde dans le fichier de test
    Jeu.sauvegarder("sauvegarde_de_test")
    #lecture du fichier sauvegardé
    fichier = open("sauvegarde_de_test.txt", 'r')
    sauv2 = fichier.read()
    fichier.close()
    
    #vérification
    
    assert sauv2.split("\n")[2].split(": ")[1] == "noirs"