#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 18:07:56 2025

@author: sergio
"""

# Importando biblioteca
import matplotlib.pyplot as plt

# Importando classe
from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    
    # Criando instância
    rw = RandomWalk()
    # Definindo passeio aleatório
    rw.fill_walk()

    #Plotando gráfico de distribuição
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show() # Mostra gráfico
    
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break