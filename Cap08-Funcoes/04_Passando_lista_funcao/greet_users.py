#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:54:32 2024

@author: sergio
"""

#Função e listas
#Passando listas para função

def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        print("Hello, " + name.title() + "!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)