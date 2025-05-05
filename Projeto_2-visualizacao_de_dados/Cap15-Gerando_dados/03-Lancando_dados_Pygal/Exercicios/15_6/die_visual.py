#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:16:03 2025

@author: sergio
"""

# Importando bibliotecas
# Importa a classe Die do módulo die
from die import Die
# Importa a biblioteca pygal para gráficos.
import pygal

# Cria um dado de 6 lados, instância
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

# Visualiza os resultados
# Cria um gráfico de barras.
hist = pygal.Bar()
# Define o título.
hist.title = "Results of rolling one D6 1000 times."
# Define os rótulos do eixo x.
hist.x_labels = [value for value in range(1,D6.num_sides+1)]
# Define o título do eixo x.
hist.x_title = "Result"
# Define o título do eixo y.
hist.y_title = "Frequency of Result"
# Adiciona os dados ao gráfico.
hist.add('D6', frequencies)

# Salva o gráfico em SVG.
hist.render_to_file("die_visual.svg")
# Informa que o gráfico foi salvo.
print("Gráfico salvo como die_visual.svg")