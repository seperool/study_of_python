#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:51:13 2024

@author: sergio
"""

name = "ada lovelace"
print(name.title()) #Primeiras letras em maiusculas
print(name.upper()) #Tudo em maiuscula
print(name.lower()) #Tudo em minuscula

#Quando for armazenar uma informação é util transformar em minuscula.

#Concatenação
#1)
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #"+" concatena informações
print(full_name)

#2)
print("Hello, " + full_name.title() + "!")

#3)
message = "Hello, " + full_name.title() + "!"
print(message)