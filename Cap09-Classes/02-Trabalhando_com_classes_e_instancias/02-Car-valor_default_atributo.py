#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:08:52 2024

@author: sergio
"""

#Cria a classe
class Car():
    """Uma tentativa simples de representar um carro."""
    
    #Inicializa atributos
    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        
        #Atributo default
        #Não precisa ser inicializado no parâmetro
        self.odometer_reading = 0 #Atributo com valor default
    
    #Métodos
    def get_descriptive(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + " "
        long_name += self.make + " "
        long_name += self.model
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

#Cria uma instância
new_car = Car('audi', 'a4', 2016)

#Descreve a instância/objeto atraves do método, chama o método
print(new_car.get_descriptive())
new_car.read_odometer() #Método que imprime atributo default