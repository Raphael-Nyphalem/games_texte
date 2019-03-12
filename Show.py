import Interface
import File
import sys
import os


def Background():
    bg=File.OPEN_MENU("menu")
    bg_split = Split(bg)
    show(bg_split,0,0)
    return()

def Split(chaine):
    bg = {"map":[]}
    listeLignes = chaine.splitlines()
    for line in listeLignes:
        listeChar=list(line)
        bg["map"].append(listeChar)
    return(bg)

def Choise(show, PLAYER):
    if show == "Menu":
        Interface.menu(PLAYER)
    elif show == "Combat":
        print "tes"
    else:
        print"dd"
    return()

def show(bg,x,y) :

	#couleur fond
	sys.stdout.write("\033[40m")
	#couleur white
	sys.stdout.write("\033[37m")

	#goto
	for yp in range(y,len(bg["map"])):
		for xp in range(x,len(bg["map"][yp])):
			s="\033["+str(yp+1)+";"+str(xp+1)+"H"
			sys.stdout.write(s)
			#affiche
			sys.stdout.write(bg["map"][yp][xp])
