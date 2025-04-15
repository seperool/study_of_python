#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 13:45:33 2025

@author: sergio
"""


# Importando biblioteca
import matplotlib.pyplot as plt

# Importando classe
from random_walk_mod import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    
    # Criando instância
    rw = RandomWalk(5000)
    # Definindo passeio aleatório
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    # Plotando gráfico de distribuição
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # Enfatiza o primeiro e último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Obtém a referência aos eixos correntes
    ax = plt.gca()
    #Removendo eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # Define o tamanho da janela de plotagem
    plt.figure(figsize=(10,6))
    
    plt.show() # Mostra gráfico
    
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break