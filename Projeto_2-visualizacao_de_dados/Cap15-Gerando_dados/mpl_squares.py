#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:14:32 2025

@author: sergio
"""

import matplotlib.pyplot as plt # Importa a biblioteca matplotlib para criação de gráficos

squares = [1,4,9,16,25]         # Cria uma lista de números quadrados
plt.plot(squares)               # Plota a lista de números quadrados em um gráfico de linha
plt.show()                      # Exibe o gráfico criado