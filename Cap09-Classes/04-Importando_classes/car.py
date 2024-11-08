#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:21:35 2024

@author: sergio
"""

"""
Um conjunto de classes usado para representar carros á gasolina e elétricos.
"""

#Classes
class Car():
    """Uma tentativa simples de representar um carro."""
    def __init__(self,make,model,year):
        """Inicializa os atributos que descrevem um carro."""
        #Atributo
        self.make = make
        self.model = model
        self.year = year
        
        #Atributo default
        self.odometer_reading = 0
    
    #Métodos
    def get_descriptive_name(self):
        """
        Devolve um nome descritivo formatado de modo elegante.
        """
        long_name = str(self.year) + " " + self.make
        long_name += " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita alteração se for tentativa de definir um valor menor
        para o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,miles):
        """
        Soma a quantidade especificada ao valor de leitura do hodômetro.
        """
        self.odometer_reading += miles

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