#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:49:18 2024

@author: sergio
"""

#Path relativo
file_name = 'text_files/pi_digits.txt'

#Abrir arquivo pi_digits.txt
with open(file_name) as file_object:
    
    #Método for para ler linhas de um arquivo
    for line in file_object:
        print(line.rstrip())