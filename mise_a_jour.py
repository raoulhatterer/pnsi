# Script python qui
# Fait la même chose que le script bash
# ```for i in $(find ./ -type d -name '.git')
#   do sed -i s/hg@forge/git@forge/ $i/config
# done```
# Est utilisée pour remplacer la chaîne de caractères hg@forge par git@forge dans les fichiers config correspondants.

# Notez que ce script modifie les fichiers de configuration des dépôts Git,
# il est donc important de bien comprendre ce qu'il fait avant de l'exécuter.
# Assurez-vous également de sauvegarder vos fichiers avant de les modifier.


import os
import fileinput

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if name == ".git":
            config_file = os.path.join(root, name, "config")

            for line in fileinput.input(config_file, inplace=True):
                print(line.replace("hg@forge", "git@forge"), end='')

