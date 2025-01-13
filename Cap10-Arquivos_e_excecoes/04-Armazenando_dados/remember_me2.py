#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:45:16 2025

@author: sergio
"""

import json

# Carrega o nome do usuário se foi armazenado anteriormente
# Caso contrário, pede que o usuário forneça o nome e armazena essa informação
filename = "username.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you como back, "+
              username + "!")
else:
    print("Wellcome back, " + username + "!")