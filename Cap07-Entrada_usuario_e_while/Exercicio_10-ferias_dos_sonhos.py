#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:28:13 2024

@author: sergio
"""

ferias_sonhos = {}

active = True

while active:
    nome = input("Insira o nome: ")
    lugar = input("Se pudesse visitar um lugar no mundo, para onde iria? ")
    
    #Armazenando resposta no dicionário, nome como chave e lugar como valor correspondente
    ferias_sonhos[nome] = lugar
    
    #Criterio de saída
    nova_iteração = input("Gostaria de nova enquete? (yes/no) ")
    if nova_iteração == 'no':
        active = False

print("\n")
#Resultados da enquete
for nome, lugar in ferias_sonhos.items():
    print("Nas ferias dos sonhos de " + nome.title() + 
          " visitaria " + lugar.title())