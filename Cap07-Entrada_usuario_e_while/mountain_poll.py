#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:39:52 2024

@author: sergio
"""

#Preenchendo um dicionário com dados de entrada e saída

#Inicializando um dicionário vazio
responses = {}

#Flag
polling_active = True

while polling_active:
    #Pede o nome da pessoa e a resposta
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you to climb someday? ")
    
    #Armazenando resposta no dicionário, name como chave e response como valor.
    responses[name] = response
    
    #Criterio de saída do laço, ou nova enquete
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#Percorrendo o dicionário
#Enquete concluída, mostra o resultado
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
