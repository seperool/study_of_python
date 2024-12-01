#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:11:09 2024

@author: sergio
"""

#Path relativo
file_name = 'text_files/pi_digits.txt'

#Abrir arquivo pi_digits.txt
with open(file_name) as file_object:
    
    #Método readlines, para leitura de linhas em uma lista
    lines = file_object.readlines()
    
#Percorrendo a lista de linhas
for line in lines:
    print(line.rstrip()) #Elimando espaços em branco com o método rstrip()