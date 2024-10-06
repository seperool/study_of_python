#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:20:52 2024

@author: sergio
"""

#Passando uma lista para uma função

def show_magicians(lista_magicos):
    print("\nLista de todos os magicos:")
    for magico in lista_magicos:
        print(magico.title())

def make_great(lista):
    count = 0 #Contador
    while count < len(lista): #Enquanto contador menor que tanhanho da lista
        lista[count] = "Grande " + lista[count]
        count += 1 #Acrescentando +1 ao contador
    return lista

lista_magicos = ['david cooperfild', 'cris angel', 'mister m']
list_great_magicians = make_great(lista_magicos[:]) #Passando uma copia da lista
show_magicians(lista_magicos)
show_magicians(list_great_magicians)