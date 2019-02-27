import math
import os
import sys
import json

import Game_Play
import Player
import File
import Interface


PLAYER= {}

#Classes et aller voir https://www.dol-celeb.com/autres/classes/
#pour plus d'idee


def start():

    PLAYER = File.OPEN_FILE("save/save_player.txt")
    return(PLAYER)






"""
_____________________________________________________________
MAIN
"""
PLAYER = start()
i=1
while i==1:
    Interface.clear()
    Interface.menu(PLAYER)

'''
_____________________________________________________________
TEST
'''

"""
a=0
PLAYER= ADD_PLAYER(PLAYER)

print(PLAYEUR[a]["lv"],PLAYEUR[a]["xp"])
PLAYEUR[a] = XP(PLAYEUR[a],XP_GAIN())
print(PLAYEUR[a]["lv"],PLAYEUR[a]["xp"])


nb=len(PLAYER)
print nb
print PLAYER
"""
