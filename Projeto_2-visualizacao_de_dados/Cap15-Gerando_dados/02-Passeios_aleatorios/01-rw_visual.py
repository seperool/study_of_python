#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 16:50:12 2025

@author: sergio
"""

# Importando biblioteca
import matplotlib.pyplot as plt

# Importando classe
from random_walk import RandomWalk

# Criando instância
rw = RandomWalk()
# Definindo passeio aleatório
rw.fill_walk()

#Plotando gráfico de distribuição
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show() # Mostra gráfico

# Salvando gráfico
plt.savefig('rw_scatter.png', bbox_inches='tight')