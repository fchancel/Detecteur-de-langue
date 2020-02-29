#!/bin/python3
# -*-coding:utf-8 -*

import sys
import os.path
import pickle
from functions import *

if len(sys.argv) < 2:
    print('Utilisation : {0} LANGUE  FICHIER\n\
Saisissez " {0} --help " pour plus d\'information'.format(sys.argv[0]))
    sys.exit(1)
elif sys.argv[1] == '--help':
        print('Utilisation : {0} LANGUE FICHIER\n\
Entraine LANGUE avec le texte issu de FICHIER\n\
LANGUE doit être écrit dans la langue francaise'.format(sys.argv[0]))

elif os.path.isfile(sys.argv[2]) != True:
    print("{}: impossible d'accéder à '{}': Aucun fichier ou dossier de ce type".format(sys.argv[0], sys.argv[1]))
else:
    result = trainLanguage(sys.argv[1], sys.argv[2])
    if result == 1:
        print('Succès: La langue {} fut entraîné avec le texte issu de {}.'.format(sys.argv[1], sys.argv[2]))
    else:
        print('Succès: La langue {} n\'existait pas et fut créé à l\'aide du texte issu de {}'.format(sys.argv[1], sys.argv[2]))