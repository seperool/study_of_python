#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:35:42 2025

@author: sergio
"""

#Biblioteca
import json #Biblioteca json

#Patch arquivo json
filename = "username.json"

with open(filename) as f_obj: #Abrindo arquivo
    username = json.load(f_obj) #Carrega informações armazenadas
    print("Welcome back, " + username + "!")