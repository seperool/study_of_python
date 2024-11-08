#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:39:13 2024

@author: sergio
"""

#Importando classes
from car import ElectricCar

#Cria uma instância
my_tesla = ElectricCar("tesla",'model s',2016)

#Chama métodos
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()