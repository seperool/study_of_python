#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:32:05 2025

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

    point_numbers = list(range(rw.num_points))
    #Plotando gráfico de distribuição
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
            edgecolors='none', s=15)
    
    #Enfatiza o primeiro e último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Obtém a referência aos eixos correntes
    ax = plt.gca()
    #Removendo eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show() # Mostra gráfico
    
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break