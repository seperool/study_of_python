#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:43:56 2024

@author: sergio
"""

#Importando classe de um módulo
from car import Car
#from nome_módulo import nome_classe

#Chamadas
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()