import File

srt_class = ["Assassin","Barde","Chevalier"]

def Open_Class(classename):
    #"classname" est le nom de la classe que vous appeler
    #retoune la classe
    file_classe = File.OPEN_FILE("Class/"+classname+"/classe.txt")
    return(file_classe)

def Open_Attaques(classname):
    #"classname" est le nom de la classe que vous appeler
    #retoune les attaque de la classe
    file_attaque = File.OPEN_FILE("Class/"+classname+"/attaque.txt")
    return(file_attaque)

def Open_Descrition(classname):
    #"classname" est le nom de la classe que vous appeler
    #retoune les attaque de la description
    file_descrip = File.OPEN_FILE("Class/"+classname+"/description.txt")
    return(file_descrip)
