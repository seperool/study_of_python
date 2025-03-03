#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:14:32 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criação de gráficos
import matplotlib.pyplot as plt

# Lista de valores do eixo x
input_values = [1,2,3,4,5]
# Cria uma lista de números quadrados
# Lista de valores do eixo y
squares = [1,4,9,16,25]
# Cria um gráfico de linha com a lista de números quadrados
plt.plot(input_values,squares,linewidth=5)

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
plt.savefig("plot_linear.png", bbox_inches='tight')