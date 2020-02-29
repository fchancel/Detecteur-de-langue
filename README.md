# DETECTEUR DE LANGUE

Fonctionne uniquement sur des textes longs. Gère le francais, l'anglais, l'allemand, l'espagnol et l'italien

## Challenge

Création d'un programme fonctionnant sous le terminal avec pour objectif de détecter 
la langue utilisé dans un fichier texte passé en argument.
Le détecteur de langue gère le francais, l'anglais, l'allemand, l'espagnol et l'italien.
Celui-ci ne fonctionne qu'avec les textes longs.
Création d'un programme fonctionnant sous le terminal ayant pour objectif d'entraîner
une langue déjà présente ou d'en rajouter une nouvelle.

## Détails et Conception

Le programme de détection de langue se passe en plusieurs étapes.
1 - Appel d'une fonction permettant de lire un fichier non binaire et retournant
une chaine de caractère comportant le contenu du fichier.
2 - Stockage dans un dictionnaire de toutes les lettres (accents inclus) du texte
ainsi que le nombre d'occurence de celles-ci.
3 - Normalisation le nombre d'occurence des lettres issus du dictionnaire. Normaliser entre 0 et 1.
4 - Comparaison des valeurs normaliser avec les différents dictionnaires entraîné. 
Chaque valeurs identique (arrondis à trois chiffres après la virgule) rapporte un point.
Le tout est mit en pourcentage, ce qui donne un pourcentage de correspondance entre 
les différentes langues.
Le dictionnaire entraîné possédant le plus haut pourcentage de comptabilité avec 
le dictionnaire issu du texte est considéré comme language utilisé dans le fichier
dont l'analyse était demandé.

## Usage
Détecteur de langue:
Utilisation : `./detect_language.py  FICHIER`
Saisissez `./detect_language.py --help` pour plus d'information

Entraînement d'une langue :
Utilisation :  ./train_language.py LANGUE  FICHIER`
Saisissez ` ./train_language.py --help` pour plus d'information