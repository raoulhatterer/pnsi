# Vers le tri par insertion

![image](data/insertion1.gif){: .center}


Comme dans tous les autres algorithmes de tri que nous allons étudier, nous allons travailler **en place**. Cela signifie que nous ne travaillons que sur la liste initiale, sans en créer de nouvelles. Le tri sera fait en permutant des éléments.

- On traite successivement toutes les valeurs à trier, en commençant par celle en deuxième position.
- Traitement : tant que la valeur à traiter est inférieure à celle située à sa gauche, on échange ces deux valeurs. On procède par permutations.



??? note "Code à trous :star: :star: :star: :star:"
    ```python linenums='1'
    def tri_insertion(lst):
        '''trie en place la liste lst donnée en paramètre'''
                           
    ``` 



??? note "Code à trous :star: :star: :star: :octicons-star-24: " 
    ```python linenums='1'
    def tri_insertion(lst):
        '''trie en place la liste lst donnée en paramètre'''
        for i in range(..., ...):                 
            ... = ...                                    
            while ... > ... and ... > ... :      
                ..., ... = ..., ...      
                ... = ...                              
    ``` 

??? note "Code à trous :star: :star: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def tri_insertion(lst):
        '''trie en place la liste lst donnée en paramètre'''
        for i in range(..., len(lst)):                 
            k = ...                                    
            while k > ... and lst[...] > lst[...] :      
                lst[...], lst[...] = lst[...], lst[...]      
                k = ...                               
    ``` 



??? note "Code à trous :star: :octicons-star-24: :octicons-star-24: :octicons-star-24:"
    ```python linenums='1'
    def tri_insertion(lst):
        '''trie en place la liste lst donnée en paramètre'''
        for i in range(1, len(lst)):                 
            k = ...                                    
            while k > ... and lst[k-1] > lst[k] :      
                lst[k], lst[k-1] = lst[...], lst[...]      
                k = ...                               
    ``` 
        



