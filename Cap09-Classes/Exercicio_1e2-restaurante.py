#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 01:13:37 2024

@author: sergio
"""

#Definindo a classe
class restaurant():
    
    #Atributos
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    #Métodos
    def describe_restaurant(self):
        print("O nome do restaurante é " + self.restaurant_name.title() + ".")
        print("O tipo da cozinha é " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " esta aberto!")

#Novas instâncias
new_restaurant_1 = restaurant("ratatulé", "massas")
new_restaurant_2 = restaurant("pé sujo", "comida caseira")
new_restaurant_3 = restaurant("tramelinha", "restaurante familiar")


#Mostrando os atributos da instância
print(new_restaurant_1.restaurant_name.title())
print(new_restaurant_1.cuisine_type)

#Chamando os métodos da instância
new_restaurant_1.describe_restaurant()
new_restaurant_1.open_restaurant()


#Chamada do método describe_restaurant para cada instância
print("\nDescrição dos restaurantes.")
print("Descrição do restaurante 1:")
new_restaurant_1.describe_restaurant()
print("\nDescrição do restaurante 2:")
new_restaurant_2.describe_restaurant()
print("\nDescrição do restaurante 3:")
new_restaurant_3.describe_restaurant()