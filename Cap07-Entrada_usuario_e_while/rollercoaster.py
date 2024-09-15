#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 04:46:35 2024

@author: sergio
"""

height = input("How tall are you, in inches? ") #Lê a entrada como string
height = int(height) #Converte a entrada para número inteiro

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")