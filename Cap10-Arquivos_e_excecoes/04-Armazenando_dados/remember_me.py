#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:56:21 2025

@author: sergio
"""

#Bibliotecas
import json

#Entrada do usuário, nome
username = input("What is your name? ")

filename = "username.json" #Nome do arquivo

#Escrevendo arquivo json, uso da função json.dump()
with open(filename,'w') as f_obj:
    json.dump(username, f_obj) #Descarrega dados em um arquivo json
    print("We'll remember you when you come back, " + username + "!")