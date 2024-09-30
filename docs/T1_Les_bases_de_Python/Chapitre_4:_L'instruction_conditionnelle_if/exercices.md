# Exercices sur l'instruction conditionnelle `if` 

{{ initexo(0) }}

!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire un programme qui demande deux nombres et qui affiche le plus grand des deux.
    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        n1 = int(input('Premier nombre ?'))
        n2 = int(input('Deuxième nombre ?'))

        if n1 > n2:
            print('le nombre le plus grand est', n1)
        elif n2 > n1:
            print('le nombre le plus grand est', n2)
        else:
            print('les deux nombres sont égaux')

        ```
        "
        ) }}



!!! example "{{ exercice() }}"
    === "Énoncé"
        Exercice utilisant le module [ipythonblocks](https://www.carnets.info/jupyter/ipythonblocks/) ou le module p5 à réaliser sur Capytale.
        ![image](data/damier.png){: .center}
    === "Correction en p5"
        ```python linenums='1'
        from p5 import*
        
        def setup ():
            createCanvas(300,300)
            noLoop()
            
        def draw():
            background(0)
            cote = 30
            stroke(255)
            for x in range(10):
                for y in range(10):
                    if (x + y) % 2 == 0:
                        fill(0)
                    else :
                       fill(0, 255, 255)
                    rect(x * cote, y * cote, cote, cote)
        run()
        ```
    === "Correction en ipythonblocks"
        ```python linenums='1'
        from ipythonblocks import BlockGrid
        grille_D = BlockGrid(10, 10)
        for cellule in grille_D:
            if (cellule.row + cellule.col) % 2 == 1:
                cellule.set_colors(0, 255, 255)
        grille_D 
        ``` 


!!! example "{{ exercice() }}"
    === "Énoncé"
        Le jeu du FizzBuzz : il s'agit de compter à partir de 1 en remplaçant certains nombres par Fizz, Buzz ou Fizzbuzz :

        - si le nombre est divisible par 3, on ne le dit pas et on le remplace par Fizz.
        - si le nombre est divisible par 5, on ne le dit pas et on le remplace par Buzz.
        - si le nombre est divisible par 3 et par 5, on ne le dit pas et on le remplace par FizzBuzz.

        Écrire un code qui joue au FizzBuzz jusqu'à 50.

    === "Correction"
        {{ correction(True,
        "
        ```python linenums='1'
        for k in range(1,51):
            if k % 3 == 0 and k % 5 == 0:
                print('fizzbuzz')
            elif k % 3 == 0:
                print('fizz')
            elif k % 5 == 0:
                print('buzz')
            else:
                print(k)
        ```
        "
        ) }}


!!! example "{{ exercice() }}"
    === "Énoncé"
        Une année est déclarée bissextile (et compte donc 366 jours au lieu de 365) si elle est :

        - soit divisible par 400.
        - soit divisible par 4 mais pas divisible par 100.

        Écrire un code qui détermine si une année est bissextile ou non.

        *Explication : la Terre faisant le tour du Soleil en [un peu plus que 365 jours](https://fr.vikidia.org/wiki/R%C3%A9volution_de_la_Terre_autour_du_Soleil), on s'est dit qu'on allait rajouter un jour tous les 4 ans, mais c'était trop, alors on a enlevé un jour tous les 100 ans, mais c'était plus assez, alors on a rajouté un jour tous les 400 ans, ce qui donne une approximation convenable.*

    === "Correction"
        {{ correction(True,
        """
        ```python linenums='1'
        annee = 2021

        if annee % 400 == 0:
            print(annee, \"est bissextile\")
        elif annee % 4 == 0 and annee % 100 != 0:
            print(annee, \"est bissextile\")
        else:
            print(annee, \"n'est pas bissextile\")

        ```
        """
    


        
        ) }}
