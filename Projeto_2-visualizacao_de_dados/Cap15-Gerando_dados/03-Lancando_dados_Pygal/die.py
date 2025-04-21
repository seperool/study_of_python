#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 18:09:47 2025

@author: sergio
"""

from random import randint

class Die():
    """Uma classe que representa um único dado."""
    
    def __init__(self, num_sides=6):
        """Supõe que seja um dado de seis lados"""
        self.num_sides=num_sides
        
    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados"""
        return randint(1, self.num_sides)