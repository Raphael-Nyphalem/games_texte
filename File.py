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

def OPEN_MENU(filename):
    myfile = open("Ressources/Background/Menu/"+filename+".txt", "r")
    chaine=myfile.read()
    myfile.close()
    return(chaine)

#Class
def Open_Class(classename):
    #"classname" est le nom de la classe que vous appeler
    #retoune la classe
    file_classe = OPEN_FILE("Class/"+classname+"/classe.txt")
    return(file_classe)

def Open_Attaques(classname):
    #"classname" est le nom de la classe que vous appeler
    #retoune les attaque de la classe
    file_attaque = OPEN_FILE("Class/"+classname+"/attaque.txt")
    return(file_attaque)

def Open_Descrition(classname):
    #"classname" est le nom de la classe que vous appeler
    #retoune les attaque de la description
    file_descrip = OPEN_FILE("Class/"+classname+"/description.txt")
    return(file_descrip)
