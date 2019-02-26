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


def ADD_PLAYER(PLAYER):
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
    Player["classe"]= input('" A": Assassin \n "B": Barde \n "C": Chevalier \n "D":Druide \n "E": Enchanteur \n choisissais votre classe: ')
    Playeurnb = "Player_" + str(nb)
    print Playeurnb
    PLAYER[Playeurnb]= Player
    print PLAYER[Playeurnb]
    return(PLAYER)

def OPEN_FILE(filename):
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)

def SAVE_FILE(save,filename):
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

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


def Save(PLAYER):
    def Save_player(PLAYER):
        a=PLAYER
        SAVE_FILE(a,"save/save_player.txt")
        return()
    def Save_game():
        return()
    Save_player(PLAYER)

    return()

"""
----------------------------------------------------------
"""
def clear():
    #clear fenetre
    return()

def menu(PLAYER):
    clear()
    print(
    "Create new player: C\n"+
    "Save: S\n"+
    "Exit Game: E"
    )
    choise_menu = raw_input(": ")
    if choise_menu == 'C':
        PLAYER= ADD_PLAYER(PLAYER)
    elif choise_menu == "S":
        Save(PLAYER)
    elif choise_menu == "E":
        sys.exit()

    else:
        clear()
        print("Nous n'avons pas compris")
        menu()
    clear()
    return(PLAYER)


"""
_____________________________________________________________
MAIN
"""
PLAYER = start()
print PLAYER
i=1
while i==1:
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
