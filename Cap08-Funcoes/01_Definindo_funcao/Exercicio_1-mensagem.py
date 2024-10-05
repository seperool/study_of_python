#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:08:56 2024

@author: sergio
"""

#Definição da função

def display_message(): #Definição da função
    print("Aprendendo sobre funções.\n")
    func = {'Definição de função':'def',
            'Nome da função': 'Dá nome a função',
            'Parâmetros':'Uma informação de que a função precisa para executar sua tarefa.',
            'Corpo da função':'Bloco de programação indentado dentro da função.',
            'Chamar a função':'Chama a função para ser executada pelo Python.',
            'Argmento':'Um argumento é uma informação passada para uma função em sua chamada.'
            }
    for chave, valor in func.items():
        print(chave + ": " + valor)

display_message() #Chama a função