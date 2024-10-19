#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 13:19:35 2024

@author: sergio
"""

#Cria a classe Dog
#Nome da classe em maiusculo por ser uma classe
class Dog():
    """Uma tentativa simples de modelar um cachorro."""
    
    #Atributos
    def __init__(self, name, age):
        """Inicializando os atributos name e age."""
        self.name = name
        self.age = age
    
    #Metodos
    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!")