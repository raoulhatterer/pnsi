from serveur import get_template, render, OK, Redirect, pageDynamique, lancerServeur





def traitement1(url, vars):
    """Traitement du formulaire1"""
    print("Le formulaire à envoyé:",vars)
    return Redirect('/formulaire1.html')

pageDynamique('/traitement_formulaire1', traitement1)


# Lancer le serveur
lancerServeur()
