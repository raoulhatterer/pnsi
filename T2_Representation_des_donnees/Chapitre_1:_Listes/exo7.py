texte = "cet texte est prodigieusement ennuyeux"

def rang(lettre):
    return(ord(lettre) - 97)

compt = [0]*26
for lettre in texte :
    if lettre != " " :
        compt[rang(lettre)] += 1
