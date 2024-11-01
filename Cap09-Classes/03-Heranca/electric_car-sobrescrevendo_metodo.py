#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 07:03:46 2024

@author: sergio
"""

#Herança

#classe-pai
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
        self.tank_gas = False
    #Métodos
    ##Descreve o carro atraves dos atributos
    def get_descriptive(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + " "
        long_name += self.make + " "
        long_name += self.model
        return long_name.title()
    
    ##Imprime odometer na tela
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    ##Método para modificar atributo
    def update_odometer(self,mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita aalteração se for tentativa de definir um valor menor para o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    ##Método para incrementar atributo
    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
    
    ##Método informa se tem um tank de gás
    def fill_gas_tank(self):
        if self.tank_gas == True:
            print("Contém um tanque de gás!")
        else:
            print("Não contém um tanque de gás!")

#Classe-filha
class ElectricCar(Car): #herança da classe-pai 'Car'
    """Representa aspectos de um carro especificos de veiculos elétricos."""
    
    #Atributos herdados
    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos especificos deum carro elétrico.
        """
        super().__init__(make, model, year) #herda atributos da classe-pai
        self.battery_size = 70 #definindo atrabuto da específico da classe-filha
        
    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    #Sobrescrevendo método
    def fill_gas_tank(self):
        """Carros elétricos não tem tanques de gasolina."""
        print("This car doesn't need a gas tank!")

#Instância
my_tesla = ElectricCar("tesla", "model s", "2016")

#Chamando método sobrescrito
my_tesla.fill_gas_tank()