#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:05:49 2024

@author: sergio
"""

#Função retornando dicionário
#Parâmetro opcional número de faixas do album
#Chamada de função com entradas de usuário

def make_album(artista,titulo,n_faixas=''):
    album = {'band':artista.title(),'title':titulo.title()}
    if n_faixas: #Ação opcional
        album['numero_faixas'] = n_faixas
    return album

prompt = "\nAdicione informações sobre o album."
prompt += "\n(Insira 'q' a qualquer momento para interromper o programa)"

while True:
    print(prompt)
    artist = input("\nInsira nome do artista/banda: ")
    if artist == 'q':
        break
    titulo = input("\nInsira o titulo do album: ")
    if titulo == 'q':
        break
    opcional = input("\nDeseja inserir o numero de faixas? (s/n) ")
    if opcional == 's':
        num_faixas = input("\nInsira o número de faixas do album: ")
        if num_faixas == "q":
            break
        album = make_album(artist, titulo, num_faixas)
    elif opcional == 'q':
        break
    else:
        album = make_album(artist, titulo)
    print("\n")
    print(album)