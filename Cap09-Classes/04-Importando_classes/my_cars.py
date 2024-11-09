#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:18:32 2024

@author: sergio
"""

#Importando classes de um módulo
from car import Car, ElectricCar
#from nome_módulo import nome_classe_1, nome_classe_2, ...

#Instâncias
my_beetle = Car('volkswagem', 'beetle', 2016)
my_tesla = ElectricCar('tesla', 'roadster', 2016)

#Chamadas
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())