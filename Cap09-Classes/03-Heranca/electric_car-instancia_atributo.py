#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:31:51 2024

@author: sergio
"""

#Herança

#classes-pai
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

class Battery():
    """
    Uma tentativa de simples de modelar uma bateria de carro elétrico.
    """
    
    def __init__(self,battery_size=70):
        """Inicializa atributos da bateria."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Exibe uma frase que descrevea capacidade da bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """
        Exibe uma frase sobre a distância
        que o carro é capaz de percorrer com essa bateria.
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

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
        self.battery = Battery() #Cria um atributo que é uma instância

#Instância
my_tesla = ElectricCar("tesla", "model s", "2016")

#Chamando método sobrescrito
print(my_tesla.get_descriptive())

#Chama atributo-instancia, que referencia um método
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()