#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:50:23 2024

@author: sergio
"""

#Passando um número arbitrário de argumentos
#Não se sabe quantos argumentos a função vai receber

def make_pizza(*toppings): #Cria uma tupla para receber número aleatório de argumentos
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(topping)

make_pizza('peperoni') #Chamada com 1 argumento
make_pizza('mushrooms','green peppers','extra cheese') #Chamada com 3 argumentos