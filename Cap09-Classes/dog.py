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

#Criando instâncias a partir da classe
my_dog = Dog('willie',6)
your_dog = Dog('lucy', 3)

#Acessando atributos
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Chamando métodos
my_dog.sit()
my_dog.roll_over()

#Acessando atributos
print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")

#Chamando métodos
your_dog.sit()
your_dog.roll_over()