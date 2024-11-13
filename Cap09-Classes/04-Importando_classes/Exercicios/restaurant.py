#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:19:31 2024

@author: sergio
"""

#Definindo a classe
class Restaurant():
    
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