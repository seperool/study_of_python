#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:17:30 2024

@author: sergio
"""

name = input("Qual seu nome? ")
with open('guest.txt','w') as file_object:
    file_object.write(name.title())