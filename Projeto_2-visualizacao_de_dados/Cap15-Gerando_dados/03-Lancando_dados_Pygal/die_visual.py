#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:16:03 2025

@author: sergio
"""

# Importa a classe Die do módulo die
from die import Die

# Cria um dado de 6 lados
D6 = Die()

# Inicializa uma lista para armazenar os resultados
results = []
# Simula 1000 lançamentos
for roll_num in range(1000):
    # Lança o dado
    result = D6.roll()
    # Adiciona o resultado à lista
    results.append(result)

# Imprime os resultados
print(results)

# Inicializa uma lista para armazenar as frequências
frequencies = []
# Calcula a frequência de cada valor
for value in range(1, D6.num_sides + 1):
    # Conta as ocorrências do valor
    frequency = results.count(value)
    # Adiciona a frequência à lista
    frequencies.append(frequency)

# Imprime as frequências
print(frequencies)