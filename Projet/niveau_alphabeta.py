import pytest
from joueurs import*
from EtatJeu import*
from piece import*



def partie_IA_vs_Stockfish(niveau_IA, elo_Stockfish, plateau="plateau_base"):
    bot1,bot2 = IA("negalphabetamax",True,niveau_IA),Stockfish("Stockfish",False,elo_Stockfish)
    partie = EtatJeu(plateau)
    
    
    joueurs=[bot2,bot1]
    draw= False
    while partie.gagnant() is None and not draw:
        coord_i,coord_f=joueurs[int(partie.trait)].jouer_coup(partie)
        #print(f"{conv_int(coord_i)}-{conv_int(coord_f)}",end=", ")
        partie.deplacer_piece(coord_i,coord_f)
        
    print(f"{joueurs[partie.gagnant()].nom} a gagné la partie ! \n")
    return partie.gagnant()


def déterminer_nv(niveau_IA):
    stockfishwin = False
    elos=0
    while not stockfishwin:
        elos+=1
        stockfishwin = not partie_IA_vs_Stockfish(niveau_IA,elos)
        print(stockfishwin)
    print(f"un bot de niveau{niveau_IA} perd contre stockfish {elos} elo")


if __name__=="__main__":
    déterminer_nv(3)