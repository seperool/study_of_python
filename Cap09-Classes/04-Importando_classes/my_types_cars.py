#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:55:27 2024

@author: sergio
"""

#Importando classes dos módulos
from car import Car
from electric_car import ElectricCar, Battery

#Criando instâncias e chamadas de descrição da instância
my_beetle = Car("volkswagem", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster', 2016)
print(my_tesla.get_descriptive_name())