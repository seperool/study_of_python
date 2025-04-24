#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:16:03 2025

@author: sergio
"""

from die import Die

# Cria uma instância da classe Die, que por padrão representa um dado de 6 lados (D6)
D6 = Die()

# Cria uma lista vazia para armazenar os resultados dos lançamentos
results = []
# Loop que roda 1000 vezes para simular 1000 lançamentos do dado
for roll_num in range(1000):
    # Lança o dado e obtém um valor aleatório entre 1 e o número de lados do dado
    result = D6.roll()
    # Adiciona o resultado do lançamento à lista de resultados
    results.append(result)

# Imprime a lista com todos os resultados dos 1000 lançamentos
print(results)

# Cria uma lista vazia para armazenar a frequência de cada valor que saiu no dado
frequencies = []
# Loop que itera por cada possível valor que o dado pode ter (de 1 até o número de lados)
for value in range(1, D6.num_sides + 1):
    # Conta quantas vezes cada valor específico apareceu na lista de resultados
    frequency = results.count(value)
    # Adiciona a frequência desse valor à lista de frequências
    frequencies.append(frequency)

# Imprime a lista com a frequência de cada valor. O primeiro número corresponde à frequência do valor 1, o segundo do valor 2, e assim por diante.
print(frequencies)