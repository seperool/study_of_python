#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:29:42 2024

@author: sergio
"""

#Criando módulo = um função para importação
def make_pizza(size,*toppings): #parâmetros, um posicional e um arbitrario (tupla)
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)