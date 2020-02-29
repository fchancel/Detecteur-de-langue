#!/bin/python3
# -*-coding:utf-8 -*

import sys
import os.path
import pickle
from functions import *

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Utilisation : {0}  FICHIER\n\
Saisissez " {0} --help " pour plus d\'information'.format(sys.argv[0]))
    sys.exit(1)
elif sys.argv[1] == '--help':
        print('Utilisation : {0} FICHIER\n\
Analyse le texte issu de FICHIER et indique la langue utilisé dans celui-ci.'.format(sys.argv[0]))

elif os.path.isfile(sys.argv[1]) != True:
    print("{}: impossible d'accéder à '{}': Aucun fichier ou dossier de ce type".format(sys.argv[0], sys.argv[1]))
else:
    dico_need_analyse = normalize(histogram(read_file(sys.argv[1])))
    result = findLanguage(dico_need_analyse)
    print(result)