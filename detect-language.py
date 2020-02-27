#!/bin/python3
# -*-coding:utf-8 -*

import pickle
import os.path

def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def histogram(text):
    hist = {}
    for c in text:
        if ord(c) != ' ' and c != '\n':
            hist[c.lower()] = hist.get(c.lower(), 0)+1
    return hist

def normalize(hist):
    total = sum(hist.values())
    dict = {k : r/total for k, r in hist.items()}
    dict1 = sorted(dict.items(),key = lambda t: t[1], reverse=True)
    return dict


def trainLanguage(language, filename):
    newDict = normalize(histogram(read_file(filename)))
    if os.path.isfile('dict' + language):
        with open('dict' + language, 'rb') as file:
            dict = pickle.Unpickler(file)
            dict = dict.load()
        for elt in dict.items():
            res = newDict.get(elt[0], 0)
            dict[elt[0]] = (res + elt[1]) / 2
    else:
        dict = newDict

    with open('dict' + language, 'wb') as file:
        nDict = pickle.Pickler(file)
        nDict.dump(dict)
    
def returnDict(language):
    if os.path.isfile('dict' + language):
        with open('dict' + language, 'rb') as file:
            dict = pickle.Unpickler(file)
            dict = dict.load()
            return dict

def checkConnection(officialDict, dict):
    j = 0
    i = 0
    for elt in dict.items():
        if round(elt[1], 2) == round(officialDict.get(elt[0], 0), 2):
            i += 1
        j += 1
    return(i * 100 / j)

# textvf = normalize(histogram(read_file('textger.txt')))
# print(checkConnection(returnDict('turc'), textvf))



# dictvf = normalize(histogram(read_file('textvf.txt')))
# dicten = normalize(histogram(read_file('texten.txt')))
# dictger = normalize(histogram(read_file('textger.txt')))
# dicttur = normalize(histogram(read_file('texttur.txt')))
# print('ve = {}'.format(dicten.get('h')))
# print('vf = {}'.format(dictvf.get('h')))
# print('vger = {}'.format(dictger.get('h')))
# print('vtur = {}'.format(dicttur.get('h')))

