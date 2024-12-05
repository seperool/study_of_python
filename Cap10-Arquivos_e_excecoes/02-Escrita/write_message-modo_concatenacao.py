#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:53:01 2024

@author: sergio
"""

#Nome do arquivo
filename = 'programming.txt'

#Abre o arquivo e concatena dados ('a'), acrescenta informação
with open(filename,'a') as file_object:
    file_object.write("I also finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")