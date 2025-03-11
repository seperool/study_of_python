#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 20:50:52 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criar gráficos
import matplotlib.pyplot as plt

# Cria um gráfico de dispersão com um ponto na coordenada (2, 4)
#s = tamanho do ponto
plt.scatter(2,4, s=200)
# Adiciona uma grade ao gráfico
plt.grid()

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig("grafico_de_ponto.png", bbox_inches='tight')

# Exibe o gráfico
plt.show()