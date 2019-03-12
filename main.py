import math
import os
import sys
import json
import time
import select
import tty
import termios


import Game_Play
import Player
import File
import Interface
import Show


PLAYER= {}
dt = 0.02
show ="Menu"
#Classes et aller voir https://www.dol-celeb.com/autres/classes/
#pour plus d'idee


def start():

    PLAYER = File.OPEN_FILE("save/save_player.txt")
    tty.setcbreak(sys.stdin.fileno())
    Show.Background()
    return(PLAYER)


def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def loop_time():
    global PLAYER, dt, show
    c=0
    t=time.time()
    while (time.time() - t)<= dt:#zone calcul tmp reel
        #recuperation clavier
        if isData():
            c= sys.stdin.read(1)
        #action utilisant l'input clavier
        if c != 0:
            print "c!=0"
        c=0
    return()


"""
_____________________________________________________________
MAIN
"""

PLAYER = start()
Show.Choise(show, PLAYER)
while True:
    loop_time()
    Show.Choise(show, PLAYER)
