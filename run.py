#!/bin/python3
# -*-coding:utf-8 -*

import sys
import os.path
import pickle
from detect_language import *

if len(sys.argv) < 2:
    print('Veuillez indiquer un fichier à lire en argument')
    sys.exit(1)
elif len(sys.argv) > 2:
    print(sys.argv[0], " ne prend qu'un seul paramètre")
    sys.exit(1)

if os.path.isfile(sys.argv[1]) != True:
    print(sys.argv[0], "ne trouve pas le fichier indiquer")
else:
    dico_need_analyse = normalize(histogram(read_file(sys.argv[1])))
    result = findLanguage(dico_need_analyse)
    print(result)