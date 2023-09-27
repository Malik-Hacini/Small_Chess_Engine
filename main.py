from joueurs import*
from Partie import*
import sys

def jouer_une_partie(joueur1,joueur2):
    """Joue une partie d'échecs. 

    Args:
        joueur1 (_type_): Le joueur 1. Peut être humain ou IA
        joueur2 (_type_): Le joueur 2. Peut être humain ou IA 
    """
    joueurs=[joueur1,joueur2]
    
    save=None
    while save not in ("O","N"):
        
        save=input("Voulez vous charger une sauvegarde ? (O/N) \n")
    
    if save=="O":
        loop=True
        while loop:
            try :
                nom_save=input("Nom du fichier de sauvegarde : \n")
                save_file=open(f"{nom_save}.txt")
                print("Sauvegarde chargée \n")
                loop=False
            except:
                print("Fichier introuvable \n")
                
        partie = Partie(joueur1,joueur2,save_file)
    
    else:
        partie= Partie(joueur1,joueur2)        
    
        
    tour = True
    draw= False
    while partie.gagnant() is None and not draw:
        
        print(partie)
        partie.deplacer_piece(joueurs[tour].jouer_coup(partie))
        
        tour = not tour
    
    print(f"{partie.gagnant().nom} a gagné la partie ! \n")
    
    
    
def main():
    """Le jeu d'échec dans son intégralité. Initialise une partie, 
    la joue et répète tant que l'utilisateur veut rejouer."""
    
    while True:
        for i in range(1,3):
            type_joueur=None
            while type_joueur not in ("1","2"):
                type_joueur=input(f"De quel type est le Joueur {i} ? \n 1: Humain \n 2: IA \n")
            
                
            if type_joueur=="1": nom=input(f"Quel est le nom du Joueur {i} ? \n")
            else: nom==f"IA {i}"
            
            if type_joueur=="1":
                if i==1:
                    joueur1=Humain(nom, 1)
                else:
                    joueur2=Humain(nom,0)
            else:
                if i==1:
                    joueur1=IA(nom, 1)
                else:
                    joueur2=IA(nom,0)

        jouer_une_partie(joueur1,joueur2)
            
        replay=None
        while replay not in ("O","N"):
            replay=input("Voulez vous rejouer ? (O/N) \n")
            
        if replay=="N":
            print("Merci d'avoir joué ! ")
            sys.exit()
    
    
        
if __name__== "__main__":
    main()