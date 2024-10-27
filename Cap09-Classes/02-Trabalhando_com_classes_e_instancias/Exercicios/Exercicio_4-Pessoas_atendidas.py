#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:17:35 2024

@author: sergio
"""

#Definindo a classe
class restaurant():
    
    #Atributos
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #Atributo default
        self.number_served = 0
    
    #Métodos
    def describe_restaurant(self):
        print("O nome do restaurante é " + self.restaurant_name.title() + ".")
        print("O tipo da cozinha é " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("O restaurante " + self.restaurant_name.title() + " esta aberto!")
    
    ##Método para mudar atributo
    def set_number_served(self,number_client_atendidos):
        self.number_served = number_client_atendidos
    
    ##Incrementa atributo atraves de um método
    def increment_number_served(self,increment_served):
        self.number_served += increment_served

#Novas instâncias
new_restaurant_1 = restaurant("ratatulé", "massas")

#Apresentando atributo default e modificando de maneira direta
print(f"Numéro de clientes atendidos: {new_restaurant_1.number_served}")
new_restaurant_1.number_served = 23
print(f"Numéro de clientes atendidos: {new_restaurant_1.number_served}")

#Método para mudar atributo
print(f"\nNuméro de clientes atendidos: {new_restaurant_1.number_served}")
new_restaurant_1.set_number_served(45)
print(f"Numéro de clientes atendidos: {new_restaurant_1.number_served}")

#Método para incrementar atributo
new_restaurant_1.set_number_served(0)
print(f"\nNuméro de clientes atendidos, no inicio do dia: {new_restaurant_1.number_served}")
new_restaurant_1.increment_number_served(23)
print(f"Numéro de clientes atendidos, ao final do dia: {new_restaurant_1.number_served}")
