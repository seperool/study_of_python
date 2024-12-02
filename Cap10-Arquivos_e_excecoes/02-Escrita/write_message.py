#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:31:34 2024

@author: sergio
"""

#Nome do arquivo a ser criado
filename = 'programming.txt'

#Abre e define que é um arquivo a ser criado e escrito ('w')
with open(filename,'w') as file_object:
    file_object.write("I love programming.") #Escreve no arquivo