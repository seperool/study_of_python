#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:38:54 2024

@author: sergio
"""

#Importando um módulo completo
##Importa tudas as classes do módulo
import car
#from nome_módulo

#Instâncias
my_beetle = car.Car('volkswagem', 'beetle', 2016)
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)

#Chamadas
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())