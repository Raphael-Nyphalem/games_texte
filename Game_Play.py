



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
