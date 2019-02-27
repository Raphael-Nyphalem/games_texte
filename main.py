import math
import os
import sys
import json

PLAYER= {}

#Classes et aller voir https://www.dol-celeb.com/autres/classes/
#pour plus d'idee
Assassin   = {"Classes":"Assassin"  ,"attaque":[],"armes":[],"armure":[]}
Barde      = {"Classes":"Barde"     ,"attaque":[],"armes":[],"armure":[]}
Chevalier  = {"Classes":"Chevalier" ,"attaque":[],"armes":[],"armure":[]}
Druide     = {"Classes":"Druide"    ,"attaque":[],"armes":[],"armure":[]}
Enchanteur = {"Classes":"Enchanteur","attaque":[],"armes":[],"armure":[]}
Fantasin   = {"Classes":"Fantasin"  ,"attaque":[],"armes":[],"armure":[]}

def start():

    PLAYER = OPEN_FILE("save/save_player.txt")
    return(PLAYER)

#Creation joueur
def ADD_PLAYER(PLAYER):

    def input_class(choise_class):
        clear()
        Classe_jouable = ["A","a","B","b","C","c","D","d","E","e","F","f"]
        i=1
        while i==1:
            i=0
            choise_class= raw_input('" A": Assassin \n "B": Barde \n "C": Chevalier \n "D":Druide \n "E": Enchanteur \n choisissais votre classe: ')
            if choise_class not in Classe_jouable:
                choise_class= input_class(choise_class)
            else:
                if choise_class == 'A' or "a":
                    choise_class = A
                elif choise_class == 'B' or "b":
                    choise_class = B
                elif choise_class == 'C' or "c":
                    choise_class = C
                elif choise_class == 'D' or "d":
                    choise_class = D
                elif choise_class == 'E' or "e":
                    choise_class = E
                elif choise_class == 'F' or "f":
                    choise_class = F
                else:
                    i=1
            return(choise_class)

    clear()
    #Ajouter un player
    nb = len(PLAYER)
    A,B,C,D,E,F = Assassin,Barde,Chevalier,Druide,Enchanteur,Fantasin
    Player = {
        "player":nb,
        "name": None,
        "lv":1 ,
        "xp": 0,
        "classe":None,
        "element":None,
        "inventory" : None,
        }
    Player["name"] = raw_input("Name: ")
    #chois de la classe
    Player["classe"] = input_class("")
    #ajout player
    Playeurnb = "Player_" + str(nb)
    PLAYER[Playeurnb]= Player
    return(PLAYER)

#file
def OPEN_FILE(filename):
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)

def SAVE_FILE(save,filename):
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

# Saves
def Save(PLAYER):
    def Save_player(PLAYER):
        a=PLAYER
        SAVE_FILE(a,"save/save_player.txt")
        return()
    def Save_game():
        return()
    Save_player(PLAYER)
    b=raw_input("save complit")
    clear()
    return()


#Game play
def XP(player,gain):
    #Ajout xp a un player
    xp = playeur["xp"]
    lv = playeur["lv"]
    xpmax= lv * 10 + lv^2 #Calcul de l'xp
    xp = xp+gain
    if xp >= xpmax:
        playeur["xp"] = xp - xpmax
        playeur["lv"] =lv + 1
    return(playeur)



"""
----------------------------------------------------------
"""
#Clear Windows
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
        PLAYER= ADD_PLAYER(PLAYER)

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
        Save(PLAYER)

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


"""
_____________________________________________________________
MAIN
"""
PLAYER = start()
i=1
while i==1:
    clear()
    menu(PLAYER)

'''
_____________________________________________________________
TEST
'''


a=0
PLAYER= ADD_PLAYER(PLAYER)
"""
print(PLAYEUR[a]["lv"],PLAYEUR[a]["xp"])
PLAYEUR[a] = XP(PLAYEUR[a],XP_GAIN())
print(PLAYEUR[a]["lv"],PLAYEUR[a]["xp"])
"""

nb=len(PLAYER)
print nb
print PLAYER
