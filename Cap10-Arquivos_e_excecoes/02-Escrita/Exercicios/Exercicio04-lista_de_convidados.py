#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:30:17 2024

@author: sergio
"""

while True:
    entrada = input("Olá gostaria de se registrar? (s/n)")
    if entrada == 's':
        name = input("Entre com o nome: ")
        with open('guest_book.txt','a') as file_object:
            file_object.write(str(name)+"\n")
        print("Olá " + str(name).title() + 
              "! Você esta cadastrado(a) na lista de convidados.")
    else:
        break