#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:39:02 2024

@author: sergio
"""

while True:
    entrada = input("Gostaria de responder a enquete? (s/n)\n")
    if entrada == 's':
        name = input("Informe o nome:\n")
        resposta = input("Por que você gosta de programar?\n")
        with open('Enquete.txt','a') as file_object:
            file_object.write('Nome: '+ str(name) + '\n')
            file_object.write('\t' + str(resposta) + '\n')
    else:
        break