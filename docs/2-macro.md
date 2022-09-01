# Macro

On peut créer sa propre macro Python

Dans le fichier `main.py`, si on ajoute une nouvelle macro comme :

```py
    @env.macro
    def affiche_addition(x, y):
        texte = []
        texte.append("Voici une addition")
        texte.append("")
        texte.append(f"{x} + {y} = {x + y}")
        texte.append("")
        texte.append("Avec LaTeX")
        texte.append("")
        texte.append(f"$${x} + {y} = {x + y}$$")
        return "\n".join(texte)
```

Il faut alors stopper `mkdocs serve` puis le relancer ; à chaque nouvel ajout de macro.

On peut alors l'utiliser

!!! note "Entrée"
    {{ "{{ affiche_addition(30, 12) }}" }}

!!! done "Rendu"
    Il est délicat (mais possible) de l'avoir dans une admonition. Pour commencer, utiliser des macros qui renvoient plusieurs lignes de texte **hors** admonition et autre cadre avec indentation.

{{ affiche_addition(30, 12) }}

Pour de plus amples informations, se référer à la documentation : <https://mkdocs-macros-plugin.readthedocs.io/en/latest/>
