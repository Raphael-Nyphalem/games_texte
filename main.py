import math
import os
import sys


#Classes et aller voir https://www.dol-celeb.com/autres/classes/
#pour plus d'idee
Assassin   = {"Classes":"Assassin"  ,"attaque":[],"armes":[],"armure":[]}
Barde      = {"Classes":"Barde"     ,"attaque":[],"armes":[],"armure":[]}
Chevalier  = {"Classes":"Chevalier" ,"attaque":[],"armes":[],"armure":[]}
Druide     = {"Classes":"Druide"    ,"attaque":[],"armes":[],"armure":[]}
Enchanteur = {"Classes":"Enchanteur","attaque":[],"armes":[],"armure":[]}
Fantasin   = {"Classes":"Fantasin"  ,"attaque":[],"armes":[],"armure":[]}


PLAYER= {}
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
    PLAYER[Playeurnb]= Player
    print PLAYER[Playeurnb]
    return(PLAYER)


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

def XP_GAIN():
    xp = 50
    return xp

def Save():
    print("il n'y a pas de sauvegarde paussible pour le moment")
    def Save_player():
        return()
    def Save_game():
        return()
    return

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
        Save()
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
