#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 20:17:16 2025

@author: sergio
"""

import matplotlib.pyplot as plt

# Cria lista de valores x de 1 a 1000.
x_values = list(range(1,1001))
# Cria lista de valores y (quadrado de x).
y_values = [x**2 for x in x_values]

# Gera gráfico de dispersão (x, y), com cores e tamanho dos pontos.
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolors='none' ,s=40)

# Adiciona grade ao gráfico.
plt.grid()

# Define título do gráfico.
plt.title("Square Numbers", fontsize=24)
# Define rótulo do eixo x.
plt.xlabel("Value", fontsize=14)
# Define rótulo do eixo y.
plt.ylabel("Square of Value", fontsize=14)
# Define tamanho dos rótulos dos eixos.
plt.tick_params(axis='both', which='major', labelsize=14)

# Define limites dos eixos x e y.
plt.axis([0,1100,0,1100000])

# Exibe o gráfico.
plt.show()

# Salva gráfico em arquivo PNG.
plt.savefig("grafico_de_pontos_automaticos-colormap.png", bbox_inches='tight')