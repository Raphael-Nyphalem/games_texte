import File
import Class
#Creation joueur

def ADD_PLAYER(PLAYER):

    def input_class(choise_class):
        Classe_jouable = ["A","a","B","b","C","c","D","d","E","e","F","f"] #possibliliter de de rajouter des mots chef pour la demande de classe
        i=1
        while i==1:
            i=0
            choise_class= raw_input(' "A": Assassin \n "B": Barde \n "C": Chevalier \n "D":Druide \n "E": Enchanteur \n choisissais votre classe: ')
            if choise_class not in Classe_jouable:
                choise_class= input_class(choise_class)
            else:
                if choise_class == 'A' or "a":
                    choise_class = "Assassin"
                elif choise_class == 'B' or "b":
                    choise_class = "Barde"
                elif choise_class == 'C' or "c":
                    choise_class = "Chevalier"
                elif choise_class == 'D' or "d":
                    choise_class = "Druide"
                elif choise_class == 'E' or "e":
                    choise_class = "Enchanteur"
                elif choise_class == 'F' or "f":
                    choise_class = "Fantassin"
                else:
                    i=1
            return(choise_class)

    #Ajouter un player
    nb = len(PLAYER)
    Player = {
        "player":nb,        #int
        "name": None,       #srt
        "lv":1 ,            #int
        "xp": 0,            #int
        "classe":None,      #str
        "element":None,     #dic
        "inventory" : None, #dic
        }

    Player["name"] = raw_input("Name: ")
    #chois de la classe
    Player["classe"] = input_class("")
    #ajout player
    Playeurnb = "Player_" + str(nb)
    PLAYER[Playeurnb]= Player
    return(PLAYER)
