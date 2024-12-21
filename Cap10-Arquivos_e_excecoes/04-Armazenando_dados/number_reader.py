#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:50:14 2024

@author: sergio
"""

#Módulo
import json

#Arquivo a ser lido
filename = 'numbers.json'

#Abrir arquivo
with open(filename) as f_obj:
    numbers = json.load(f_obj) #Lendo arquivo json
    
print(numbers)
print(type(numbers))