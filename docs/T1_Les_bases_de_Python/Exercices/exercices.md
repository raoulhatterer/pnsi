# Je me teste

{{ initexo(0) }}

Quelques exercices très simples pour vérifier que vous maîtrisez un minimum les bases du langage python.

## Variables et Entrées/Sorties

!!! example "{{ exercice() }}"
    === "Énoncé"
         Écrire un programme qui demande son nom à l'utilisateur puis qui affiche sur la console "Bonjour" suivi du nom donné par l'utilisateur.
    === "Correction"
        Exercice 1
        
## Opérateurs arithmétiques

!!! example "{{ exercice() }}"
    === "Énoncé"
        Répondre aux questions suivantes à l'aide de l'interpréteur Python.
        Quel est le type du résultat de chacune des opérations suivantes :
        
        - division d'un entier par un entier à l'aide de l'opérateur `/`
        - division d'un entier par un entier à l'aide de l'opérateur `//`
        - opérateur  `%` entre deux entiers
        - opérateur  `%` entre un nombre à virgule (float) et un entier
    === "Correction"
        Exercice 2

## Branchements conditionnels

!!! example "{{ exercice() }}"
    === "Énoncé"
        À l'aide d'un programme, posez à l'utilisateur une devinette dont la réponse attendue soit une chaîne de caractères, et félicitez-le s'il a raison.
    === "Correction"
        Exercice 3
        
!!! example "{{ exercice() }}"
    === "Énoncé"
        À l'aide d'un programme, posez à l'utilisateur une devinette dont la réponse attendue soit une valeur numérique, et réprimandez-le s'il se trompe.
    === "Correction"
        Exercice 4


!!! example "{{ exercice() }}"
    === "Énoncé"
        À l'aide d'un programme, posez à l'utilisateur 3 questions différentes, en lui donnant 1 point par réponse exacte.
    === "Correction"
        Exercice 5

!!! example "{{ exercice() }}"
    === "Énoncé"
        À l'aide d'un programme, posez à l'utilisateur 3 questions différentes, en lui donnant 1 point par réponse exacte et en lui enlevant 1 point par réponse fausse
    === "Correction"
        Exercice 6

!!! example "{{ exercice() }}"
    === "Énoncé"
        Compléter le programme de l'exercice 5 pour qu'il affiche un commentaire différent pour chacune des valeurs du score final possibles (de 0 à 3)
    === "Correction"
        Exercice 7
        
!!! example "{{ exercice() }}"
    === "Énoncé"
        Calculateur postfixé. 
        Un calculateur postfixé reçoit les instructions de calcul dans l'ordre (opérande 1, opérande 2, opérateur).   
        Le programme ci-dessous est une ébauche de calculateur postfixé.
        ```python linenums="1"
        v1=float(input("première valeur: "))  # (1)
        v2=float(input("deuxième valeur: "))  # (2)
        op=input("opérateur: ")               # (3)
        if op=="+":                           # (4)
            print(v1+v2)                      # (5)
        ```
        
        1. Saisie du premier opérande                               
        2. Saisie du deuxième opérande                              
        3. Saisie de l'opérateur                                    
        4. Est-ce l'opérateur d'addition ?                          
        5. Si oui, l'addition est effectuée et le résultat affiché  
            
        Compléter le code pour qu'il puisse effectuer l'une des quatre opérations `+` , `-` , `*` , `/` (ou des sept opérations `+` , `-` , `*` , `/` , `//` , `%` , `**` pour les courageux) selon le choix de l'utilisateur, ou bien qu'il affiche "opérateur invalide" si 'op' ne désigne pas une de ces opérations.
    === "Correction"
        Exercice 8

## Boucle `while`
`
!!! example "{{ exercice() }}"
    === "Énoncé"
        Ce programme demande un mot à l'utilisateur, tant que la longueur du mot est inférieure à 5 :
        ```python linenums="1"
        mot='' #initialisation avec un mot de longueur inférieure à 5, pour que la boucle démarre
        while len(mot)<5:                                            # (1)
            mot=input("Ecrire un mot d'au moins 5 lettres : ")
        print("Enfin! Ce n'était pourtant pas si difficile ! "       # (2)
        ```

        1. Condition d'exécution de la boucle
        2. Le programme est sorti de la boucle, cela montre que l'utilisateur a donné un mot de plus de 5 lettres
    
        a. Écrire une variante de l'exemple ci-dessus, qui demande un mot à l'utilisateur jusqu'à ce que la longueur du mot soit exactement 5.  
        b. Écrire une variante de l'exemple qui demande un mot à l'utilisateur jusqu'à ce que la longueur du mot soit inférieure à 5.
    === "Correction"
        Exercice 9

!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire un programme affichant tous les multiples de 41 inférieurs à 1000
    === "Correction"
        Exercice 10

!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire un programme affichant les 25 premiers multiples de 11.
    === "Correction"
        Exercice 11

!!! example "{{ exercice() }}"
    === "Énoncé"
        La suite de Fibonacci est une suite d'entier dont chaque terme, à partir du rang 3, est la somme des deux termes précédents. Le premier terme vaut 0 et le second 1. Le troisième terme vaut donc 0+1=1, le quatrième 1+1=2, etc...

        Écrire un programme qui calcule et affiche tous les termes de la suite inférieurs à 1000.
    === "Correction"
        Exercice 12
        
!!! example "{{ exercice() }} (bilan)"
    === "Énoncé"
        Écrire un programme qui fasse deviner à l'utilisateur un nombre entier compris entre 100 et 200, en utilisant une boucle qui ne s'arrête que quand la bonne valeur a été trouvée. Pour chaque essai manqué, le programme donnera à l'utilisation des indications "trop petit" ou "trop grand" en fonction de la valeur qu'il aura donnée, à l'aide de branchements conditionnels.
    
        → Ne pas oublier que l'instruction input renvoie une chaîne de caractères  
        → Le nombre entier n à deviner peut être tiré au hasard en utilisant les instructions
        ```python linenums="1"
        import random
        n=random.randint(100,200)
        ```
        (il est conseillé de mettre d'abord le programme au point en utilisant un 'nombre à deviner' connu)

        → Une version plus élaborée du programme peut incorporer un compteur d'essais, et même limiter (à 8, par exemple) le nombre maximum d'essais accordés
    === "Correction"
        Exercice 13
        
## Boucle `for`
        
        
!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire une boucle `for` permettant d'afficher tous les chiffres impairs de 1 (inclus) à 15 (inclus)    
    === "Correction"
        Exercice 14
    
        
!!! example "{{ exercice() }}"
    === "Énoncé"
        Écrire une boucle `for` permettant d'afficher les 16 premières puissances de 2        
    === "Correction"
        Exercice 15

## Fonctions

!!! example "{{ exercice() }}"
    === "Énoncé"
        1. Écrire une fonction appelée `carre` attendant un seul paramètre, supposé être une valeur numérique, et affichant son carré. 
        2. Écrire l'appel de cette fonction pour la valeur 5.    
    === "Correction"
        Exercice 16
    
!!! example "{{ exercice() }}"
    === "Énoncé"
        Modifier la fonction `carre` de l'exercice précédent pour qu'au lieu d'*afficher* le carré du nombre passé en paramètre, elle *retourne* le carré du nombre.    
    === "Correction"
        Exercice 17
        
!!! example "{{ exercice() }}"
    === "Énoncé"
        1. Écrire une fonction appelée `est_pair`, attendant un seul paramètre supposé être une valeur numérique, et retournant `True` si le paramètre est un nombre pair, `False` sinon. Remarque: un nombre n est pair ssi `n%2=0`.
        2. Puis afficher le résultat de l'appel de cette fonction pour les valeurs 4 et 5.
    === "Correction"
        Exercice 18

        
    
[QCM](http://www.scientillula.net/NSI/premiere/notions%20de%20base/autoeval.html){:target="_blank"} 
