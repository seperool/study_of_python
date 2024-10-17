#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:17:01 2024

@author: sergio
"""

#Módulo
#Argumentos nomeados e arbitrários (dicionário)

def make_car(fabricante, model, **info_car):
    car = {} #Inicia um dicionário vazio que receberá as informações
    car['fabricante'] = fabricante #Passa o valor fabricante pra chave frabricante
    car['modelo'] = model #Passa o valor model pra chave modelo
    for key, value in info_car.items(): #Percorre os argumentos chave-valor arbitrários
        car[key] = value
    return car