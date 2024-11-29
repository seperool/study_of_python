#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:22:11 2024

@author: sergio
"""

#path, caminho ate o arquivo
file_name = 'text_files/pi_million_digits.txt'

with open(file_name) as file_object: #Abre arquivo
    lines = file_object.readlines() #Cria um lista de linhas

pi_string = '' #Inicializa string pi como vazia
for line in lines: #Pecorre as linhas
    pi_string += line.strip() #Junta strings e remove espaços em branco

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")