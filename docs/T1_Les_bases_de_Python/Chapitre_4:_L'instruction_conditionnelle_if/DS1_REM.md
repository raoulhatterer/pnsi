!!! example "{{ exercice() }}"
    === "Énoncé"
        On calcule l'IMC (Indice de Masse Corporelle) par la formule $I = M / T^2$ où M est la masse (en kg) d'une personne et T sa taille (en m).
        Selon la classification de l'OMS, une personne est en état de maigreur si son IMC est inférieur à 18 et en surpoids si son IMC est supérieur à 25. 

        1. Écrire un programme qui demande la masse et la taille d'une personne, calcule son IMC et annonce si la personne est en état de maigreur.
        2. Modifier ensuite le programme pour qu'il annonce si la personne est en état de maigreur, en surpoids ou bien si son IMC est normal.
    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        masse = float(input('Quelle est votre masse (en kg) ? '))
        taille = float(input('Quelle est votre taille (en m) ? '))

        IMC = masse / taille**2
        print('votre IMC vaut :', IMC)
        if IMC < 18:
            print('vous êtes en état de maigreur')
        elif IMC < 25:
            print('votre corpulence est dans la normale')
        else:
            print('vous êtes en surpoids')
        ```
        "
        ) }} 
