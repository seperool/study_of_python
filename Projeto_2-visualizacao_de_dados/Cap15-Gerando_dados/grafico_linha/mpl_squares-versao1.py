#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 19:32:36 2025

@author: sergio
"""

# Importa a biblioteca matplotlib para criação de gráficos
import matplotlib.pyplot as plt 

# Cria uma lista de números quadrados
squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5) #Espessura da linha

# Define o titulo do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

# Exibe o tamanho dos rótulos das marcações
plt.tick_params(axis='both',labelsize=14)

# Exibe o gráfico criado
plt.show()