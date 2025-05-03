#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:05:44 2025

@author: sergio
"""

# Importa bibliotecas
# Importa pygal para gráficos
import pygal
# Importa a classe Die
from die import Die

# Cria dado de 6 lados
d6 = Die()
# Cria dado de 10 lados
d10 = Die(10)

# Lista para armazenar resultados
results = []
# Simula 50000 lançamentos
for _ in range(50000):
    # Soma os lançamentos
    result = d6.roll() + d10.roll()
    # Adiciona resultado
    results.append(result)

# Imprime resultados
print(results)

# Lista para armazenar frequências
frequencies = []
# Valor máximo da soma
max_result = d6.num_sides + d10.num_sides
# Calcula frequência de cada soma
for value in range(2, max_result + 1):
    # Conta ocorrências
    frequency = results.count(value)
    # Adiciona frequência
    frequencies.append(frequency)

# Imprime frequências
print(frequencies)

# Cria gráfico de barras
hist = pygal.Bar()
# Define título
hist.title = "Resultados ao lançar um D6 e um D10 50.000 vezes"
# Define rótulos do eixo x
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
# Define título do eixo x
hist.x_title = "Soma dos Resultados"
# Define título do eixo y
hist.y_title = "Frequência da Soma"
# Adiciona dados ao gráfico
hist.add('D6 + D10', frequencies)

# Salva o gráfico
hist.render_to_file("different_dice_visual.svg")
# Informa que o gráfico foi salvo
print("Gráfico salvo como different_dice_visual.svg")