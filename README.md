# DETECTEUR DE LANGUES

Fonctionne uniquement sur des textes longs.

Gère actuellement le francais, l'anglais, l'allemand, l'espagnol et l'italien (Possibilité de rajouter de nouvelles langues a l'aide de l'entraineur de langues)

## Challenge

Création d'un programme fonctionnant sous le terminal, avec pour objectif de détecter la langue utilisée dans un fichier texte passé en argument ainsi qu'un entraineur permettant d'entrainer une langue déjà présente ou d'en rajouter une nouvelle.

Le détecteur de langues gère le francais, l'anglais, l'allemand, l'espagnol et l'italien.

Celui-ci ne fonctionne qu'avec les textes longs.



## Détails et Conception


Le programme de détection de langues se déroule en plusieurs étapes.

1 - Appel d'une fonction permettant de lire un fichier non binaire et retournant une chaine de caractères comportant le contenu du fichier.

2 - Stockage dans un dictionnaire de toutes les lettres (accents inclus) du texte ainsi que le nombre d'occurences de celles-ci.

3 - Normalisation du nombre d'occurences des lettres issues du dictionnaire. Normalisées entre 0 et 1.

4 - Comparaison des valeurs normalisées avec les différents dictionnaires entraînés. Chaque valeur identique (arrondie à trois chiffres après la virgule) rapporte un point.
Le tout est mis en pourcentage, ce qui donne un pourcentage de correspondance entre 
les différentes langues.
Le dictionnaire entraîné possédant le plus haut pourcentage de comptabilité avec 
le dictionnaire issu du texte est considéré comme language utilisé dans le fichier
dont l'analyse était demandée.



## Usage

Détecteur de langues:


Utilisation : `./detect_language.py  FICHIER`

Saisissez `./detect_language.py --help` pour plus d'informations



Entraînement d'une langue :


Utilisation :  `./train_language.py LANGUE  FICHIER`

Saisissez ` ./train_language.py --help` pour plus d'informations