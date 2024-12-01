#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:25:10 2024

@author: sergio
"""

#path, caminho ate o arquivo
file_name = 'text_files/pi_digits.txt'

with open(file_name) as file_object: #Abre arquivo
    lines = file_object.readlines() #Cria um lista de linhas

pi_string = '' #Inicializa string pi como vazia
for line in lines: #Pecorre as linhas
    pi_string += line.strip() #Junta strings e remove espaços em branco

print(pi_string) #string pi sem espaço em branco
print(len(pi_string)) #Tamanho da string