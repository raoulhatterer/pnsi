# script permettant de démarrer le serveur mkdocs

#1. Activation de l'environnement virtuel 
source /Users/raoul/.virtualenvs/mkDocs_env/bin/activate
#2. Affichage du répertoire courant
pwd
#3. Démarrage du serveur
mkdocs serve



# note:
#1. rendre le script exécutable avec : chmod +x startserver.sh
#2. l'exécuter avec:  ./startserver.sh
#3. l'exécuter dans ce buffer emacs avec C-c C-x (rajouter des apostrophes si le nom contient des espaces)
