#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 13:51:02 2025

@author: sergio
"""

# Importando bibliotecas
# Importa a classe Die do módulo die
from die import Die
# Importa a biblioteca pygal para gráficos.
import pygal

# Cria dois dado de 8 lados, instância
D8_1 = Die(8)
D8_2 = Die(8)

# Inicializa uma lista para armazenar os resultados
results = []
# Simula 1000 lançamentos
for roll_num in range(1000):
    # Lança o dado
    result = D8_1.roll()+D8_2.roll()
    # Adiciona o resultado à lista
    results.append(result)

# Imprime os resultados
print(results)

# Inicializa uma lista para armazenar as frequências
frequencies = []
max_result = D8_1.num_sides + D8_2.num_sides
# Calcula a frequência de cada valor
for value in range(2, max_result + 1):
    # Conta as ocorrências do valor
    frequency = results.count(value)
    # Adiciona a frequência à lista
    frequencies.append(frequency)

# Imprime as frequências
print(frequencies)

# Visualiza os resultados
# Cria um gráfico de barras.
hist = pygal.Bar()
# Define o título.
hist.title = "Results of rolling two D8 dice 1000 times."
# Define os rótulos do eixo x.
hist.x_labels = [value for value in range(2,max_result + 1)]
# Define o título do eixo x.
hist.x_title = "Result"
# Define o título do eixo y.
hist.y_title = "Frequency of Result"
# Adiciona os dados ao gráfico.
hist.add('D8 + D8', frequencies)

# Salva o gráfico em SVG.
hist.render_to_file("dice_visual.svg")
# Informa que o gráfico foi salvo.
print("Gráfico salvo como dice_visual.svg")