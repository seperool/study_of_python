#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:25:50 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Lista de valores do eixo x
x = list(range(1,6))

# Cria uma lista de números ao cubo
# Lista de valores do eixo y
y = [value**3 for value in x]
print(y)

# Plotagem

# Cria um gráfico de linha com a lista de números quadrados
plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolor='none', s=40)

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
plt.savefig("plot_cubo5-colormap.png", bbox_inches='tight')