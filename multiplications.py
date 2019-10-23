#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__= 'Mairien Anthony'
__version__ = '1.0.0'
__status__ = 'Training & fun'
######################################
# Programme table de multiplications #
#    (Try/Except,fonction,boucle)    #
######################################

# "Tant que Vrai", c'est-à-dire toujours, on exécute le code qui suit
while True:
    print("Ce programme va calculer la table de multiplication du nombre choisi \n")
    #Demande à l'utilisateur le nombre à calculer
    nb=input("Entrez un chiffre/nombre svp: ")
    try:
        #On essaye de convertir le nb en entier, et on print une erreur si ce n'en est pas un
        nb=int(nb)
    except ValueError:
        print("Merci de rentrer le chiffre/nombre au format numérique svp !")
    #Si pas d'erreur (else), on break la boucle, et on continue donc le programme
    else:
        break
#Création de la fonction servant à multiplier le nb
def multiplication(nb):
    compteur=0
    while compteur<10:
        compteur+=1
        print(compteur, "*", nb, "=", compteur * nb)
#Exécution de la fonction, avec le nb en paramètre
multiplication(nb)
