#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 20:36:02 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criar gráficos
import matplotlib.pyplot as plt

# Eixos x e y
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

# Cria um gráfico de dispersão
plt.scatter(x_values,y_values,s=100)
# Adiciona uma grade ao gráfico
plt.grid()

# Define o título do gráfico com tamanho da fonte.
plt.title("Square Numbers", fontsize=24)
# Define o rótulo do eixo x com tamanho da fonte.
plt.xlabel("Value", fontsize=14)
# Define o rótulo do eixo y com tamanho da fonte.
plt.ylabel("Square of Value", fontsize=14)
# Ajusta o tamanho da fonte dos rótulos dos eixos.
plt.tick_params(axis='both', which='major', labelsize=14)

# Salva o gráfico em um arquivo PNG, ajustando o tamanho para evitar cortes.
plt.savefig("grafico_de_pontos.png", bbox_inches='tight')

# Exibe o gráfico
plt.show()