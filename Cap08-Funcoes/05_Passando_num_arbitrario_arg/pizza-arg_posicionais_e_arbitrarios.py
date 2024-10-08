#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:36:11 2024

@author: sergio
"""

#Função que aceita argumento posicional e arbitrário
#Arbitrário: Não se sabe quantos argumentos a função vai receber

def make_pizza(size,*toppings): #Um argumento posicional e um arbitrário
    #Argumento arbritrário sempre no final
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

make_pizza(16,'peperoni') #Chamada com 1 argumento
make_pizza(12,'mushrooms','green peppers','extra cheese') #Chamada 1 argumento posicional e 3 argumentos arbitrários