#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:29:56 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Lista de valores do eixo x
input_values = list(range(1,5001))
# Cria uma lista de números ao cubo
# Lista de valores do eixo y
cubos = [value**3 for value in input_values]

# Plotagem

# Cria um gráfico de linha com a lista de números quadrados
plt.scatter(input_values, cubos, c=cubos, cmap=plt.cm.Blues, 
         edgecolor='none', s=40)
# Especifica o intervalo dos eixos
plt.axis([0,5000,0,1e11])

# Define o título do gráfico
plt.title("Square Numbers", fontsize=24)
# Define o rótulo do eixo x
plt.xlabel("Value", fontsize=14)
# Define o rótulo do eixo y
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos dos eixos
plt.tick_params(axis='both', labelsize=14)

# Exibe o gráfico criado
plt.show()

# Salva o gráfico de maneira automática
# Argumentos: nome do gráfico e remove espaços em branco
plt.savefig("plot_cubos5000-colormap.png", bbox_inches='tight')