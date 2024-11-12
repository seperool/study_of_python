#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:21:35 2024

@author: sergio
"""

"""
Uma classe que pode ser usada para representar um carro.
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