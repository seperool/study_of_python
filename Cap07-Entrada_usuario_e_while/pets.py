#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:27:05 2024

@author: sergio
"""

#Removendo todas as instancias de valores especificos de uma lista

pets = ["dog","cat","dog","goldfish","cat","rabbit","cat"]
print(pets)

while 'cat' in pets: #Enquanto 'cat' contido na lista pets faça:
    pets.remove('cat')

print(pets)