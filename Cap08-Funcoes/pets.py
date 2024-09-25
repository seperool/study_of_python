#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:57:21 2024

@author: sergio
"""

#Passando argumentos para função

#Argumentos posicinais:
#Os argumentos são passados na mesma ordem 
#em que os parâmetros na definição da função aparecem

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', "harry") #Argumento posicional