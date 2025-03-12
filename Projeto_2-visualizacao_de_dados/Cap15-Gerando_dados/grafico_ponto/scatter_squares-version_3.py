#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:48:43 2025

@author: sergio
"""

import matplotlib.pyplot as plt

# Cria uma lista de valores x de 1 a 1000.
x_values = list(range(1,1001))
# Cria uma lista de valores y, sendo o quadrado de cada valor x.
y_values = [x**2 for x in x_values]

# Cria um gráfico de dispersão com os valores x e y, tamanho dos pontos 40.
plt.scatter(x_values, y_values, s=40)

# Adiciona uma grade ao gráfico.
plt.grid()

# Define o título do gráfico.
plt.title("Square Numbers", fontsize=24)
# Define o rótulo do eixo x.
plt.xlabel("Value", fontsize=14)
# Define o rótulo do eixo y.
plt.ylabel("Square of Value", fontsize=14)
# Define o tamanho dos rótulos dos eixos.
plt.tick_params(axis='both', which='major', labelsize=14)

# Define os limites dos eixos x e y.
plt.axis([0,1100,0,1100000])

# Exibe o gráfico.
plt.show()

# Salva o gráfico em um arquivo PNG.
plt.savefig("grafico_de_pontos_automaticos.png", bbox_inches='tight')