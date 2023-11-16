from joueurs import*
from EtatJeu import*
import sys
import os
import time

def conv_date(date:str)->str:
    """Convertit une date au format "AAAAMMJJ-HMS en texte plus clair.

    Args:
        date (str): date à convertir

    Returns:
        str: date au format JJ-MM-AAAA H:M
    """
    annee=date[:4]
    mois=date[4:6]
    jour=date[6:8]
    heure=date[9:11]
    min=date[11:13]
    
    return jour + "/" + mois + "/" + annee + " à " + heure + ":" + min
    
    
def partie(joueur1: Joueur,joueur2: Joueur):
    """Joue une partie d'échecs. 

    Args:
        joueur1 (Joueur): Le joueur 1. Peut être humain ou IA     
        joueur2 (Joueur): Le joueur 2. Peut être humain ou IA 
    """
    
    save=None
    while save not in ("O","N"):
        
        save=input("Voulez vous charger une sauvegarde ? (O/N) \n")
    
    
    #On affiche les sauvegardes disponibles à l'utilisateur, et on lui en fait choisir une. On gère les erreurs possibles.
    if save=="O":
        liste_fichiers=[fichier for fichier in os.listdir("./sauvegardes") if os.path.splitext(fichier)[-1].lower()==".fen"]
        liste_fichiers.remove("Plateau_base.fen")
        if liste_fichiers==[]:
            start=input("""Aucune sauvegarde n'est disponible. 
Appuyez sur Entrée pour démarrer une nouvelle partie.""")
            nom_save="Plateau_base.fen"
        else:
            print("Voici les sauvegardes disponibles: ")
            for index,fichier in enumerate(liste_fichiers):
                    print(index+1,".Sauvegarde du " + conv_date(fichier[5:-4]))
            fichier_valide=False
            while not fichier_valide:
                    num_save=input(f"Choisissez une sauvegarde (1-{len(liste_fichiers)}) \n")
                    if num_save.isdigit():
                        if int(num_save)-1 in list(range(len(liste_fichiers))):
                            nom_save=liste_fichiers[int(num_save) - 1]
                            fichier_valide=True
                            continue
                    print("Fichier introuvable ou invalide.")       
        partie=EtatJeu(nom_save)
    
    else:
        partie= EtatJeu()        
    
    print("Bonne partie ! A tout moment, entrez 'save' pour sauvegarder et quitter, et 'nulle' pour voter pour la nulle.")
        
    joueurs=[joueur2,joueur1]


    print(partie)
    nulle_votee=False
    draw_votes=0
    while partie.gagnant() is None and not partie.nulle() and not nulle_votee:

        
        #Si le joueur précédent a voté nulle :
        if draw_votes==1:
            vote=0
            while vote not in ("O","N"):
                vote=input(f"{joueurs[int(partie.trait)].nom}, acceptez vous la nulle ? (O/N) \n")
            
            if vote=="O": 
                nulle_votee=True 
                partie.trait = not partie.trait #On change le tour
                continue
            else: print("Nulle refusée.")   
        
        #On demande quelle pièce bouger au joueur (il peut écrire nulle ou save)
        deplacement_valide=False
        while not deplacement_valide:
            deplacement=joueurs[int(partie.trait)].jouer_coup(partie)
            if deplacement=="nulle" and isinstance(joueurs[not partie.trait],IA):
                print("Vous ne pouvez pas voter nulle contre une IA. ")
            else:
                deplacement_valide=True

        #Cas particuliers (vote de nulle ou save)
        if deplacement=="nulle":
                    draw_votes=1
                    partie.trait = not partie.trait #On change le tour
                    continue
        else:
            draw_votes=0
        if deplacement=="save" :
            date=time.strftime("%Y%m%d-%H%M%S")
            partie.sauvegarder(f"save_{date}")
            print("Sauvegarde effectuée.") 
            return "N"
        
        partie.deplacer_piece(deplacement[0],deplacement[1])
        
        print(partie)
        if partie.echec(): print("Votre roi est en échec.")
    
    #On affiche le résultat de la partie.
    if partie.nulle() or nulle_votee: print("Partie Nulle.")
    else: print(f"{joueurs[partie.gagnant()].nom} a gagné la partie ! \n")
    
    
    
def main():
    """Le jeu d'échec dans son intégralité. Initialise une partie, 
    la fait jouer et répète tant que l'utilisateur veut rejouer."""
    
    
    print("""
███████  ██████ ██   ██ ███████  ██████ ███████ 
██      ██      ██   ██ ██      ██      ██      
█████   ██      ███████ █████   ██      ███████ 
██      ██      ██   ██ ██      ██           ██ 
███████  ██████ ██   ██ ███████  ██████ ███████



                     Par
        ===============================
        ||       Timothé Boyer       ||
        ||       Basile Mouret       ||
        ||       Malik Hacini        ||
        ===============================
        
        
            Bienvenue aux échecs ! 
        """)                                        
          
    while True:
        
        
        replay=None
        joueurs = []
        for i in (1,0):
            type_joueur=None
            if i==1: couleur="blanc"
            else: couleur="noir"
            
            while type_joueur not in ("1","2"):
                type_joueur=input(f"De quel type est le Joueur {couleur} ? \n 1: Humain \n 2: IA \n")
            
                
            if type_joueur=="1":
                nom=input(f"Quel est le nom du Joueur {couleur} ? \n")
                joueurs.append(Humain(nom,i))   
            else:
                niveau=5
                while niveau not in ("0","1","2","3"):
                    niveau=input(f"""Quel est le niveau de l'IA {couleur} souhaité ? 
0. Novice : Joue aléatoirement.
1. Débutant
2. Intérmédiaire (700 elo)
3. Avancé (800 elo) \n""")
                nom=f"IA {couleur}"
                joueurs.append(IA(nom, i, int(niveau)))

        replay=partie(joueurs[0],joueurs[1])
            
        while replay not in ("O","N"):
            replay=input("Voulez vous rejouer ? (O/N) \n")
            
        if replay=="N":
            print("Merci d'avoir joué ! ")
            sys.exit()
    
    
    
        
if __name__== "__main__":
    main()