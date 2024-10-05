#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:53:39 2024

@author: sergio
"""

#Função argumentos posicionais

def make_shirt(frase="Eu amo Python",tamanho='g'): #Parâmetros e default
    print("Será fabricada a camiseta tamanho " + tamanho.upper() +
          ", com a frase:")
    print('\n"' + frase+'"')

make_shirt("Quanto maior melhor!",'gg') #Arguemento posicional
make_shirt() #Argumentos default
make_shirt(tamanho='m') #Argumentos nomeados e default