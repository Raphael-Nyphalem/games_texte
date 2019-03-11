#Obsolet a changer par une vrai interface en if elif

import os
import sys
import Player
import File

def clear():
    #clear fenetre
    os.system('cls' if os.name=='nt' else 'clear')
    return()

def menu(PLAYER):
    print(
    "Create new player: C\n"+
    "List of player: L\n"+
    "Save: S\n"+
    "Exit Game: E\n"
    )
    choise_menu = raw_input("Choise: ")
    #cree un joueur
    if choise_menu == 'C':
        PLAYER= Player.ADD_PLAYER(PLAYER)

    #affiche la liste des joueur
    elif choise_menu == "L":
        clear()
        i =0
        while i != len(PLAYER):
            Playeurnb = "Player_" + str(i)
            print str(PLAYER[Playeurnb]["name"]) +" de classe "+ str(PLAYER[Playeurnb]["classe"]["Classes"]) +" ayans pour niveau "+ str(PLAYER[Playeurnb]["lv"])
            i+=1
        raw_input()
    #sauvegarde
    elif choise_menu == "S":
        File.Save(PLAYER)
        clear()

    #ferme le jeu
    elif choise_menu == "E":
        clear()
        sys.exit()

    #commende non pris en compt
    else:
        clear()
        print("\nNous n'avons pas compris\n")
        PLAYER=menu(PLAYER)
    clear()
    return(PLAYER)

def Creation_playeur():
    return()
