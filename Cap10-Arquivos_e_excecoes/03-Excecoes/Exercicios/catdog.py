#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:52:23 2024

@author: sergio
"""

try:
    with open('cats.txt') as file_cat:
        cats_names = file_cat.readlines()
        cats_names = cats_names.strip()
        print("\nNome dos gatos:")
        for cat in cats_names:
            cat = cat.strip()
            print(cat.title())
except FileNotFoundError:
    pass #Falhando silenciosamente

try:
    with open('dogs.txt') as file_dog:
        dogs_names = file_dog.readlines()
        print("\nNome dos cachorros:")
        for dog in dogs_names:
            dog = dog.strip()
            print(dog.title())
except FileNotFoundError:
    #Mensagem amigavel de error FileNotFoundError
    print("Arquivo dogs.txt não foi encontrado!")
    print("Verifique o repositório.")