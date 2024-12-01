#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:02:51 2024

@author: sergio
"""

#path, caminho ate o arquivo
file_name = 'learning_python.txt'

#1) Ler o arquivo inteiro
print("Lendo arquivo inteiro de uma vez.")
with open(file_name) as file_object:
    arquivo = file_object.read()
    print(arquivo)

#2) Ler o arquivo linha por linha - método for
print("\nMétodo for para leitura de arquivo.\n")
with open(file_name) as file_object:
    for linha in file_object:
        print(linha)

#3) Ler o arquivo lista de linhas - método readlines()
with open(file_name) as file_object:
    lines = file_object.readlines()

print("\nMétodo readlines().\n")
for line in lines:
    print(line)