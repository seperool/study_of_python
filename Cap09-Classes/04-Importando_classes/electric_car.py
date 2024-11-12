#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:39:43 2024

@author: sergio
"""

"""
Um conjunto de classes que pode ser usado para representar carros elétricos.
"""

#Importando classe-pai
from car import Car

#Classes-filhas
class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""
    
    #Atributos
    def __init__(self,battery_size=70):
        """Inicializa atributos da bateria."""
        self.battery_size = battery_size
    
    #Métodos
    def describe_battery(self):
        """Exibe uma fraseque descreve a capacidade da bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """
        Exibe frase sobre a distância que o carro pode percorrer 
        com essa bateria.
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    
    #Atributos
    def __init__(self,make,model,year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make,model,year)
        self.battery = Battery()