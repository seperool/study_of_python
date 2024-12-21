#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:43:41 2024

@author: sergio
"""

#Módulo
import json

#Lista a ser salva
numbers = [2,3,5,7,11,13]

#Caminho (Path) file
filename = "numbers.json"

#Escrever arquivo json
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj) #Salvar valores json