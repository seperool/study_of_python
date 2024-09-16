#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:23:25 2024

@author: sergio
"""

#1) Locação de carros

prompt1 = "Qual carro deseja locar? " #Criando prompt do input() separado
carro = input(prompt1)
print("Deixa-me ver se consigo um(a) " + carro.title() + " para você.")

#2) Lugares em um restaurante

num_pessoas = input("Quantas pessoas estão em seu grupo para jantar? ")
num_pessoas = int(num_pessoas) #Transformando a representação númerica coletada em int
if num_pessoas > 8:
    print("É preciso esperar uma mesa.")
else:
    print("A mesa esta pronta.")

#3) Multiplos de dez
num = input("Informe um número qualquer: ")
num = int(num)
if num % 10 == 0:
    print("O número " + str(num) + " é multiplo de dez.")
else:
    print("O número " + str(num) + " não é multiplo de dez.")