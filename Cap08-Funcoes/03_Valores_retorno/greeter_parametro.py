#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:02:10 2024

@author: sergio
"""

def greet_user(username): #Define o nome e parâmetros da função
    """Exibe um saudação simples.""" #Docstring
    print("Hello " + username.title() + "!") #Bloco de programação

greet_user('jesse') #Chama a função e passa um argumento