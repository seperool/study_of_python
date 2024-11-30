#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:56:26 2024

@author: sergio
"""

#path, caminho ate o arquivo
file_name = 'learning_python.txt'

with open(file_name) as file_object: #Abrir arquivo e colocar em váriavel
    lines = file_object.readlines() #Criar uma lista de linhas

for line in lines: #Percorrer lista de linhas
    message = line.replace("Python", "C") #Substituir palavra
    print(message)