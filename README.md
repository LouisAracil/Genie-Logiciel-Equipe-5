# Genie-Logiciel-Equipe-5

Les tests effectués consistent en une boucle qui ouvre 12345 fois un fichier de test afin de connaître la durée d'exécution de chaque langage.

## Fonctionnement du programme

Pour le nom du fichier, le programme prend le nom du fichier, il exécute un basename et un replace pour retirer les antislash.

Pour les auteurs, le programme récupère le nm du fichier, récupère le string avant le 1er underscore (cela correspond au nom d'un des auteurs), puis fait une recherche avec le string et récupère les données qui suivent.

Pour le titre, le programme récupère le nom du fichier, supprime le texte avant le 2ème underscore, puis fait une recherche avec le string restant et récupère les données qui suivent jusqu'à un saut de ligne.  

Pour récupérer l'abstract, le programme cherche le mot "abstract" et récupère le paragraphe qui suit jusqu'à un saut de ligne.

Pour les références bibliographiques, le programme cherche le mot "references" et récupère les données qui suivent.


## Exécution du programme

Pour exécuter le programme, il faut écrire dans un terminal "python3 main.py [-t|-x] repertoire".
-t : permet d'écrire les données dans un fichier en format txt
-x : permet d'écrire les données dans un fichier en format xml
repertoire : chemin vers le répertoire contenant les fichiers à parser
