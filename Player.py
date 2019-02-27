#Creation joueur

Assassin   = {"Classes":"Assassin"  ,"attaque":[],"armes":[],"armure":[]}
Barde      = {"Classes":"Barde"     ,"attaque":[],"armes":[],"armure":[]}
Chevalier  = {"Classes":"Chevalier" ,"attaque":[],"armes":[],"armure":[]}
Druide     = {"Classes":"Druide"    ,"attaque":[],"armes":[],"armure":[]}
Enchanteur = {"Classes":"Enchanteur","attaque":[],"armes":[],"armure":[]}
Fantasin   = {"Classes":"Fantasin"  ,"attaque":[],"armes":[],"armure":[]}

def ADD_PLAYER(PLAYER):

    def input_class(choise_class):
        Classe_jouable = ["A","a","B","b","C","c","D","d","E","e","F","f"] #possibliliter de de rajouter des mots chef pour la demande de classe
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
