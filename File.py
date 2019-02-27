import json
import sys
import os


def OPEN_FILE(filename):
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)

def SAVE_FILE(save,filename):
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

def Save(PLAYER):
    def Save_player(PLAYER):
        a=PLAYER
        SAVE_FILE(a,"save/save_player.txt")
        return()
    def Save_game():
        return()

    Save_player(PLAYER)
    raw_input("save complit")
    return()
