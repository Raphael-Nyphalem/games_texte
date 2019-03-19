import json
import sys
import os

#json
def OPEN_FILE(filename):
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)

def SAVE_FILE(save,filename):
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

#XML
def SAVE_FILE_XML(save,filename):
    myFile=open(filename,"w")
    myFile.write(save)
    myFile.close()
    return()

def OPEN_FILE_XML(filename):
    myFile=open(filename,"r")
    txt=myFile.read()
    myFile.close()
    return(txt)

def SPLIT(doc,spliter):
    #permet de coupee un txt pour le transformer en liste
    #doc = srt a split
    #spliter type str est le mots/ simbole / phrase ou le txt doit etre coupe
    doc_split=doc.split(spliter))
    return(doc_split)

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


#simplification
#menu
def OPEN_MENU(filename):
    chaine=OPEN_FILE_XML("Ressources/Background/Menu/"+filename+".txt")
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
