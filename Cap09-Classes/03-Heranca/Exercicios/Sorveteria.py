#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:37:27 2024

@author: sergio
"""

#Definindo a classe

#Classe-pai
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

#Classe-filha
class IceCreamStand(restaurant):
    
    #Atributos
    def __init__(self,restaurant,cuisine_type):
        #Atributos originais
        self.flavors = ["maracuja","manga",
                        "menta com flocos", "morango",
                        "creme", "chocolate"]
        #Atributos herdados
        super().__init__(restaurant, cuisine_type)
     
    #Métodos
    def favors_scream (self):
        print(f"Os sabores de sorvete são:")
        for sabor in self.flavors:
            print(sabor)

#Instância
restaurante01 = IceCreamStand("sorveteria", "lanchonete")

#Chamadas
restaurante01.favors_scream()