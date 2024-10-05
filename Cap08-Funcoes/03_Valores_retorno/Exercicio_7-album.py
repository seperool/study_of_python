#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:36:12 2024

@author: sergio
"""

#Função retornando dicionário
#Parâmetro opcional número de faixas do album

def make_album(artista,titulo,n_faixas=''):
    album = {'band':artista.title(),'title':titulo.title()}
    if n_faixas: #Ação opcional
        album['numero_faixas'] = n_faixas
    return album

album_1 = make_album('pearl jam', "ten")
print(album_1)
album_2 = make_album('matanza', "pior cenário possível",10)
print(album_2)
album_3 = make_album('system of a down', "hypnotize")
print(album_3)