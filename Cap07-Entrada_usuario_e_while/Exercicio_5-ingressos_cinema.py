#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:09:10 2024

@author: sergio
"""

# input e while
#Ingressos para o cinema

active = True

prompt = "O programa informa o preço do ingresso de acordo com a idade." 
prompt += "\n(Enter 'quit' when you are finished.)"
print(prompt)

while active:
    idade = input("\nInforme a sua idade: ")
    if idade == 'quit':
        print("Fim do programa")
        break
    idade = int(idade)
    if idade < 3:
        print("\nO ingresso é gratuito.")
    elif idade <= 12:
        print("\nO ingresso custará 10 dólares.")
    else:
        print("\nO ingresso custará 15 dólares.")
    