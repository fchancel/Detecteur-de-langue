#!/bin/python3
# -*-coding:utf-8 -*

import pickle
import os.path
from os import listdir

def read_file(filename):
    """
    Lecture d'un fichier non binaire.

    @filename = nom du fichier à lire
    return une chaine de caractère représentant le contenu du fichier
    """
    with open(filename, 'r') as file:
        text = file.read()
    return text

def histogram(text):
    """
    Stock dans un dictionnaire toutes les lettres de l'alphabet (accent inclus) du texte ainsi que le nombre de fois où celle-ci est répété

    @text = texte à analyser
    return un dictionnaire ayant pour clef les lettres de l'alphabet trouvé dans le texte et pour valeur le nombre
    où celle-ci fut trouvé dans le texte
    """
    hist = {}
    for c in text:
        c = c.lower()
        cNb = ord(c)
        if (cNb >= 97 and cNb <= 122) or (cNb >= 191 and cNb <= 254):
            hist[c] = hist.get(c, 0)+1
    return hist

def normalize(hist):
    """
    Normalise les valeurs issu du dictionnaire fournit par la fonction histogram. Normaliser entre 0 et 1.

    @hist = dictionnaire à normaliser
    return un nouveau dictionnaire ayant pour clé les clés de @hist et pour valeurs la normalisation des valeurs issu de @hist
    """
    total = sum(hist.values())
    dict = {k : r/total for k, r in hist.items()}
    dict1 = sorted(dict.items(),key = lambda t: t[1], reverse=True)
    return dict


def trainLanguage(language, filename):
    """
    Entraine des dictionnaires à reconnaitre une langue

    @language = nom de la langue à entrainé (nom donné en francais)
    @filename = fichier avec lequel le dictionnaire doit être entrainé
    Return 0 ou 1 si le dictionnaire existait déjà ou non.
    """
    newDict = normalize(histogram(read_file(filename)))
    language = language.lower()
    if os.path.isfile('dict-comparaison/dict' + language):
        with open('dict-comparaison/dict' + language, 'rb') as file:
            dict = pickle.Unpickler(file)
            dict = dict.load()
        for elt in dict.items():
            res = newDict.get(elt[0], 0)
            dict[elt[0]] = (res + elt[1]) / 2
        result = 1
    else:
        dict = newDict
        result = 0

    with open('dict-comparaison/dict' + language, 'wb') as file:
        nDict = pickle.Pickler(file)
        nDict.dump(dict)
    return result
    
def returnOfficialDict(language):
    """
    Retourne le dictionnaire entrainé du language demandé en paramètre.

    @language = langue dont le dictionnaire entrainé est désiré
    return dictionnaire entrainé
    """
    if os.path.isfile('dict-comparaison/dict' + language):
        with open('dict-comparaison/dict' + language, 'rb') as file:
            dict = pickle.Unpickler(file)
            dict = dict.load()
            return dict

def checkConnection(officialDict, dico):
    """
    Calcul le pourcentage de correspondance entre le dictionnaire fournit et le dictionnaire entrainé

    @officialDict = Dictionnaire entraîné issu du dossier dict-comparaison
    @dico = Dictionnaire à comparé et créer avec la fonction normalize
    return le pourcentage de correspondance
    """
    if len(dico) == 0:
        return 0
    j = 0
    i = 0
    for elt in dico.items():
        if round(elt[1], 2) == round(officialDict.get(elt[0], 0), 2):
            i += 1
        j += 1
    return(i * 100 / j)

def findLanguage(dicNeedAnalyse):
    """
    Cherche quel langage est utilisé avec l'aide du dictionnaire fournit en paramètre

    @dicNeedAnalyse = dictionnaire issu de la fonction normalize
    return une chaine de caractère indiquant la langue utilisé
    """
    result = {}
    for f in listdir('dict-comparaison'):
        with open('dict-comparaison/' + f, 'rb') as file:
            officialDict = pickle.Unpickler(file)
            officialDict = officialDict.load()
            result[f[4:]] = checkConnection(officialDict, dicNeedAnalyse)
    result = sorted(result.items(),key = lambda t: t[1], reverse=True)
    return(result[0][0].capitalize())