#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:25:44 2024

@author: sergio
"""

#Argumentos posiciais e arbitrários

def ing_sanduiches(*ingredientes): #Parâmetro arbitrário e posicional
    print("\nO sanduiche pedido é feito de:")
    count = 0
    while count < len(ingredientes):
        ingrediente = ingredientes[count]
        print(ingrediente)
        count += 1

ing_sanduiches('pão','queijo')
ing_sanduiches('pão', 'queijo','presunto')
ing_sanduiches('pão', 'ovo')