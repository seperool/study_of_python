#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:11:09 2024

@author: sergio
"""

#Path relativo
file_name = 'text_files/pi_digits.txt'

#Abrir arquivo pi_digits.txt
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())