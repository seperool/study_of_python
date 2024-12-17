#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:39:35 2024

@author: sergio
"""

print("Soma dois números inteiros.")
while True:    
    numero_1 = input("digite o primeiro número: ")
    numero_2 = input("digite o segundo número: ")
    try:
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    except ValueError:
        print("Não é possivel somar com strings, por favor digite números.")
    else:
        numero_total = numero_1 + numero_2
        print("A soma é " + numero_total)
    arg = input("Gostaria de continuar (s/n): ")
    if arg == 'n':
        break