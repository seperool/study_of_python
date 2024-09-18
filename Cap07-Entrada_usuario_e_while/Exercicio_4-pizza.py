#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:56:36 2024

@author: sergio
"""

#input e laço while
#Ingredientes para uma pizza

prompt = "\nEntre com os ingredientes da pizza."
prompt += "\n(Enter 'quit' when you are finished.)"
prompt += "\n"

prompt2 = "\nAdicione novo ingrediente:"
prompt2 += "\n(Enter 'quit' when you are finished.)"
prompt2 += "\n"

pizza = []
active = True

print(prompt)

while active:
    ingrediente = input(prompt2)
    if ingrediente == 'quit':
        break
    else:
        print("O ingrediente " + ingrediente + " foi adicionado a pizza.")
        pizza.append(ingrediente)
print("\nA pizza será feita com os ingredientes:")
for ing in pizza:
    print(ing)