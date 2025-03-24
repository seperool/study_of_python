#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 22:15:51 2025

@author: sergio
"""

from random import choice

class RandomWalk():
    """Uma classe para gerar caminhadas aleatórias."""

    def __init__(self, num_points=5000):
        """Inicializa os atributos de uma caminhada."""
        self.num_points = num_points
        
        # Inicializa a caminhada na origem (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Calcula todos os pontos da caminhada."""
        # Mantém a caminhada até atingir o número desejado de pontos.
        while len(self.x_values) < self.num_points:
            # Decide a direção e a distância para o passo x.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            # Decide a direção e a distância para o passo y.
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Rejeita movimentos que não vão a lugar nenhum.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calcula os próximos valores x e y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            # Adiciona os novos valores x e y às listas.
            self.x_values.append(next_x)
            self.y_values.append(next_y)