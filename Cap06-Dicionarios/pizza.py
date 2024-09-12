#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:52:42 2024

@author: sergio
"""

#Armazena informações sobre uma pizza que está sendo pedida
pizza = {'crust':'thick',
          'toppings':['mushrooms','extra cheese']}

#Resumo do pedido
print("You ordered a " +
      pizza['crust'] +
      '-crust pizza ' + 
      "with the following toppings:")
for topping in pizza['toppings']:
  print('\t'+topping)
