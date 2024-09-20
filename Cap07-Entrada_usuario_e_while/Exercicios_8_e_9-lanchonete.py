#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:14:12 2024

@author: sergio
"""

#Lanchonete

sandwich_orders = ['queijo com presunto','pastrami','ovo',
                   'queijo','pastrami','salame','atum','pastrami']

finished_sandwiches = []

#Removendo todas as ocorrencias de determinado valor, 'pastrami'
print("Estamos sem pastrami.")
while 'pastrami' in sandwich_orders: #Enquanto tiver determinado valor na lista:
    sandwich_orders.remove('pastrami') #Remova o primeiro que encontrar, a cada iteração


#Transferindo itens de uma lista para outra, usando while
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    print("Preparei seu sanduiche de " + sandwich + ".")
    finished_sandwiches.append(sandwich)
    
print("Sanduiches preparados:")
for pronto in finished_sandwiches:
    print(pronto)

