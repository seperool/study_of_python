#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:16:03 2025

@author: sergio
"""

from die import Die

#Cria uma instancia de D6
D6 = Die()

#Faz alguns lançamentos e armazena os resultados numa lista
results = []
for roll_num in range(100):
    result = D6.roll()
    results.append(result)

print(results)