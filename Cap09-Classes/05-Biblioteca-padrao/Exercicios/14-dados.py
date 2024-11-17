#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 03:27:33 2024

@author: sergio
"""

#Importando biblioteca-padrão
from random import randint

#Classe
class Die():
    """Define um dado."""
    
    #Atributos
    def __init__(self):
        #Atributos
        self.sides = 6 #Default dado de 6 lados
    
    #Métodos
    def roll_die(self):
        """Rola o dado, gera um número aleatório da rolagem."""
        num = randint(1, self.sides)
        print(f"Dado: {num}")
    
    def sides_die(self,sides):
        """Define o número de lados do dado."""
        self.sides = sides
        print(f"\nO dado agora tem {self.sides} lados!")

#Jogando um dado de 6 lados
#Instância
d6 = Die()

#Chamadas
##Rolando os dados
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()
d6.roll_die()

#Jogando um dado de 10 lados
#Instância
d10 = Die()

#Chamadas
#Definindo o número de lados do dado para 10
d10.sides_die(10)

#Rolando os dados
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()
d10.roll_die()

#Jogando um dado de 20 lados
#Instância
d20 = Die()

#Definindo o número de lados do dado para 10
d20.sides_die(20)

#Rolando os dados
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()
d20.roll_die()