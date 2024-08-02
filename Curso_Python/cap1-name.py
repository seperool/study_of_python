#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:51:13 2024

@author: sergio
"""
# print

name = "ada lovelace"
print(name.title()) #Primeiras letras em maiusculas
print(name.upper()) #Tudo em maiuscula
print(name.lower()) #Tudo em minuscula

##Quando for armazenar uma informação é util transformar em minuscula.

#-----------------------------------------------------------------------------#

##Concatenação
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

#-----------------------------------------------------------------------------#

## removendo espaços em branco

favorite_linguage = ' python '

#1) Removendo espaços em branco do lado direito

favorite_linguage.rstrip()

#2) Removendo espaços em branco do lado esquerdo

favorite_linguage.lstrip()

#3) Removendo espaços em branco dos dois lados

favorite_linguage.strip()

#4) Armazenando num variável
# Remover espaços em branco não armazena dados automaticamente.

favorite_linguage = favorite_linguage.strip()
print(favorite_linguage)
