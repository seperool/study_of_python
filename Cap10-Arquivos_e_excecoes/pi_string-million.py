#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:01:43 2024

@author: sergio
"""

#path, caminho ate o arquivo
file_name = 'text_files/pi_million_digits.txt'

with open(file_name) as file_object: #Abre arquivo
    lines = file_object.readlines() #Cria um lista de linhas

pi_string = '' #Inicializa string pi como vazia
for line in lines: #Pecorre as linhas
    pi_string += line.strip() #Junta strings e remove espaços em branco

print(pi_string[:50] + "...") #string pi sem espaço em branco
print(len(pi_string)) #Tamanho da string